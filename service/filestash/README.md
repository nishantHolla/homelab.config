# Filestash service

Web file manager for the directories synced by [Syncthing](../syncthing/).

## Installation

- Make sure `FILESTASH_ROOT_DIR` in [env.yaml](./env.yaml) matches `SYNCTHING_ROOT_DIR` in
  [syncthing's env.yaml](../syncthing/env.yaml)

- Create the state directory so it is owned by the homelab user and not by root
```bash
mkdir -p ~/Data/apps/filestash/state
```

- Run `homelab service up filestash`

- Visit `http://<homelab-ip>:<FILESTASH_PORT>/admin` and set the admin password

- Enable the local storage backend
  - In the admin console, go to Storage
  - Enable `local` and disable every other backend you don't want
  - Under Authentication, pick how users log in (for example `passthrough` or `htpasswd`) and
    map it to the `local` backend with the path `/srv/sync`

- Visit `http://<homelab-ip>:<FILESTASH_PORT>` and log in to browse the synced directories

## Notes

- The sync directory is mounted read-write at `/srv/sync`, so files changed through Filestash are
  picked up by Syncthing and synced to the other devices
- The container runs as `HOMELAB_UID:HOMELAB_GID`, the same user as Syncthing, so files created
  through Filestash have the right owner
- To make Filestash read-only, add `:ro` to the sync volume in
  [docker-compose.yml](./docker-compose.yml)
