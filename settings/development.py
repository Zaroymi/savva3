from .common import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'development'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost']

import os



BASE_DIR = os.path.dirname(os.path.dirname(__file__))
REPOSITORY_ROOT = os.path.dirname(BASE_DIR)


STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(REPOSITORY_ROOT, 'static/')

MEDIA_URL = '/media/'
#MEDIA_ROOT = os.path.join(REPOSITORY_ROOT, 'media/')
