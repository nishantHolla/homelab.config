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

- Setup variables for disk by partuuid
```bash
blkid
BOOT=/dev/disk/by-partuuid/<id-of-boot-partition>
SWAP=/dev/disk/by-partuuid/<id-of-swap-partition>
DISK=/dev/disk/by-partuuid/<id-of-nixos-partition>
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
