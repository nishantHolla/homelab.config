HOMELAB_USAGE = """
Usage: homelab <command> <sub-command> [..arguments]

command:

    help:

        Print the help message and exit.

    nixos:

        Control system-level configuration.

    service:
"""

NIXOS_USAGE = """
Usage: homelab nixos <sub-command> [..arguments]

sub-command:

    help:

        Print the help message and exit.

    setup:

        Perform setup actions for the system.
        Run only once for a new system.

    switch:

        Switch to new configuration by rebuilding using nixos.
"""
