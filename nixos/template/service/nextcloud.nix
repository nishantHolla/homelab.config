## Config for nextcloud service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    NEXTCLOUD_PORT="8260";
    COLLABORA_PORT="8261";
    NEXTCLOUD_MYSQL_HOST="db";
    NEXTCLOUD_MYSQL_DATABASE="nextcloud";
    NEXTCLOUD_MYSQL_USER="nextcloud";
    NEXTCLOUD_REDIS_HOST="redis";
  };
}
