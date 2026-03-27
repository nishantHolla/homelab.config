## Config for navidrome service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    NAVIDROME_PORT="8220";
  };
}
