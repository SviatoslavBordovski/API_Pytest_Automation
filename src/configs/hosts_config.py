API_HOSTS = {
    "test": "http://localhost:10004/wp-json/wc/v3/",
    "dev": "",
    "prod": ""
}
WOO_API_HOSTS = {
    "test": "http://localhost:10004/",
    "dev": "",
    "prod": ""
}

DB_HOST = {
    'machine1': {
              "test": {"host": "localhost",
                       "database": "local",
                       "table_prefix": "wp_",
                       "USER": "root",
                       "PASSWORD": "your_own_db_password",
                       # "socket": "/home/sviatoslav/.config/Local/run/WvJY8UqdR/mysql/mysqld.sock",
                       "port": 10005
                       },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'docker': {
              "test": {
                  "host": "host.docker.internal",
                  "database": "wp398",
                  "table_prefix": "wp2p_",
                  "socket": None,
                  "port": 3306
              },
              "dev": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
              "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
            },
    'machine2': {
        "test": {"host": "localhost",
                 "database": "local",
                 "table_prefix": "wp_",
                 "socket": "/Users/akinfu/Library/Application Support/Local/run/d84nqkpSm/mysql/mysqld.sock",
                 "port": 3306
                 },
        "dev": {
                  "host": "host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
        "prod": {
                  "host":"host.docker.internal",
                  "database": "local",
                  "table_prefix": "wp_",
                  "socket": None,
                  "port": 3306
              },
    }
}
