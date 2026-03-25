## Config for adguard service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    ADGUARD_PORT="8000";
    ADGUARD_ADMIN_PORT="8001";
  };
}
