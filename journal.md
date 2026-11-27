# System journal

## Setup

- Connect to wifi

- Clone homelab repository
```bash
sudo apt install git
git clone https://github.com/nishantHolla/homelab.config Homelab
cd Homelab/cli
```

- Setup Sops
```bash
scp -r {Sops-dir} {Homelab-user}@{Homelab-ip-address}:~/Sops
```

- Setup tailscale
```bash
sudo tailscale up
# Update the DNS ip address to point to the homelab in the tailscale admin page
```

- Setup GoDaddy
  - Create following records
  ```txt
  Type: CNAME
  Name: *.homelab
  Value: homelab.nishantholla.com

  Type: A
  Name: homelab
  Value: {Homelab machine's IP address from tailscale}
  ```
  - Create API Key
    - Visit [https://developer.godaddy.com/keys](https://developer.godaddy.com/keys)
    and create a new api key
    - Note down the `Key` as `GODADDY_KEY` and `Secret` as `GO_DADDY_SECRET`
    - Set up new credentials in `nginx` dashboard page
