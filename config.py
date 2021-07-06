import os

class vars(object):
    api_id = os.getenv('api_id', 123456)
    api_hash = os.getenv('api_hash' ,'abcdefghxxxxx')
    bot_token = os.getenv('bot_token', None)
    some_secret = os.getenv('some_secret', None)