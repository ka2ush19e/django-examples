# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function, unicode_literals
from os.path import abspath, dirname, join, normpath


########## PATH
# Config directory
CONFIG_ROOT = dirname(abspath(__file__))

# Project directory
PROJECT_ROOT = dirname(CONFIG_ROOT)

# Django directory
DJANGO_ROOT = dirname(PROJECT_ROOT)


########## APPLICATION
# https://docs.djangoproject.com/en/1.9/ref/settings/#installed-apps
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
    'compressor',
    'debug_toolbar',
)

PROJECT_APPS = (
    'core',
)

EXTENSION_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS + EXTENSION_APPS


########## MIDDLEWARE
# https://docs.djangoproject.com/en/1.9/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


########## DEBUG
# https://docs.djangoproject.com/en/1.9/ref/settings/#debug
DEBUG = True


########## SECRET KEY
# https://docs.djangoproject.com/en/1.9/ref/settings/#secret-key
SECRET_KEY = '$per=gqrn!jd6wa^_bb(xaedja5g&y(b0a(%wo@=v_h5(dgbij'


########## DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'localhost',
        'PORT': 5432,
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': '',
        'ATOMIC_REQUESTS': True,
    }
}


########## FIXTURE
# https://docs.djangoproject.com/en/1.9/ref/settings/#fixture-dirs
FIXTURE_DIRS = (
    normpath(join(PROJECT_ROOT, 'fixtures'))
)


########## PASSWORD VALIDATOR
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


########## INTERNATIONALIZATION
# https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-TIME_ZONE
TIME_ZONE = 'Asia/Tokyo'

# https://docs.djangoproject.com/en/1.9/ref/settings/#language-code
LANGUAGE_CODE = 'ja'

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-i18n
USE_I18N = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/1.9/ref/settings/#languages
from django.utils.translation import ugettext_lazy as _
LANGUAGES = [
    ('ja', _('Japanese'))
]

# https://docs.djangoproject.com/en/1.9/ref/settings/#locale-paths
LOCALE_PATHS = [
    normpath(join(PROJECT_ROOT, 'locale'))
]


########## TEMPLATE
# https://docs.djangoproject.com/en/1.9/ref/settings/#templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            normpath(join(PROJECT_ROOT, 'templates'))
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'debug': DEBUG,
        },
    },
]


########## MEDIA
# https://docs.djangoproject.com/en/1.9/ref/settings/#media-root
MEDIA_ROOT = normpath(join(PROJECT_ROOT, 'media'))

# https://docs.djangoproject.com/en/1.9/ref/settings/#media-url
MEDIA_URL = '/media/'


########## STATIC FILE
# https://docs.djangoproject.com/en/1.9/ref/settings/#static-root
STATIC_ROOT = normpath(join(PROJECT_ROOT, 'public'))

# https://docs.djangoproject.com/en/1.9/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.9/ref/settings/#staticfiles-dirs
STATICFILES_DIRS = (
    normpath(join(PROJECT_ROOT, 'static')),
)

# https://docs.djangoproject.com/en/1.9/ref/settings/#staticfiles-finders
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

# https://django-compressor.readthedocs.org/en/latest/settings/#django.conf.settings.COMPRESS_OUTPUT_DIR
COMPRESS_OUTPUT_DIR = 'compressed'


########## URL
# https://docs.djangoproject.com/en/1.9/ref/settings/#root-urlconf
ROOT_URLCONF = 'config.urls'


########## LOGIN / LOGOUT
# https://docs.djangoproject.com/en/1.9/ref/settings/#login-url
# LOGIN_URL = '/accounts/login/'

# https://docs.djangoproject.com/en/1.9/ref/settings/#login-redirect-url
# LOGIN_REDIRECT_URL = '/'

# https://docs.djangoproject.com/en/1.9/ref/settings/#logout-url
# LOGOUT_URL = '/accounts/logout/'


########## WSGI
# https://docs.djangoproject.com/en/1.9/ref/settings/#wsgi-application
WSGI_APPLICATION = 'config.wsgi.application'


########## USER MODEL
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-user-model
# AUTH_USER_MODEL = 'accounts.User'


########## LOGGING
# https://docs.djangoproject.com/en/1.9/ref/settings/#logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(asctime)s %(levelname)-8s %(name)-30s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': True,
        },
        'core': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'apps': {
            'handlers': ['console'],
            'level': 'INFO',
        },
    }
}
