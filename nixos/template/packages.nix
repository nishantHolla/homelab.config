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
    sops
    tmux
    wget

    (python313.withPackages (ps: with ps; [
      pyyaml
    ]))
  ];
}

