## System packages for homelab
{ config, lib, pkgs, ... }:

{
  # System packages
  environment.systemPackages = with pkgs; [
    curl
    gcc
    git
    neovim
    python313
    tmux
    wget
  ];
}

