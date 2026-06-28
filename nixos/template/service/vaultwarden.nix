## Config for vaultwarden service
{ config, lib, pkgs, ... }:

{
  environment.variables = {
    VAULTWARDEN_PORT="8020";
  };
}
