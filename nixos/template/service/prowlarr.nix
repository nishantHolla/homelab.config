## Config for prowlarr service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    PROWLARR_PORT="8660";
  };
}
