## Config for nginx proxy manager service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    NPM_PORT="81";
  };
}
