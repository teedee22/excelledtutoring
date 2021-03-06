from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#o6^1!)+kx7solv!h$r@f#sqw@&-gs#6*f$($g)n09+1ss18+n'


INSTALLED_APPS = INSTALLED_APPS + [
    'debug_toolbar',
]

MIDDLEWARE = MIDDLEWARE + [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

INTERNAL_IPS = ("127.0.0.1", "172.17.0.1")
# Recaptcha Settings
RECAPTCHA_PUBLIC_KEY = '6LcBX7gUAAAAAHnHeDeX8CQ_KUNgFaFvBszhzNju'
RECAPTCHA_PRIVATE_KEY = '6LcBX7gUAAAAALEjWCR-GW1DLDPLzOVXIA6l01Ei'
NOCAPTCHA = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
try:
    from .local import *
except ImportError:
    pass
