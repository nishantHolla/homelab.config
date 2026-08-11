# Backup service using rustic
{ pkgs, ...}:

{
  environment.systemPackages = with pkgs; [
    restic
  ];

  users.users.backups = {
    isSystemUser = true;
    group = "restic-backup";
    home = "/var/backups/restic";
    createHome = true;
    shell = pkgs.bash;
    openssh.authorizedKeys.keys = [
      "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAILbZvfxuLPoct789FDFEXZ5HQEoNitV9AS0JXwIEUGb3 backups@nixosPavilion"
    ];
  };
  users.groups.restic-backup = {};
}
