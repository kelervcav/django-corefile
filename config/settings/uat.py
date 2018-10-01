from .base import *
import configparser

config = configparser.ConfigParser()
config.read('env.ini')

DEBUG = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += [
    'rest_framework_swagger',
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'UNAUTHENTICATED_USER': None,
}

DATABASES = {
    'default': {
        'ENGINE': config['UAT']['DATABASE_ENGINE'],
        'NAME': config['UAT']['DATABASE_NAME'],
        'USER': config['UAT']['DATABASE_USER'],
        'PASSWORD': config['UAT']['DATABASE_PASSWORD'],
        'HOST': config['UAT']['DATABASE_HOST'],
    }
}
