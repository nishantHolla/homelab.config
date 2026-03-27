## Environment variables for ports of services
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    ## Core services

    UPTIME_KUMA_PORT="8020";

    ## Tools and Utilities

    STIRLING_PORT="8420";
  };
}
