from .base import *

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS += [
    'rest_framework_swagger',
]

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'UNAUTHENTICATED_USER': None,
}

config = configparser.ConfigParser()
config.read('env.ini')

DATABASES = {
    'default': {
        'ENGINE': config['LOCAL']['DATABASE_ENGINE'],
        'NAME': config['LOCAL']['DATABASE_NAME'],
        'USER': config['LOCAL']['DATABASE_USER'],
        'PASSWORD': config['LOCAL']['DATABASE_PASSWORD'],
        'HOST': config['LOCAL']['DATABASE_HOST'],
        'PORT': config['LOCAL']['DATABASE_PORT'],
    }
}
