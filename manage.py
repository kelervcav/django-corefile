#!/usr/bin/env python
import os
import sys
import configparser

config = configparser.ConfigParser()
config.read('env.ini')

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', config['SETTINGS']['CONFIG'])
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
