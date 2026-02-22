# Edit this configuration file to define what should be installed on
# your system. Help is available in the configuration.nix(5) man page, on
# https://search.nixos.org/options and in the NixOS manual (`nixos-help`).

{ config, lib, pkgs, ... }:

{
  # Boot Loader
  boot.loader.grub.enable = true;
  boot.loader.grub.zfsSupport = true;
  boot.loader.grub.efiSupport = true;
  boot.loader.grub.efiInstallAsRemovable = true;
  boot.loader.grub.mirroredBoots = [
    { devices = [ "nodev" ]; path = "/boot"; }
  ];

  # ZFS
  boot.supportedFilesystems = [ "zfs" ];
  networking.hostId = "9b500f6c";
  services.zfs.autoScrub.enable = true;

  # Networking
  networking.hostName = "homelab";
  networking.networkmanager.enable = true;

  # Time Zone
  time.timeZone = "Asia/Kolkata";

  # Network Proxy
  # networking.proxy.default = "http://user:password@proxy:port/";
  # networking.proxy.noProxy = "127.0.0.1,localhost,internal.domain";

  # Internationalisation Properties
  i18n.defaultLocale = "en_US.UTF-8";

  # X11
  services.xserver.enable = false;

  # Users
  users.users.admin = {
    isNormalUser = true;
    extraGroups = [ "wheel" "docker" ];
    packages = with pkgs; [ ];
  };

  # Packages
  environment.systemPackages = with pkgs; [
    vim
    wget
    curl
    git
  ];

  # Variables
  environment.variables = {
    HOMELAB_CONFIG_DIR="$HOME/Homelab";
    HOMELAB_DATA_DIR="$HOME/Data";
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
  networking.firewall.allowedTCPPorts = [

  ];
  networking.firewall.allowedUDPPorts = [ ];

  # Garbage collection
  nix.gc.automatic = true;
  nix.gc.dates = "weekly";
  nix.gc.options = "--delete-older-than 7d";

  # Other settings
  system.stateVersion = "25.11";
  nix.settings.experimental-features = [ "nix-command" "flakes" ];

}
