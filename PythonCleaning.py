
import tweepy
from tweepy.auth import OAuthHandler
from twython import Twython
import csv
'''

consumer_key = "9ZR36AfiJnk6NtqMhfXT9NSK3"
consumer_secret = "ct0T7wsLPn0mWDCd5zq23SJBBcKYSZ18hy4HHetzxMvMBL8pPg"
access_key = "1435440192345739264-iOXxmxwFxugyax7YlbgFTRthz5br12"
access_secret = "WzAsqNbxTTHRUk4addWnTLRm51YrQvY7iC47PxOOiuDHf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

twitter = Twython(
    consumer_key, consumer_secret,
    access_key, access_secret)

tweet = twitter.show_status(id=981117681733722112)
print(tweet['text'])
'''


API_KEY = "9ZR36AfiJnk6NtqMhfXT9NSK3"
API_SECRET = "ct0T7wsLPn0mWDCd5zq23SJBBcKYSZ18hy4HHetzxMvMBL8pPg"
ACCESS_TOKEN = "1435440192345739264-iOXxmxwFxugyax7YlbgFTRthz5br12"
ACCESS_TOKEN_SECRET = "WzAsqNbxTTHRUk4addWnTLRm51YrQvY7iC47PxOOiuDHf"

auth = OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
print(api.me().name)
