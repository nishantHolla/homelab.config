# Syncthing service

## Installation

- Copy the directories from the laptop into the sync root on the homelab
```bash
ssh {Homelab-user}@{Homelab-ip-address} 'mkdir -p ~/Data/library/sync'
rsync -avP \
  --exclude='.venv/' \
  --exclude='venv/' \
  --exclude='node_modules/' \
  --exclude='__pycache__/' \
  --exclude='target/' \
  --exclude='.cache/' \
  {Dir-1} {Dir-2} ... {Homelab-user}@{Homelab-ip-address}:~/Data/library/sync/
# Add -n to do a dry run first
```

- Run `homelab service up syncthing`

- Visit `http://<homelab-ip>:<SYNCTHING_PORT>` and set a GUI username and password
  (Settings > GUI)

- Install syncthing on the laptop and desktop
  - Fedora: `sudo dnf install syncthing && systemctl --user enable --now syncthing`
  - Windows: Install [SyncTrayzor](https://github.com/GermanCoding/SyncTrayzor) or
    `winget install Syncthing.Syncthing`

- Set the default ignore patterns on each device (homelab, laptop and desktop)
  - Open the dashboard and go to Actions > Advanced > Default Ignores
  - Paste the contents of [stignore](./stignore) and save
  - Do this before adding or accepting any folders, so every folder gets a
    `.stignore` with these patterns before its first scan

- Pair the devices
  - On the homelab dashboard, add the laptop and desktop as remote devices using their device IDs
  - Set the homelab's address on the laptop and desktop to
    `tcp://<homelab-tailscale-ip>:<SYNCTHING_SYNC_PORT>`

- Share the folders
  - On the homelab dashboard, add a folder for each directory, with the path
    `/var/syncthing/data/<dir-name>`, and share it with the laptop and desktop
  - Accept the share on the laptop and desktop and point it at the local copy of the directory

## Ignore patterns

- [stignore](./stignore) is the master list of ignore patterns
- `.stignore` is not synced between devices, each folder on each device has its own copy
- To change the patterns
  - Update [stignore](./stignore) and the Default Ignores on each device, for new folders
  - Edit the folder's ignore patterns (Folder > Edit > Ignore Patterns) on each device,
    for existing folders
