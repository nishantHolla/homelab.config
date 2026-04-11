# Homelab

This repository contains the configuration files and Docker Compose setups for my self-hosted homelab environment.
The goal of this homelab is to run core services locally with proper DNS, reverse proxy, and containerized deployments.

## Services

### Core services (8000 to 8200)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Nginx Proxy Manager](./service/nginx_proxy_manager/) | Reverse proxy with web-based management UI           | `81`             | proxy.homelab     |
| [AdGuard Home](./service/adguard/)                    | Network-wide DNS and ad blocking                     | `8000`, `8001`   | dns.homelab       |
| [Uptime Kuma](./service/uptime_kuma/)                 | A self-hosted monitoring tool                        | `8020`           | uptime.homelab    |

### Storage and Cloud (8200 to 8400)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [Immich](./service/immich/)                           | Self-hosted photo and video backup solution          | `8200`           | photos.homelab    |
| [Navidrome](./service/navidrome/)                     | Self-hosted music streaming solution                 | `8220`           | music.homelab     |
| [Jellyfin](./service/jellyfin/)                       | Self-hosted media solution                           | `8240`, `8241`   | shows.homelab     |
| [Nextcloud](./service/nextcloud/)                     | Self-hosted cloud storage and collaboration platform | `8260`, `8261`   | cloud.homelab     |

### Tools and Utilities (8400 to 8600)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain        |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | ----------------- |
| [ConvertX](./service/convertx/)                       | Self-hosted file conversion service                  | `8400`           | convert.homelab   |
| [Stirling](./service/stirling/)                       | Self-hosted PDF toolkit                              | `8420`           | pdf.homelab       |

### Automation (8600 to 8800)

| Service                                               | Description                                          | Dashboard Port   | Sub Domain           |
| ----------------------------------------------------- | ---------------------------------------------------- | ---------------- | -------------------- |
| [Radarr](./service/radarr/)                           | Automate movie downloading                           | `8600`           | movie.media.homelab  |
| [Sonarr](./service/sonarr/)                           | Automate tv show downloading                         | `8620`           | tv.media.homelab     |
| [Lidarr](./service/lidarr/)                           | Automate music downloading                           | `8640`           | music.media.homelab  |
| [Prowlarr](./service/prowlarr/)                       | Indexer for the arr stack                            | `8660`           | index.media.homelab  |


## Hardware

Currently it is running on a Raspberry Pi 4B (4GB RAM) inside a tailscale network.
