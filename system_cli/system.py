#!/usr/bin/env python

import utils
from config import values as v
from config import usage as u

import sys

if __name__ == "__main__":
    args = sys.argv[:]
    program = args.pop(0)

    if len(args) == 0:
        utils.io.info("system", u.SYSTEM_USAGE)
        exit(1)

    command = args.pop(0)

    if command == "help":
        utils.io.info("system", u.SYSTEM_USAGE)
    else:
        utils.io.error("system",
                       f'Unknown command "{command}"\n'
                       "Run 'system help' for list of commands"
                       )

    exit(0)
