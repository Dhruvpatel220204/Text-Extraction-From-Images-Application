import os
from os import environ

class config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'Sumit@143'

    UPLOADS = "/Users/sumitkumarsingh/Downloads/Text Extraction Flask App/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(config):
    DEBUG = False
