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
from django.contrib import messages
# from django.contrib.messages import constants as message_constants

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'krr)oi)qtu2m)jhk!)nr&-2_hl94u=24n&1jq22x11x6g7&h&a'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DOMAIN = 'localhost'
ALLOWED_HOSTS = [DOMAIN,'127.0.0.1/']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'copyright',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'quinnrose.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'quinnrose/templates')
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'quinnrose.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quinnrose',
        'USER': 'quinnrose',
        'PASSWORD': 'quinnrose',
        'HOST': 'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}
import sys
if 'test' in sys.argv:
    DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATIC_GLOBAL = os.path.join(BASE_DIR, 'static')
# if 'test' in sys.argv:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# else:
#     STATICFILES_DIRS = (
#         STATIC_GLOBAL,
#     )
STATICFILES_DIRS = (
        STATIC_GLOBAL,
)
# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder"
# )

MESSAGE_TAGS = {
    messages.DEBUG: 'debug',
    messages.INFO: 'info',
    messages.SUCCESS: 'success',
    messages.WARNING: 'warning',
    messages.ERROR: 'danger'  # For bootstrap class names
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'rjbdevel@gmail.com'
EMAIL_HOST_PASSWORD = 'QuinnRose81$gm'
EMAIL_PORT = 587

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
