import os

SECRET_KEY = 'something_special'


class Config(object):
    TESTING = False


class DevelopmentConfig(Config):
    ENV = "development"
    TESTING = True
    DEBUG = True
    PROPAGATE_EXCEPTIONS = True
    TRAP_BAD_REQUEST_ERRORS = True
    TEMPLATES_AUTO_RELOAD = True


# basedir = os.path.abspath(os.path.dirname(__file__))
