## Config for kavita service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    KAVITA_PORT="8640";
  };
}
