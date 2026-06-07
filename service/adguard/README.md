# Adguard service

## Installation

- Run `homelab service up adguard`

- Visit `http://<homelab-ip>:<ADGUARD_ADMIN_PORT>` to create the admin account

- Create a new `DNS rewrite` under `Filters` tab with the domain name as `*.homelab` and IP address of the homelab machine
