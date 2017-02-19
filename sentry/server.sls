{%- from "sentry/map.jinja" import server with context %}
{%- if server.enabled %}

include:
- python

sentry_packages:
  pkg.installed:
  - names: {{ server.pkgs }}
  - require:
    - pkg: python_packages

sentry_env:
  virtualenv.manage:
  - name: {{ server.dir.base }}/env
  - system_site_packages: True
  - requirements: salt://sentry/files/requirements.txt
  - require:
    - pkg: sentry_packages

sentry_user:
  user.present:
  - name: sentry
  - system: True
  - home: {{ server.dir.base }}
  - require:
    - virtualenv: sentry_env

sentry_dirs:
  file.directory:
  - mode: 755
  - user: sentry
  - makedirs: True
  - names:
    - {{ server.dir.base }}
    - {{ server.dir.log }}
    - {{ server.dir.config }}
    - {{ server.dir.base }}/run
  - require:
    - user: sentry_user

{{ server.dir.config }}/sentry.conf.py:
  file.managed:
  - source: salt://sentry/files/sentry.conf.py
  - mode: 644
  - template: jinja
  - require:
    - file: sentry_dirs
  - require_in:
    - cmd: sentry_schema_upgrade

{{ server.dir.config }}/config.yml:
  file.managed:
  - source: salt://sentry/files/config.yml
  - mode: 644
  - template: jinja
  - require:
    - file: sentry_dirs
  - require_in:
    - cmd: sentry_schema_upgrade

sentry_schema_upgrade:
  cmd.run:
  - name: source {{ server.dir.base }}/env/bin/activate; SENTRY_CONF=/etc/sentry sentry upgrade

{%- endif %}
