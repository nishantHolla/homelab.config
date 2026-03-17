# Adguard service

## Installation

- Create `.env` file with the following values
```bash
# Port number for the main Adguard dashboard
PORT=

# Port number for the admin dashboard
ADMIN_PORT=

# Time zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
TZ=
```

- Visit `http://<homelab-ip>:<ADMIN_PORT>` after `docker compose up` to create admin account
