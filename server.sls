{%- if pillar.sentry.server.enabled %}

include:
- python

sentry_packages:
  pkg.installed:
  - names:
    - python-setuptools
    - python-memcache
    - python-psycopg2
    - python-imaging
    - python-docutils
    - python-simplejson
    - build-essential
    - gettext
  - require:
    - pkg: python_packages

/srv/sentry:
  virtualenv.manage:
  - system_site_packages: True
  - requirements: salt://sentry/conf/requirements.txt
  - require:
    - pkg: sentry_packages

sentry_user:
  user.present:
  - name: sentry
  - system: True
  - home: /srv/sentry
  - require:
    - virtualenv: /srv/sentry

sentry_writable_dirs:
  file.directory:
  - mode: 755
  - user: sentry
  - makedirs: True
  - names:
    - /srv/sentry
    - /srv/sentry/logs
    - /srv/sentry/run

/etc/sentry.conf.py:
  file:
  - managed
  - source: salt://sentry/conf/sentry.conf.py
  - mode: 644
  - template: jinja
  - require:
    - file: /srv/sentry/logs

{%- endif %}