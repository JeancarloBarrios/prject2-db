import tweepy



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


def save_tweet(tweet):
    api = _set_twitter_session()
