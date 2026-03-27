## Config for jellyfin service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    JELLYFIN_TCP_PORT="8240";
    JELLYFIN_UDP_PORT="8241";
  };
}
