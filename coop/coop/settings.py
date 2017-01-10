"""
Django settings for coop project.

Generated by 'django-admin startproject' using Django 1.10.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os


import socket 

if socket.gethostname().startswith('james'):
    DJANGO_HOST='dev'
else:
    DJANGO_HOST='production'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z8opvv_h4s!t=m%@ip*reg@x9%_snhhy=229!gsi&6)4k0)qd='

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
if DJANGO_HOST=='dev':
    DEBUG = True

ALLOWED_HOSTS = ['galwayclimbing.pythonanywhere.com','jalibras.pythonanywhere.com','localhost','poincare.nuigalway.ie']


# Application definition

INSTALLED_APPS = [
    #'bootstrap_admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'rest_framework',
    'guide',
    'homepage',
    'members',
    'posts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'coop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR,'templates'),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'guide.context_processors.nav',
            ],
        },
    },
]


WSGI_APPLICATION = 'coop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/var/www/coop_static'
STATICFILES_DIRS=[ os.path.join(BASE_DIR,'static'), ]




MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(BASE_DIR,'media')



# custom User model

AUTH_USER_MODEL = 'members.User'


#login url

LOGIN_URL = "/members/auth/login/"

# login redirect URL
LOGIN_REDIRECT_URL='/'

# logout redirect URL
LOGOUT_REDIRECT_URL='/home/'

# email settings for gmail smtp 
EMAIL_HOST = "smtp.gmail.com"
EMAIL_HOST_USER = "jamescruickshank1971@gmail.com"
EMAIL_HOST_PASSWORD = "1m1o1y1n1e1"
EMAIL_PORT = 587
EMAIL_USE_TLS = True


# Rest Framework settings

REST_FRAMEWORK = {
        'DEFAULT_PERMISSION_CLASSES': [
            'rest_framework.permissions.IsAdminUser',
            ],
        'PAGE_SIZE': 10,
        'DEFAULT_FILTER_BACKENDS':(
            'django_filters.rest_framework.DjangoFilterBackend',
            'rest_framework.filters.SearchFilter',
            'rest_framework.filters.OrderingFilter',
            ),
        }
