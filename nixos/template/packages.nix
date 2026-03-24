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
    sops
    tmux
    wget
  ];
}

