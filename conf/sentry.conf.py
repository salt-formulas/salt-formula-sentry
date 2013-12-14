import os.path

from sentry.conf.server import *

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # We suggest PostgreSQL for optimal performance
        'NAME': '{{ pillar.sentry.server.database.name }}',
        'USER': '{{ pillar.sentry.server.database.user }}',
        'PASSWORD': '{{ pillar.sentry.server.database.password }}',
        'HOST': '{{ pillar.sentry.server.database.host }}',
        'PORT': '5432',
    }
}

# If you're expecting any kind of real traffic on Sentry, we highly recommend configuring
# the CACHES and Redis settings

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': ['127.0.0.1:11211'],
    }
}

# Buffers (combined with queueing) act as an intermediate layer between the database and
# the storage API. They will greatly improve efficiency on large numbers of the same events
# being sent to the API in a short amount of time.

SENTRY_USE_QUEUE = False

#BROKER_URL = 'redis://localhost:6379'

# You'll need to install the required dependencies for Redis buffers:
#   pip install redis hiredis nydus

#SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
#SENTRY_REDIS_OPTIONS = {
#    'hosts': {
#        0: {
#            'host': '127.0.0.1',
#            'port': 6379,
#        }
#    }
#}

SENTRY_KEY = '{{ pillar.sentry.server.secret_key }}'

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
SENTRY_URL_PREFIX = ''

SENTRY_WEB_HOST = '{{ pillar.sentry.server.bind.address }}'
SENTRY_WEB_PORT = {{ pillar.sentry.server.bind.port }}
SENTRY_WEB_OPTIONS = {
    'workers': 3,  # the number of gunicorn workers
    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = '{{ pillar.sentry.server.mail.host }}'
EMAIL_HOST_PASSWORD = '{{ pillar.sentry.server.mail.password }}'
EMAIL_HOST_USER = '{{ pillar.sentry.server.mail.user }}'
EMAIL_PORT = 25
EMAIL_USE_TLS = False

# http://twitter.com/apps/new
# It's important that input a callback URL, even if its useless. We have no idea why, consult Twitter.
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
