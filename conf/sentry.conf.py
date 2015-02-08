{% set sentry = pillar.sentry.server %}
import os.path

from sentry.conf.server import *

CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # We suggest PostgreSQL for optimal performance
        'NAME': '{{ sentry.database.name }}',
        'USER': '{{ sentry.database.user }}',
        'PASSWORD': '{{ sentry.database.password }}',
        'HOST': '{{ sentry.database.host }}',
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

CELERY_ALWAYS_EAGER = False

SENTRY_KEY = '{{ sentry.secret_key }}'

# You should configure the absolute URI to Sentry. It will attempt to guess it if you don't
# but proxies may interfere with this.
{%- if sentry.bind.name is defined %}
SENTRY_URL_PREFIX = 'http://{{ sentry.bind.name }}'
{%- else %}
{%- if pillar.nginx.proxy is defined %}
SENTRY_URL_PREFIX = 'http://{{ sentry.bind.name }}'
{%- else %}
SENTRY_URL_PREFIX = 'http://{{ sentry.bind.url }}:{{ sentry.bind.port }}'
{%- endif %}
{%- endif %}

ALLOWED_HOSTS = [
    '*',
]

SENTRY_REMOTE_TIMEOUT = 10

SENTRY_REMOTE_URL = 'http://{{ sentry.bind.name }}/sentry/store/'

SENTRY_WEB_HOST = '{{ sentry.bind.address }}'
SENTRY_WEB_PORT = {{ sentry.bind.port }}
SENTRY_WEB_OPTIONS = {
    'workers': {{ sentry.get('workers', '3') }},  # the number of gunicorn workers
#    'secure_scheme_headers': {'X-FORWARDED-PROTO': 'https'},  # detect HTTPS mode from X-Forwarded-Proto header
}

# Mail server configuration

# For more information check Django's documentation:
#  https://docs.djangoproject.com/en/1.3/topics/email/?from=olddocs#e-mail-backends

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

{%- if sentry.mail.get('encryption', 'none') == 'tls' %}
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
{%- endif %}
{%- if sentry.mail.get('encryption', 'none') == 'ssl' %}
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
{%- endif %}
EMAIL_HOST = "{{ sentry.mail.get('host', 'localhost') }}"
EMAIL_HOST_USER = "{{ sentry.mail.user }}"
EMAIL_HOST_PASSWORD = "{{ sentry.mail.password }}"
EMAIL_PORT = {{ sentry.mail.get('port', '25') }}


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
