HOMELAB_USAGE = """
Usage: homelab <command> <sub-command> [...arguments]

command:

    nixos:

        Control system-level configuration.

    service:

        Control services of the homelab.
"""

NIXOS_USAGE = """
Usage: homelab nixos <sub-command> [...arguments]

sub-command:

    setup:

        Perform setup actions for the system.
        Run only once for a new system.

    switch:

        Switch to new configuration by rebuilding using nixos.
"""
