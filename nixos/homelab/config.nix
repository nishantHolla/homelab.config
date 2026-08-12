# Edit this configuration file to define what should be installed on
# your system. Help is available in the configuration.nix(5) man page, on
# https://search.nixos.org/options and in the NixOS manual (`nixos-help`).

{ config, lib, pkgs, ... }:

{
  # Boot Loader
  boot.kernelPackages = pkgs.linuxPackages_rpi4;
  boot.kernelParams = [
    "8250.nr_uarts=1"
    "console=tyAMA0,115200"
    "console=tty1"
    "cma=128M"
  ];

  boot.loader.raspberryPi.enaable = true;
  boot.loader.raspberryPi.version = 4;
  boot.loader.grub.enable = false;
  boot.loader.generic-extlinux-compatible.enable = true;

  # ZFS
  boot.supportedFilesystems = [ "zfs" ];
  boot.zfs.extraPools = [ "zpool" ];
  boot.zfs.devNodes = "/dev/disk/by-partuuid";

  services.zfs.autoScrub.enable = true;
  services.zfs.trim.enable = true;

  # Networking
  networking.hostId = "";
  networking.hostName = "homelab";
  networking.networkmanager.enable = true;

  # Time Zone
  time.timeZone = "Asia/Kolkata";

  # Internationalisation Properties
  i18n.defaultLocale = "en_US.UTF-8";

  # X11
  services.xserver.enable = false;

  # Users
  users.users.admin = {
    isNormalUser = true;
    extraGroups = [ "wheel" "docker" ];
    packages = with pkgs; [ ];
    shell = pkgs.zsh;
  };

  # Zsh
  programs.zsh.enable = true;
  programs.zsh.shellInit = ''
    export PATH="$PATH:$HOMELAB_DIR/bin"
    export SOPS_AGE_KEY_FILE="$HOMELAB_SOPS_DIR/age/keys.txt"
  '';


  # Packages
  environment.systemPackages = with pkgs; [
    vim
    wget
    curl
    git
  ];

  # Variables
  environment.variables = {
    HOMELAB_DIR="$HOME/Homelab";
    HOMELAB_DATA_DIR="$HOME/Data";
    HOMELAB_SOPS_DIR="$HOME/Sops";
    HOMELAB_UID="1000";
    HOMELAB_GID="100";
    TZ="Asia/Kolkata";
  };

  # SUID Wrappers
  programs.mtr.enable = true;
  programs.gnupg.agent = {
    enable = true;
    enableSSHSupport = true;
  };

  # Services
  services.openssh.enable = true;

  # Docker
  virtualisation.docker.enable = true;
  virtualisation.docker.enableOnBoot = true;
  virtualisation.docker.autoPrune.enable = true;
  virtualisation.docker.autoPrune.dates = "weekly";

  # Tailscale
  services.tailscale.enable = true;

  # Firewall
  networking.firewall.enable = true;
  networking.firewall.trustedInterfaces = [ "tailscale0" ];
  networking.firewall.allowedTCPPorts = [ ];
  networking.firewall.allowedUDPPorts = [ ];

  # Garbage collection
  nix.gc.automatic = true;
  nix.gc.dates = "weekly";
  nix.gc.options = "--delete-older-than 7d";

  # Other settings
  system.stateVersion = "25.11";
  nix.settings.experimental-features = [ "nix-command" "flakes" ];
}
