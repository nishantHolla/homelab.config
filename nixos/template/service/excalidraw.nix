## Config for excalidraw service
{ config, lib, pkgs, ...}:

{
  environment.variables = {
    EXCALIDRAW_PORT="8440";
  };
}
