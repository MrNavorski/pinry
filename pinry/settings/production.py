from pinry.settings import *

import os


DEBUG = False
TEMPLATE_DEBUG = DEBUG
#
# # TODO: I recommend using psycopg2 w/ postgres but sqlite3 is good enough.
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(SITE_ROOT, 'production.db'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'nice_design',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': 'outbrixd321',  # Not used with sqlite3.
        'HOST': '10.162.82.194',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}

# TODO: Be sure to set this.
SECRET_KEY = ''
