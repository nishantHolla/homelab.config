## Config for radarr service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    RADARR_PORT="8600";
  };
}
