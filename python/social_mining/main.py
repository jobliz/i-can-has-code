# -*- coding: utf-8 -*-

"""
Call "from main import *" to load the whole workspace into IPython

Some redis keys to keep in mind:
'twitter_id_to_screenname'
'screen_name$jobliz$follower_ids'
'screen_name$jobliz$friend_ids'
"""

import functools
import redis
import login
import util

r0 = redis.Redis(db=0) # miscellaneous data and login info
r1 = redis.Redis(db=1) # twitter mining storage
t = login.from_redis(r0, 'twitterlogin$jobliz')

getInfo = functools.partial(util.getUserInfo, t, r1)

getFollowers = functools.partial(util.getFriendsOrFollowersUsingFunc,
                                 t.followers.ids, 'follower_ids', t, r1)

getFriends = functools.partial(util.getFriendsOrFollowersUsingFunc, 
                                 t.friends.ids, 'friend_ids', t, r1)



