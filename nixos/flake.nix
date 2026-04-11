{
  inputs = {
    # This is pointing to an unstable release.
    # If you prefer a stable release instead, you can this to the latest number shown here: https://nixos.org/download
    # i.e. nixos-24.11
    # Use `nix flake update` to update the flake to the latest revision of the chosen release channel.
    nixpkgs.url = "github:nixos/nixpkgs?ref=nixos-unstable";
  };

  outputs = inputs@{ self, nixpkgs }: {

    nixosConfigurations.template = nixpkgs.lib.nixosSystem { ## --START--
      modules = [
        ./template/config.nix
        ./template/packages.nix
        ./template/hardware.nix

        ./template/service/adguard.nix
        ./template/service/convertx.nix
        ./template/service/immich.nix
        ./template/service/jellyfin.nix
        ./template/service/lidarr.nix
        ./template/service/navidrome.nix
        ./template/service/nextcloud.nix
        ./template/service/nginx_proxy_manager.nix
        ./template/service/prowlarr.nix
        ./template/service/radarr.nix
        ./template/service/sonarr.nix
        ./template/service/stirling.nix
        ./template/service/uptime_kuma.nix
      ];
    }; ## --END--

  };
}
