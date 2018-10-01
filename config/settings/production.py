from .base import *
import configparser

config = configparser.ConfigParser()
config.read('env.ini')

DEBUG = False

ALLOWED_HOSTS = ['*']

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

DATABASES = {
    'default': {
        'ENGINE': config['PRODUCTION']['DATABASE_ENGINE'],
        'NAME': config['PRODUCTION']['DATABASE_NAME'],
        'USER': config['PRODUCTION']['DATABASE_USER'],
        'PASSWORD': config['PRODUCTION']['DATABASE_PASSWORD'],
        'HOST': config['PRODUCTION']['DATABASE_HOST'],
    }
}
