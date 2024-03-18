from .base import *

DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': 'djpro',
    #     'USER': 'postgres',
    #     'PASSWORD': 'Chimango',
    #     'HOST': '127.0.0.1',
    #     'PORT': '5432',
    # }

    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'djpro',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR.joinpath('static')]

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.joinpath('media')
