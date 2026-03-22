# Immich service

## Installation

- Create `.env` file with the following values
```bash
# Version of immich to use (can be v2)
IMMICH_VERSION=

# Set to some long random string
DB_PASSWORD=

# Database username (can be postgres)
DB_USERNAME=

# Database name (can be immich)
DB_DATABASE_NAME=
```

- Run `docker compose up`

- Visit `http://<homelab-ip>:<IMMICH_PORT>` to create the admin account
