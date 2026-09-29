#!/bin/sh

sudo apt update

sudo apt install -y \
    vim \
    wget \
    curl \
    git \
    zsh \
    age \
    gcc \
    neovim \
    tmux \
    python3 \
    python3-pip \
    python3-venv \
    python3-yaml \
    docker.io

sudo apt install sops


sudo systemctl enable --now docker

sudo adduser admin
sudo usermod -aG sudo,docker admin
sudo chsh -s /usr/bin/zsh admin

sudo -u admin python3 -m venv /home/admin/.venvs/homelab
sudo -u admin /home/admin/.venvs/homelab/bin/pip install \
    pyyaml docker typer
