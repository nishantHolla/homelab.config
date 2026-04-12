## Config for lidar service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    LIDARR_PORT="8640";
  };
}
