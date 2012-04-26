# -*- coding: utf-8 -*-

import sys
import locale
import twitter
import redis
import json
import time
from random import shuffle
from urllib2 import URLError
import functools

def pp(_int):  # For nice number formatting
    locale.setlocale(locale.LC_ALL, '')
    return locale.format('%d', _int, True)

# Twitter API helpers and data gathering functions

def makeTwitterRequest(t, twitterFunction, max_errors=3, *args, **kwArgs):
    wait_period = 2
    error_count = 0
    while True:
        try:
            return twitterFunction(*args, **kwArgs)
        except twitter.api.TwitterHTTPError, e:
            error_count = 0
            wait_period = handleTwitterHTTPError(e, t, wait_period)
            if wait_period is None:
                return
        except URLError, e:
            error_count += 1
            print >> sys.stderr, "URLError encountered. Continuing."
            if error_count > max_errors:
                print >> sys.stderr, "Too many consecutive errors...bailing out."
                raise

def getRemainingHits(t):
    return t.account.rate_limit_status()['remaining_hits']

# Handle the common HTTPErrors. Return an updated value for wait_period
# if the problem is a 503 error. Block until the rate limit is reset if
# a rate limiting issue
def handleTwitterHTTPError(e, t, wait_period=2):

    if wait_period > 3600: # Seconds
        print >> sys.stderr, 'Too many retries. Quitting.'
        raise e

    if e.e.code == 401:
        print >> sys.stderr, 'Encountered 401 Error (Not Authorized)'
        return None
    elif e.e.code in (502, 503):
        print >> sys.stderr, 'Encountered %i Error. Will retry in %i seconds' % (e.e.code,
                wait_period)
        time.sleep(wait_period)
        wait_period *= 1.5
        return wait_period
    elif getRemainingHits(t) == 0:
        status = t.account.rate_limit_status()
        now = time.time()  # UTC
        when_rate_limit_resets = status['reset_time_in_seconds']  # UTC
        sleep_time = max(when_rate_limit_resets - now, 5) # Prevent negative numbers
        print >> sys.stderr, 'Rate limit reached: sleeping for %i secs' % (sleep_time, )
        time.sleep(sleep_time)
        return 2
    else:
        raise e


# A template-like function that can get friends or followers depending on
# the function passed into it via func.

def getFriendsOrFollowersUsingFunc(
    func,
    key_name,
    t, # Twitter connection
    r, # Redis connection
    screen_name=None,
    limit=10000,
    ):

    cursor = -1

    result = []
    while cursor != 0:
        response = makeTwitterRequest(t, func, screen_name=screen_name, cursor=cursor)
        for _id in response['ids']:
            result.append(_id)
            r.sadd(getRedisIdByScreenName(screen_name.lower(), key_name), _id)

        cursor = response['next_cursor']
        scard = r.scard(getRedisIdByScreenName(screen_name, key_name))
        print >> sys.stderr, 'Fetched %s ids for %s' % (scard, screen_name)
        if scard >= limit:
            break

    return result

def getUserInfo(
    t, # Twitter connection
    r, # Redis connection
    screen_names=[],
    user_ids=[],
    verbose=False,
    sample=1.0,
    ):
    
    # if a string is passed as a normal arg it loads corrupt data in Redis.
    if type(screen_names).__name__ != 'list':
        raise TypeError("getUserInfo needs lists as named arguments.")

    # Sampling technique: randomize the lists and trim the length.
    if sample < 1.0:
        for lst in [screen_names, user_ids]:
            shuffle(lst)
            lst = lst[:int(len(lst) * sample)]

    info = []
    while len(screen_names) > 0:
        screen_names_str = ','.join(screen_names[:100])
        screen_names = screen_names[100:]

        response = makeTwitterRequest(t, 
                                      t.users.lookup,
                                      screen_name=screen_names_str)
        
        if response is None:
            break
                                    
        if type(response) is dict:  # Handle api quirk
            response = [response]
        for user_info in response:
            r.set(getRedisIdByScreenName(user_info['screen_name'].lower(), 'info.json'),
                  json.dumps(user_info))
            r.set(getRedisIdByUserId(user_info['id'], 'info.json'), 
                  json.dumps(user_info))
        info.extend(response)

    while len(user_ids) > 0:
        user_ids_str = ','.join([str(_id) for _id in user_ids[:100]])
        user_ids = user_ids[100:]

        response = makeTwitterRequest(t, 
                                      t.users.lookup,
                                      user_id=user_ids_str)
        
        if response is None:
            break
                                    
        if type(response) is dict:  # Handle api quirk
            response = [response]
        for user_info in response:
            r.set(getRedisIdByScreenName(user_info['screen_name'].lower(), 'info.json'),
                  json.dumps(user_info))
            r.set(getRedisIdByUserId(user_info['id'], 'info.json'), 
                  json.dumps(user_info))
            
            # addition for a hash with all seen id->screenname pairs   
            r.hset('twitter_id_to_screenname', 
                   user_info['id'], user_info['screen_name'].lower())
            
        info.extend(response)
    return info

# will receive the partial results from main.py
def crawl(getInfo, getFriends, getFollowers, 
    screen_names=[], 
    friends_limit=10000,
    followers_limit=10000,
    depth=1,
    friends_sample=0.2,
    followers_sample=0.0):
    
    getInfo(screen_names=screen_names)
    for screen_name in screen_names:
        
        friend_ids = getFriends(screen_name, limit=friends_limit)
        followers_ids = getFollowers(screen_name, limit=followers_limit)
        
        friends_info = getInfo(user_ids=friend_ids, sample=friends_sample)
        followers_info = getInfo(user_ids=followers_ids, sample=followers_sample)
        
        next_queue = [u['screen_name'] for u in friends_info + followers_info]

        d = 1
        while d < depth:
            d += 1
            (queue, next_queue) = (next_queue, [])
            for _screen_name in queue:
                friend_ids = getFriends(_screen_name, limit=friends_limit)
                follower_ids = getFollowers(_screen_name, limit=followers_limit)

                next_queue.extend(friend_ids + follower_ids)

                # Note that this function takes a kw between 0.0 and 1.0 called
                # sample that allows you to crawl only a random sample of nodes
                # at any given level of the graph

                getInfo(user_ids=next_queue)
    

# Redis helpers and data retrieving functions

def getRedisIdByScreenName(screen_name, key_name):
    return 'screen_name$' + screen_name + '$' + key_name

def getRedisIdByUserId(user_id, key_name):
    return 'user_id$' + str(user_id) + '$' + key_name

def restoreFriendsOrFollowers(r, key_name, screen_name=None):
    '''Loads user friends or followers set from Redis
    '''
    if not screen_name or not key_name:
        raise TypeError("Can't work with None as args")
        
    key = getRedisIdByScreenName(screen_name, key_name)
    print key
    if r.exists(key):
        return  r.smembers(key)
    else:
        return IndexError(screen_name + " is not on this database")

def friendsFollowersInCommon(r, screen_names):
    '''Computes the common friends and followers between given screen names
    '''
    r.sinterstore('temp$friends_in_common', 
                  [getRedisIdByScreenName(screen_name, 'friend_ids') 
                      for screen_name in screen_names])
    
    r.sinterstore('temp$followers_in_common',
                  [getRedisIdByScreenName(screen_name, 'follower_ids')
                      for screen_name in screen_names])
    
    print 'Friends in common for %s: %s' % (', '.join(screen_names),
            pp(r.scard('temp$friends_in_common')))
    
    print 'Followers in common for %s: %s' % (', '.join(screen_names),
            pp(r.scard('temp$followers_in_common')))
    
    friends = r.smembers('temp$friends_in_common')
    followers = r.smembers('temp$followers_in_common')
    r.delete('temp$friends_in_common')
    r.delete('temp$followers_in_common')
    return friends, followers
