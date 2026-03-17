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

    check <service_name>:

        Check if a service is configured correctly.
        Pass empty service name to check all services.

    up <service_name>:

        Compose up a service.
        Pass empty service name to compose up all services.

    down <service_name>:

        Compose down a service.
        Pass empty service name to compose down all services.
"""
