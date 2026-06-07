# System journal

## Setup

- Connect to wifi

- Enter root
```bash
sudo su
```

- Setup partitions
  - `BOOT`: 1GB FAT 32
  - `SWAP`: 8GB Linux Swap
  - `DISK`: nGB Linux Filesystem
```bash
lsblk
fdisk /dev/{disk-name}
```

- Setup variables for disy by partuuid
```bash
blkid
BOOT=/dev/disk/by-partuuid/{id-of-BOOT-partition}
SWAP=/dev/disk/by-partuuid/{id-of-SWAP-partition}
DISK=/dev/disk/by-partuuid/{id-of-DISK-partition}
```

- Setup zfs on `DISK` partition
```bash
zpool create \
  -O encryption=on \
  -O keyformat=passphrase \
  -O keylocation=prompt \
  -O compression=zstd \
  -O mountpoint=none \
  -O xattr=sa \
  -O acltype=posixacl \
  -o ashift=12 \
  zpool $DISK

zfs create -o mountpoint=legacy zpool/root
zfs create -o mountpoint=legacy zpool/nix
zfs create -o mountpoint=legacy zpool/var
zfs create -o mountpoint=legacy zpool/home

mkdir -p /mnt
mount -t zfs zpool/root /mnt

mkdir -p /mnt /mnt/nix /mnt/var /mnt/home
mount -t zfs zpool/nix /mnt/nix
mount -t zfs zpool/var /mnt/var
mount -t zfs zpool/home /mnt/home
```

- Format partitions
```bash
mkfs.fat -F 32 $BOOT
mkswap $SWAP
```

- Mount partitions
```bash
mkdir /mnt/boot
mount $BOOT /mnt/boot
swapon $SWAP
```

- Clone `Homelab` repository
```bash
cd /mnt
git clone https://github.com/nishantHolla/homelab.config Homelab
cd Homelab/cli
```

- Setup nixos using cli
```bash
nix --experimental-features "nix-command flakes" develop
python homelab.py nixos setup
```

- Shutdown and remove the install medium

- Power on the system and login with the user account

- Bring homelab to home directory
```bash
sudo mv /Homelab .
sudo chown -R $(whoami) Homelab
cd Homelab/cli
```

- Setup Sops
```bash
scp -r {Sops-dir} {Homelab-user}@{Homelab-ip-address}:~/Sops
```

- Setup tailscale
```bash
sudo tailscale login
# Visit the link it gives and approve the divice in tailscale admin page
sudo tailscale up
# Update the DNS ip address to point to the homelab in the tailscale admin page
```

- Setup GoDaddy
  - Create following records
  ```txt
  Type: CNAME
  Name: *.homelab
  Value: homelab.nishantholla.com

  Type: A
  Name: homelab
  Value: {Homelab machine's IP address from tailscale}
  ```
  - Create API Key
    - Visit [https://developer.godaddy.com/keys](https://developer.godaddy.com/keys)
    and create a new api key
    - Note down the `Key` as `GODADDY_KEY` and `Secret` as `GO_DADDY_SECRET`
