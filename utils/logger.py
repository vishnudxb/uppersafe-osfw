#!/usr/bin/env python3
##
# Nicolas THIBAUT
# nicolas.thibaut@uppersafe.com
##
# -*- coding: utf-8 -*-

import logging, colorlog

banner = '''
####
## UPPERSAFE-OSFW (UPPERSAFE Open Source Firewall)
## Version: 0.0.1
## License: GNU AGPLv3
## Author: Nicolas THIBAUT (nicolas[@]uppersafe[.]com)
## Debug: {}
####
'''

class logger:
    def __init__(self, name, verbose):
        handler = colorlog.StreamHandler()
        handler.setFormatter(colorlog.ColoredFormatter(
            "%(asctime)s | %(log_color)s%(levelname)-8s%(reset)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            reset=True,
            log_colors={
                "DEBUG": "cyan,bg_black",
                "INFO": "green,bg_black",
                "WARNING": "yellow,bg_black",
                "ERROR": "red,bg_black",
                "CRITICAL": "red,bg_white"
                },
            secondary_log_colors={},
            style="%"
            ))
        manager = colorlog.getLogger(name)
        manager.addHandler(handler)
        if verbose:
            manager.setLevel(logging.DEBUG)
        else:
            manager.setLevel(logging.INFO)
        for line in [x for x in banner.format(verbose).splitlines() if x.strip()]:
            manager.info(line)
        self.debug = manager.debug
        self.info = manager.info
        self.warning = manager.warning
        self.error = manager.error
        self.critical = manager.critical
