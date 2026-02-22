# Convertx service

## Installation

- Create `.env` file with the following values
```bash
# Time zone (https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
TZ=

# Delete converted files after N hours
AUTO_DELETE_EVERY_N_HOURS=

# Can be set to true if running inside tailscale
HTTP_ALLOWED=

# Allow users to convert files without creating an account
ALLOW_UNAUTHENTICATED=

# Allow new registration of account after admin account is created
ACCOUNT_REGISTRATION=

# Generate a long random string
JWT_SECRET=
```

- Visit `http://<homelab-ip>:3000` after `docker compose up` to create admin account
