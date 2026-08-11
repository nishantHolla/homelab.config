## Config for convertx service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    CONVERTX_PORT="8400";
    CONVERTX_AUTO_DELETE_EVERY_N_HOURS="24";
    CONVERTX_HTTP_ALLOWED="true";
    CONVERTX_ALLOW_UNAUTHENTICATED="false";
    CONVERTX_ACCOUNT_REGISTRATION="true";
  };
}
