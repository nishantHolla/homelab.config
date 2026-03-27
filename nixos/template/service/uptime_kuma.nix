## Config for uptime kuma service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    UPTIME_KUMA_PORT="8020";
  };
}
