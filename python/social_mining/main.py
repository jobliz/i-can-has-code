# -*- coding: utf-8 -*-

"""
Call "from main import *" to load the whole workspace into IPython

Some redis keys to keep in mind:
'twitter_id_to_screenname'
'screen_name$jobliz$follower_ids'
'screen_name$jobliz$friend_ids'

Ideas:
* A dict interface to -some- Redis structures, maybe hashes
"""

import functools
import redis
import login
import util

# Redis and Twitter connection objects

r0 = redis.Redis(db=0) # miscellaneous data and login info
r1 = redis.Redis(db=1) # twitter mining storage
t = login.from_redis(r0, 'twitterlogin$jobliz')


# Twitter info and contacts harvesting

getInfo = functools.partial(util.getUserInfo, t, r1)

getFollowers = functools.partial(util.getFriendsOrFollowersUsingFunc,
                                 t.followers.ids, 'follower_ids', t, r1)

getFriends = functools.partial(util.getFriendsOrFollowersUsingFunc, 
                                 t.friends.ids, 'friend_ids', t, r1)

crawlData = functools.partial(util.crawl, getInfo, getFriends, getFollowers)

# Reloading data from Redis

restoreFollowers = functools.partial(
    util.restoreFriendsOrFollowers, r1, 'follower_ids')

restoreFriends = functools.partial(
    util.restoreFriendsOrFollowers, r1, 'friend_ids')

