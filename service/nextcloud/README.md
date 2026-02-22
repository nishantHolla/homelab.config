# Nextclound service

## Installation

- Create `.env` file with the following values
```bash
# Time zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
TZ=

# MySQL host name (can be db)
MYSQL_HOST=

# MySQL database name (can be nextcloud)
MYSQL_DATABASE=

# MySQL username (can be nextcloud)
MYSQL_USER=

# Set to some long random string
MYSQL_PASSWORD=

# Set to some long random string
MYSQL_ROOT_PASSWORD=

# Redis host name (can be redis)
REDIS_HOST=

# List of domains that can be trusted to access nextcloud
NEXTCLOUD_TRUSTED_DOMAINS=
```

- Visit `http://<homelab-ip:2500` after `docker compose up` to create admin account
