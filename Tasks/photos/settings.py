"""
Django settings for photos project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cj*ppho-qr32_d0xgd^fb$g-2=^#wzd!e+=g@^*06k7&zzp22j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'images',
    'covertimages',
    'session',
    'multiplesession',
    'orm',
    'rest_framework',
    'many',
    'encryption',
    'log',
    'valid',
    'currency',
    'oauth',
    'rest_framework.authtoken',
    'knox',
    'date',
    'birth',
    'DOB',
    'qrrcode',
    'barcode',
    'BMI',
    'timezone',
    'forget',
    'currenttime',
    'decimalfield',
    'words',

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

ROOT_URLCONF = 'photos.urls'

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

WSGI_APPLICATION = 'photos.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'project1',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

# PASSWORD_HASHERS = [
#   'django.contrib.auth.hashers.PBKDF2PasswordHasher',
#   'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
#   'django.contrib.auth.hashers.Argon2PasswordHasher',
#   'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
#   'django.contrib.auth.hashers.BCryptPasswordHasher',
#   'django.contrib.auth.hashers.SHA1PasswordHasher',
#   'django.contrib.auth.hashers.MD5PasswordHasher',
#   'django.contrib.auth.hashers.UnsaltedSHA1PasswordHasher',
#   'django.contrib.auth.hashers.UnsaltedMD5PasswordHasher',
#   'django.contrib.auth.hashers.CryptPasswordHasher',
# ]

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
SESSION_COOKIE_AGE = 20
MEDIA_URL = '/media/'
MEDIA_ROOT = '/home/madhu/PycharmProjects/pythonProject1/photos/images/images'
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {

            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/home/madhu/PycharmProjects/pythonProject1/photos/valid.demo.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}