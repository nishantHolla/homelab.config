# Homelab

This repository contains the configuration files and Docker Compose setups for my self-hosted homelab environment.
The goal of this homelab is to run core services locally with proper DNS, reverse proxy, and containerized deployments.

## Services

### Core services (8000 to 8200)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Nginx Proxy Manager](./service/nginx_proxy_manager/) | Reverse proxy with web-based management UI           | `81`             | proxy.homelab     |
| [Uptime Kuma](./service/uptime_kuma/)                 | A self-hosted monitoring tool                        | `8000`           | uptime.homelab    |
| [Vaultwarden](./service/vaultwarden/)                 | Password manager                                     | `8020`           | password.homelab  |

### Storage and Cloud (8200 to 8400)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Immich](./service/immich/)                           | Self-hosted photo and video backup solution          | `8200`           | photos.homelab    |
| [Nextcloud](./service/nextcloud/)                     | Self-hosted cloud storage and collaboration platform | `8220`, `8221`   | cloud.homelab     |

### Tools and Utilities (8400 to 8600)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [ConvertX](./service/convertx/)                       | Self-hosted file conversion service                  | `8400`           | convert.homelab   |
| [Stirling](./service/stirling/)                       | Self-hosted PDF toolkit                              | `8420`           | pdf.homelab       |

### Media (8600 to 8800)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Navidrome](./service/navidrome/)                     | Self-hosted music streaming solution                 | `8600`           | music.homelab     |
| [Jellyfin](./service/jellyfin/)                       | Self-hosted media solution                           | `8620`, `8621`   | tv.homelab        |
| [Kavita](./service/kavita/)                           | Self-hosted digital library                          | `8640`           | reader.homelab    |

## Hardware

Currently it is running on a Raspberry Pi 4B (4GB RAM) inside a tailscale network.
