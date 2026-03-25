## Config for immich service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    IMMICH_PORT="8200";
    IMMICH_VERSION="v2";
    IMMICH_DB_USERNAME="postgres";
    IMMICH_DB_DATABASE_NAME="immich";
  };
}
