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

/srv/sentry:
  virtualenv.manage:
  - system_site_packages: True
  - requirements: salt://sentry/conf/requirements.txt
  - require:
    - pkg: sentry_packages

/etc/supervisor/conf.d/sentry-web.conf:
  file:
  - managed
  - source: salt://sentry/conf/sentry-web.conf
  - mode: 644
  - template: jinja
  - require:
    - pkg: sentry_packages

/etc/sentry.conf.py:
  file:
  - managed
  - source: salt://sentry/conf/sentry.conf.py
  - mode: 644
  - template: jinja
  - require:
    - pkg: sentry_packages
    - virtualenv: /srv/sentry


supervisor:
  service.running:
  - enable: True
  - watch:
    - file: /etc/supervisor/conf.d/sentry-web.conf

{%- endif %}
