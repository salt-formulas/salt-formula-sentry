python:
  environment:
    enabled: true
    module:
      development: true
sentry:
  server:
    enabled: true
    workers: 3
    secret_key: rfui34bt34bierbrebsbfhvbfdsv
    url: http://another.domain.cz
    bind:
      name: sentry.domain.com
      address: 0.0.0.0
      port: 8080
    cache:
      engine: 'redis'
      host: '127.0.0.1'
    database:
      engine: 'postgresql'
      host: '127.0.0.1'
      name: 'sentry'
      password: 'pwd'
      user: 'sentry'
    mail:
      host: domain.com
      password: pass
      user: robot@domain.com
