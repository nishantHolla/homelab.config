## Config for stirling service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    STIRLING_PORT="8420";
  };
}
