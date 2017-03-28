import os
basedir = os.path.abspath(os.path.dirname(__file__))

# Environments for the app the run in -
# NOTE! This app only has one environment to run
# in, but one could specify multiple classes
# here to differentiate different environments the
# backend could run in

class Config(object):
  DEBUG = True
  CSRF_ENABLED = True
  CSRF_SESSION_KEY = "secret-1"
  SECRET_KEY = "secret-2"
  THREADS_PER_PAGE = 2
