from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'dummy'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, 'db.sqlite3'),
    }
}