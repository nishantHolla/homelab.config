HOMELAB_USAGE = """
Usage: homelab <command> <sub-command> [..arguments]

command:

    help:

        Print the help message and exit.

    nixos:

        Control system-level configuration.

    service:

        Control services of the homelab.
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

SERVICE_USAGE = """
Usage: homelab service <sub-command> [..arguments]

sub-command:

    help:

        Print the help message and exit.

    up <service_name?>:

        Prepare environment for the service and starts up the given service
        Leave service_name blank to start all services.

    down <service_name?>:

        Shutdown the given service.
        Leave service_name blank to stop all services.

    list

        List all the services and their status.
"""
