
{%- if pillar.sentry is defined %}
include:
{%- if pillar.sentry.server is defined %}
- sentry.server
{%- endif %}
{%- endif %}
