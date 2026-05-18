# System journal

## Setup

- Connect to wifi

- Enter root
```bash
sudo su
```

- Setup partitions
    - `BOOT`: 1GB FAT 32
    - `swap`: 8GB Linux Swap
    - `nixos`: nGB Linux Filesystem
```bash
lsblk
fdisk /dev/<disk-name>
```

- Setup zfs on `nixos` partition
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
  rpool /dev/<nixos-partition>

zfs create -o mountpoint=legacy rpool/root
zfs create -o mountpoint=legacy rpool/nix
zfs create -o mountpoint=legacy rpool/var
zfs create -o mountpoint=legacy rpool/home

mkdir -p /mnt
mount -t zfs rpool/root /mnt

mkdir /mnt/nix /mnt/var /mnt/home
mount -t zfs rpool/nix /mnt/nix
mount -t zfs rpool/var /mnt/var
mount -t zfs rpool/home /mnt/home
```

- Format partitions
```bash
mkfs.fat -F 32 -n boot /dev/<boot-parition>
mkswap /dev/<swap-parition>
```

- Mount partitions
```bash
mkdir /mnt/boot
mount /dev/<boot-parition> /mnt/boot
swapon /dev/<swap-parition>
```

- Clone `Homelab` repository
```bash
cd /mnt
git clone https://github.com/nishantHolla/homelab.config Homelab
cd Homelab/cli
```

- Setup nixos using the cli
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
cd System.cli
```
