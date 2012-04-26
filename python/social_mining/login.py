# -*- coding: utf-8 -*-

import os
import json
import redis
import twitter
from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance

def from_static():

    # Go to http://twitter.com/apps/new to create an app and get these items
    # See also http://dev.twitter.com/pages/oauth_single_token

    APP_NAME = ''
    CONSUMER_KEY = ''
    CONSUMER_SECRET = ''
    TOKEN_FILE = 'out/twitter.oauth'

    try:
        (oauth_token, oauth_token_secret) = read_token_file(TOKEN_FILE)
    except IOError, e:
        (oauth_token, oauth_token_secret) = oauth_dance(APP_NAME, CONSUMER_KEY,
                CONSUMER_SECRET)

        if not os.path.isdir('out'):
            os.mkdir('out')

        write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)
         
    return twitter.Twitter(domain='api.twitter.com', api_version='1',
                        auth=twitter.oauth.OAuth(oauth_token, oauth_token_secret,
                        CONSUMER_KEY, CONSUMER_SECRET))

def from_redis(r, key):
    '''Creates a twitter.Twitter class based on a saved JSON string in Redis.
    Format is "twitterlogin$SCREENAME"
    '''
    try:
        return twitter.Twitter(domain='api.twitter.com', api_version='1',
                    auth=twitter.oauth.OAuth(
                    r.hget(key, 'oauth_token'), 
                    r.hget(key, 'oauth_token_secret'),
                    r.hget(key, 'consumer_key'),
                    r.hget(key, 'consumer_secret')))
    except:
        print "No such key or missing values"
