#!/usr/bin/env python
# File: log.py

# Color log text. Works on OS X, Linux, and Windows with ansi.sys enabled.
class logColor:
    OKBLUE = '\033[34m'
    BOLD = '\033[1m'
    END = '\033[0m'
    ERROR = '\033[91m'
    INFO = '\033[92m'
    UNDERLINE = '\033[4m'
    WARN = '\033[93m'
