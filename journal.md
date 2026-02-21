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
zpool create -O encryption=on -O keyformat=passphrase -O keylocation=prompt -O compression=zstd -O mountpoint=none -O xattr=sa -O acltype=posixacl -o ashift=12 zpool /dev/<nixos-partition>

zfs create zpool/root
zfs create zpool/nix
zfs create zpool/var
zfs create zpool/home

mkdir -p /mnt
mount -t zfs zpool/root /mnt -o zfsutil

mkdir /mnt/nix /mnt/var /mnt/home
mount -t zfs zpool/nix /mnt/nix -o zfsutil
mount -t zfs zpool/var /mnt/var -o zfsutil
mount -t zfs zpool/home /mnt/home -o zfsutil
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
