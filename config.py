import os
class Config(object):
    MONGO_HOST = os.environ.get('MONGO_HOST')
    MONGO_PORT = os.environ.get('MONGO_PORT')
    MONGO_DATABASE = os.environ.get('MONGO_DATABASE')
    MONGO_URI = 'mongodb://' + MONGO_HOST + ':' + MONGO_PORT + '/' + MONGO_DATABASE
