## Config for sonarr service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    SONARR_PORT="8620";
  };
}
