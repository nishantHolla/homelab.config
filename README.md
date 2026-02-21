# Homelab

This repository contains the configuration files and Docker Compose setups for my self-hosted homelab environment.
The goal of this homelab is to run core services locally with proper DNS, reverse proxy, and containerized deployments.

## Services

| Service                                               | Description                                          | Dashboard Port |
| ----------------------------------------------------- | ---------------------------------------------------- | -------------- |
| [Immich](./service/immich/)                           | Self-hosted photo and video backup solution          | `2000`         |
| [Nextcloud](./service/nextcloud/)                     | Self-hosted cloud storage and collaboration platform | `2500`         |
| [ConvertX](./service/convertx/)                       | Self-hosted file conversion service                  | `3000`         |
| [AdGuard Home](./service/adguard/)                    | Network-wide DNS and ad blocking                     | `3500`         |
| [Nginx Proxy Manager](./service/nginx_proxy_manager/) | Reverse proxy with web-based management UI           | `81`           |


## Hardware

Currently it is running on a Raspberry Pi 4B (4GB RAM) inside a tailscale network.
