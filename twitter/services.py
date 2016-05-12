# Service to manage twiiter calls
import tweepy
from mongo import services as mg
import json
# Sets the wtitter session
def _set_twitter_session():
    auth = tweepy.OAuthHandler(
        'N7ssfqpl967rfoz7Wc0utSS4A',
        'y2mk8vD87qFcRoyXdZBt0QURjFVXbfX24PjrlFotXLZjySvnbP'
    )
    auth.set_access_token(
        '2471571410-PvJ7d5f6MFwIT3SQqyGFOUVKT7GXjhSpMqkOceJ',
        'peAkOgQQjvkeXTR1kgLeTQho9TEIxCuLz4cDpeWzs38oc'
    )
    api = tweepy.API(auth)
    return api


def get_tweets(user):
    api = _set_twitter_session()
    result = api.user_timeline(user)
    array = []
    for elem in result:
        el = json.dumps(elem._json)
        mg.insertItem('tweets', el)
        array.append(el)
    return array
