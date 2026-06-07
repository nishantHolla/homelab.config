# Nginx Proxy Manager service

## Installation

- Run `homelab service up nginx_proxy_manager`

- Visit `http://<homelab-ip>:<NPM_PORT>` to create the admin account

- Create a new SSL certificate with `Let's Encrypt via DNS`. Set Domain name as `*.homelab.nishantholla.com`
and DNS provider as `GoDaddy`, enter the `GODADDY_KEY` and `GODADDY_SECRET`

- Setup proxies for all services with the forwarding IP address as the IP address of the homelab
machine from the tailscale admin dashboard

