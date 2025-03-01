# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

bind = '0.0.0.0:5005'
workers = 1


# accesslog = '-'

accesslog = "/var/log/gunicorn/access.log"  # Access logs
errorlog = "/var/log/gunicorn/error.log"  # Error logs
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
