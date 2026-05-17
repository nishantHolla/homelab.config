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
zpool create -f \
  -o ashift=12 \
  -O encryption=on \
  -O keyformat=passphrase \
  -O keylocation=prompt \
  -O compression=zstd \
  -O mountpoint=none \
  -O atime=off \
  zpool /dev/<nixos-partition>

zfs create -o mountpoint=legacy zpool/root
zfs create -o mountpoint=legacy zpool/nix
zfs create -o mountpoint=legacy zpool/var
zfs create -o mountpoint=legacy zpool/home

mkdir -p /mnt
mount -t zfs zpool/root /mnt

mkdir /mnt/nix /mnt/var /mnt/home
mount -t zfs zpool/nix /mnt/nix
mount -t zfs zpool/var /mnt/var
mount -t zfs zpool/home /mnt/home
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
