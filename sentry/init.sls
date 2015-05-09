
include:
{%- if pillar.sentry.server is defined %}
- sentry.server
{%- endif %}
