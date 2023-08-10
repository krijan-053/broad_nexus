from .base import *
from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

SECRET_KEY = "django-insecure-^u^r&(3kcs%503^hf66=995ekb89d1k@znt(ugt!a)8^$szhfl"

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": 'nexusdb',
        "USER": 'postgres',
        "PASSWORD": 'apple',
        "HOST": '127.0.0.1',
        "PORT": '5432',

    }
}

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = '888146525cc09c'
EMAIL_HOST_PASSWORD = '0bbdcf2c259179'
EMAIL_PORT = '2525'
