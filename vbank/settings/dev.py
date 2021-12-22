from vbank.settings.base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c%_k2w*ydu03jxnx(-qx-5pz9g+5p=%e+_h-q$@0(c5kqr#5kd'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'vbank.db',
}

# Email Backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('assets')
STATICFILES_DIRS = [
    Path.cwd().joinpath(BASE_DIR).joinpath('vbank/assets'),
]


MEDIA_URL = '/media/'
MEDIA_ROOT = Path.cwd().joinpath(BASE_DIR).joinpath('media')
