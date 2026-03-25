## Environment variables for ports of services
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    ## Core services

    NPM_PORT="81";
    ADGUARD_PORT="8000";
    ADGUARD_ADMIN_PORT="8001";
    UPTIME_KUMA_PORT="8020";

    ## Storage and Cloud

    IMMICH_PORT="8200";
    NAVIDROME_PORT="8220";
    JELLYFIN_TCP_PORT="8240";
    JELLYFIN_UDP_PORT="8241";
    NEXTCLOUD_PORT="8260";
    COLLABORA_PORT="8261";

    ## Tools and Utilities

    STIRLING_PORT="8420";
  };
}
