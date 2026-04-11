## Config for lidar service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    LIDAR_PORT="8640";
  };
}
