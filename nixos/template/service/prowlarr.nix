## Config for prowlarr service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    LIDAR_PORT="8660";
  };
}
