# Homelab

This repository contains the configuration files and Docker Compose setups for my self-hosted homelab environment.
The goal of this homelab is to run core services locally with proper DNS, reverse proxy, and containerized deployments.

## Services

### Core services (8000 to 8200)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Nginx Proxy Manager](./service/nginx_proxy_manager/) | Reverse proxy with web-based management UI           | `81`             | npm.homelab       |
| [AdGuard Home](./service/adguard/)                    | Network-wide DNS and ad blocking                     | `8000`, `8001`   | adguard.homelab   |
| [Uptime Kuma](./service/uptime_kuma/)                 | A self-hosted monitoring tool                        | `8020`           | uptime.homelab    |

### Storage and Cloud (8200 to 8400)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Immich](./service/immich/)                           | Self-hosted photo and video backup solution          | `8200`           | immich.homelab    |
| [Jellyfin](./service/jellyfin/)                       | Self-hosted media solution                           | `8220`           | jellyfin.homelab  |
| [Nextcloud](./service/nextcloud/)                     | Self-hosted cloud storage and collaboration platform | `8240`, `8241`   | nextcloud.homelab |

## Tools and Utilities (8400 to 8600)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [ConvertX](./service/convertx/)                       | Self-hosted file conversion service                  | `8400`           | convert.homelab   |
| [Stirling](./service/stirling/)                       | Self-hosted PDF toolkit                              | `8420`           | pdf.homelab       |

## Hardware

Currently it is running on a Raspberry Pi 4B (4GB RAM) inside a tailscale network.
