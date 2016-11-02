# -*- coding: utf-8 -*-
from settings import *

DEBUG = True

INTERNAL_IPS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/media/ramdisk/lettuce.db'
    }
}
INSTALLED_APPS += (
    'lettuce.django',
    'nose',
    'acceptance_tests'
)

LETTUCE_APPS = (
    'acceptance_tests',
)
