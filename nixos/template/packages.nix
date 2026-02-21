## System packages for homelab
{ config, lib, pkgs, ... }:

{
  # System packages
  environment.systemPackages = with pkgs; [
    curl
    gcc
    git
    neovim
    tmux
    wget
  ];
}

