# Jellyfin service

- Create `.env` file with the following values
```bash
# User ID (usually 1000)
PUID=

# Group ID (usually 100)
PGID=
```

- Run `docker compose up`

- Visit `http://<homelab-ip:<JELLYFIN_PORT>` to create the admin account
