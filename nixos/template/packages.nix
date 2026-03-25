## System packages for homelab
{ config, lib, pkgs, ... }:

{
  # System packages
  environment.systemPackages = with pkgs; [
    age
    curl
    gcc
    git
    neovim
    python313
    python313Packages.pyyaml
    sops
    tmux
    wget
  ];
}

