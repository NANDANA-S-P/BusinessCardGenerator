"""
Django settings for CardGenerator project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
from pathlib import Path
from django.contrib.messages import constants as messages
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-zj^mz$oa-8+b9#9jz!iqx7)6@b11@yh$7w%k12^bp0zfm7zs_w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://*.railway.app','https://businesscardgenerator-production.up.railway.app']
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
 }
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'payment',
    'paypal.standard.ipn',
    'home',
    'cards',
    'user',
    'corsheaders',
    'django.contrib.sites',
     'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
     'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'CardGenerator.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'CardGenerator.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
DEFAULT_FROM_EMAIL = 'hbxmailer@hotbox99.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mail.hotbox99.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'hbxmailer@hotbox99.com'
EMAIL_HOST_PASSWORD = 'Email@IK257#$'
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
# import socket
# socket.getaddrinfo('mail.hotbox99.com', 8000)
# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/
AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",

    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
        'social_core.backends.google.GoogleOAuth2',  # Add this line
    'django.contrib.auth.backends.ModelBackend',
    
)
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

# Google OAuth settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '254016101743-8gg4i7nsm29sj7snfp88vsorjl8lqnv1.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = ['profile', 'email']

# Create a Google OAuth flow object
# google_auth_flow = Flow.from_client_secrets_file(
#     'path/to/client_secrets.json',
#     scopes=['profile', 'email'],
#     redirect_uri='http://localhost:8000/google/callback'
# )
# Create a Google OAuth flow object
google_auth_flow = Flow.from_client_config(
    {
        'web': {
            'client_id': SOCIAL_AUTH_GOOGLE_OAUTH2_KEY,
            'client_secret': SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET,
            'redirect_uris': ['http://127.0.0.1:8000/accounts/google/login/callback/'],
            'auth_uri': 'https://accounts.google.com/o/oauth2/auth',
            'token_uri': 'https://oauth2.googleapis.com/token',
            'auth_provider_x509_cert_url': 'https://www.googleapis.com/oauth2/v1/certs',
            'userinfo_endpoint': 'https://openidconnect.googleapis.com/v1/userinfo',
        }
    },
    scopes=['profile', 'email']
)

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 2

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = "user.User"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/
import os
STATIC_URL = '/static/'
STATICFILES_DIRS = [ os.path.join(BASE_DIR, 'static') ]
STATIC_ROOT =os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# PAYPAL_RECEIVER_EMAIL = 'udaysk963@gmail.com'

PAYPAL_TEST = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
