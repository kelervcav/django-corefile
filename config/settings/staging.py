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
        'ENGINE': config['STAGING']['DATABASE_ENGINE'],
        'NAME': config['STAGING']['DATABASE_NAME'],
        'USER': config['STAGING']['DATABASE_USER'],
        'PASSWORD': config['STAGING']['DATABASE_PASSWORD'],
        'HOST': config['STAGING']['DATABASE_HOST'],
    }
}
