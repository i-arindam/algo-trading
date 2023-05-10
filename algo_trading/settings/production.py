import environ
import os

from algo_trading.settings.common import *

env = environ.Env()

# @TODO: change how env will be read in production
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['algo-trading-dev.ap-south-1.elasticbeanstalk.com', '172.31.11.81']

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

DATABASES = {
    'default': env('DATABASE_URL'),
}