{
  inputs = {
    # This is pointing to an unstable release.
    # If you prefer a stable release instead, you can this to the latest number shown here: https://nixos.org/download
    # i.e. nixos-24.11
    # Use `nix flake update` to update the flake to the latest revision of the chosen release channel.
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-26.05";
  };

  outputs = inputs@{ self, nixpkgs }: {

    nixosConfigurations.template = nixpkgs.lib.nixosSystem { ## --START--
      modules = [
        ./template/config.nix
        ./template/packages.nix
        ./template/hardware.nix

        ./template/service/convertx.nix
        ./template/service/excalidraw.nix
        ./template/service/immich.nix
        ./template/service/jellyfin.nix
        ./template/service/navidrome.nix
        ./template/service/nextcloud.nix
        ./template/service/nginx_proxy_manager.nix
        ./template/service/stirling.nix
        ./template/service/uptime_kuma.nix
        ./template/service/vaultwarden.nix
      ];
    }; ## --END--

    nixosConfigurations.homelab = nixpkgs.lib.nixosSystem { ## --START--
      modules = [
        ./homelab/config.nix
        ./homelab/packages.nix
        ./homelab/hardware.nix

        ./homelab/service/convertx.nix
        ./homelab/service/excalidraw.nix
        ./homelab/service/immich.nix
        ./homelab/service/jellyfin.nix
        ./homelab/service/navidrome.nix
        ./homelab/service/nextcloud.nix
        ./homelab/service/nginx_proxy_manager.nix
        ./homelab/service/stirling.nix
        ./homelab/service/uptime_kuma.nix
        ./homelab/service/vaultwarden.nix
      ];
    };

  };
}
