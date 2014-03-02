
# Sentry

Sentry is a realtime event logging and aggregation platform. At its core it specializes in monitoring errors and extracting all the information needed to do a proper post-mortem without any of the hassle of the standard user feedback loop.

It’s important to note that Sentry should not be thought of as a log stream, but as an event aggregator. It fits somewhere in-between a simple metrics solution (such as Graphite) and a full-on log stream aggregator (like Logstash).

## Sample pillar

    sentry:
      server:
        enabled: true
        workers: 3
        secret_key: rfui34bt34bierbrebsbfhvbfdsv
        bind:
          name: sentry.domain.com
          address: 0.0.0.0
          port: 8080
        cache:
          engine: 'memcached'
          host: '127.0.0.1'
          prefix: 'CACHE_SENTRY'
        database:
          engine: 'mysql'
          host: '127.0.0.1'
          name: 'sentry'
          password: 'pwd'
          user: 'sentry'
        mail:
          host: domain.com
          password: pass
          user: robot@domain.com

## Sample pillar with proxy

    sentry:
      server:
        enabled: true
        workers: 3
        secret_key: rfui34bt34bierbrebsbfhvbfdsv
        bind:
          url: http://another.domain.cz
          name: sentry.domain.com
          address: 0.0.0.0
          port: 8080
        cache:
          engine: 'memcached'
          host: '127.0.0.1'
          prefix: 'CACHE_SENTRY'
        database:
          engine: 'mysql'
          host: '127.0.0.1'
          name: 'sentry'
          password: 'pwd'
          user: 'sentry'
        mail:
          host: domain.com
          password: pass
          user: robot@domain.com

## Read more

* https://github.com/getsentry/sentry
* http://sentry.readthedocs.org/en/latest/index.html
