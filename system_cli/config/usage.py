SYSTEM_USAGE = """
Usage: system <command> <sub-command> [..arguments]

command:

    help:

        Print the help message and exit.

    nixos:

        Control system-level configuration.

    service:
"""

NIXOS_USAGE = """
Usage: system nixos <sub-command> [..arguments]

sub-command:

    help:

        Print the help message and exit.

    setup:

        Perform setup actions for the system.
        Run only once for a new system.

    switch:

        Switch to new configuration by rebuilding using nixos.
"""

SERVICE_USAGE = """
Usage: system service <sub-command> [..arguments]

sub-command:

    help:

        Print help message and exit.
"""
