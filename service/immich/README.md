# Immich service

## Installation

- Create `.env` file with the following values
```bash
# Time zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
TZ=

# Version of immich to use (can be v2)
IMMICH_VERSION=

# Set to some long random string
DB_PASSWORD=

# Database username (can be postgres)
DB_USERNAME=

# Database name (can be immich)
DB_DATABASE_NAME=
```

- Visit `http://<homelab-ip>:2000` after `docker compose up` to create admin account
