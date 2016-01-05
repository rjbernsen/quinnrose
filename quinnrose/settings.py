"""
Django settings for quinnrose project.

Generated by 'django-admin startproject' using Django 1.8.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from django.contrib import messages
from quinnrose.secrets import Secrets
# from django.contrib.messages import constants as message_constants

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

IN_PRODUCTION = True
# print('sys.argv = {}'.format(sys.argv))
if 'manage.py' in sys.argv[0]:
    IN_PRODUCTION = False
print('IN_PRODUCTION = {}'.format(IN_PRODUCTION))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print('BASE_DIR = {}'.format(BASE_DIR))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = Secrets.SECRET_KEY

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'quinnrose.elasticbeanstalk.com'
]
# ALLOWED_HOSTS = ['localhost']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'quinnrose',
    'artist',
    'organization',
    'community',
    'copyright',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.admindocs.middleware.XViewMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'quinnrose.middleware.MySessionProcessingMiddleware',
)

ROOT_URLCONF = 'quinnrose.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'quinnrose/templates'),
            os.path.join(BASE_DIR,'artist/templates'),
            os.path.join(BASE_DIR,'organization/templates'),
            os.path.join(BASE_DIR,'community/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
#             'loaders': [
#                 ('django.template.loaders.cached.Loader', [
#                     'django.template.loaders.filesystem.Loader',
#                     'django.template.loaders.app_directories.Loader',
#                 ]),
#             ],
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.template.context_processors.media',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media'
            ],
        },
    },
]

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

WSGI_APPLICATION = 'quinnrose.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': Secrets.DATABASE_NAME,
        'USER': Secrets.DATABASE_USER,
        'PASSWORD': Secrets.DATABASE_PASSWORD,
        'HOST': Secrets.DATABASE_HOST,   # Or an IP Address that your DB is hosted on
        'PORT': Secrets.DATABASE_PORT,
    }
}
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chicago'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
# if DEBUG: 
#     STATIC_ROOT = os.path.join(BASE_DIR, '/static')
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static') 
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# print('STATIC_ROOT = {}'.format(STATIC_ROOT))
STATIC_MAIN_APP = os.path.join(BASE_DIR,'quinnrose', 'static')
STATIC_ARTIST_APP = os.path.join(BASE_DIR,'artist', 'static')
STATIC_ORGANIZATION_APP = os.path.join(BASE_DIR,'organization', 'static')
STATIC_COMMUNITY_APP = os.path.join(BASE_DIR,'community', 'static')
# print('STATIC_MAIN_APP = {}'.format(STATIC_MAIN_APP))

STATICFILES_DIRS = (
    STATIC_MAIN_APP,
    STATIC_ARTIST_APP,
    STATIC_ORGANIZATION_APP,
    STATIC_COMMUNITY_APP,
    MEDIA_ROOT
#         STATIC_ROOT,
)
# print('STATICFILES_DIRS = {}'.format(STATICFILES_DIRS))


# # List of finder classes that know how to find static files in
# # various locations.
# STATICFILES_FINDERS = (
#     'django.contrib.staticfiles.finders.FileSystemFinder',
#     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
# )

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger'  # For bootstrap class names
}

EMAIL_USE_TLS       = True
EMAIL_HOST          = Secrets.EMAIL_HOST
EMAIL_HOST_USER     = Secrets.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = Secrets.EMAIL_HOST_PASSWORD
EMAIL_PORT          = Secrets.EMAIL_PORT

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'null': {
            'level':'DEBUG',
            'class':'django.utils.log.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
        'file_functional_tests': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'functional_tests.log'),
            'formatter': 'verbose',
            'maxBytes': 1024*1024* 5, # 5 MB
            'backupCount': 1,
        },
        'file_tests': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'tests.log'),
            'formatter': 'verbose',
            'maxBytes': 1024*1024* 5, # 5 MB
            'backupCount': 1,
        },
        'production': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs', 'production.log'),
            'formatter': 'verbose',
            'maxBytes': 1024*1024* 5, # 5 MB
            'backupCount': 1,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['null'],
            'propagate': False, # Ignore other handlers, i.e. stdout
        },
        'quinnrose.functional_tests': {
            'handlers': ['file_functional_tests'],
            'propagate': False, # Ignore other handlers, i.e. stdout
        },
        'quinnrose.quinnrose.tests': {
            'handlers': ['file_tests'],
            'propagate': False, # Ignore other handlers, i.e. stdout
        },
        'quinnrose': {
            'handlers': ['production'],
            'propagate': False, # Ignore other handlers, i.e. stdout
        },
    },
    'root': {'level': 'INFO'},
}

COPY_START_YEAR = 2015

if IN_PRODUCTION:
    import quinnrose.settings_prod
else:
    import quinnrose.settings_dev
print('DEBUG = {}'.format(DEBUG))

# if IN_PRODUCTION:
#     from quinnrose.settings_prod import (
#         DEBUG as DEBUG_prod, 
#         STATICFILES_STORAGE as STATICFILES_STORAGE_prod,
#         CACHES as CACHES_prod
#     )
# 
#     DEBUG = DEBUG_prod
#     STATICFILES_STORAGE = STATICFILES_STORAGE_prod
#     CACHES = CACHES_prod
# 
# else:
#     from quinnrose.settings_dev import (
#         DEBUG as DEBUG_dev, 
#         CACHES as CACHES_dev
#     )
# 
#     DEBUG = DEBUG_dev
#     CACHES = CACHES_dev

