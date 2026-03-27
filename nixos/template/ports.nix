## Environment variables for ports of services
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    ## Core services

    NPM_PORT="81";
    UPTIME_KUMA_PORT="8020";

    ## Storage and Cloud

    NAVIDROME_PORT="8220";
    NEXTCLOUD_PORT="8260";
    COLLABORA_PORT="8261";

    ## Tools and Utilities

    STIRLING_PORT="8420";
  };
}
