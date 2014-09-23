from pinry.settings import *

import os


DEBUG = True
TEMPLATE_DEBUG = DEBUG

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(SITE_ROOT, 'development.db'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'nice_design',  # Or path to database file if using sqlite3.
        'USER': 'root',  # Not used with sqlite3.
        'PASSWORD': 'root',  # Not used with sqlite3.
        'HOST': 'localhost',  # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '3306',  # Set to empty string for default. Not used with sqlite3.
    }
}

SECRET_KEY = 'fake-key'

SOUTH_MIGRATION_MODULES = {
        'taggit': 'taggit.south_migrations',
}
ALLOWED_HOSTS = ['*']

