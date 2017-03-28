import os
import json

# From https://goo.gl/YzypOI
def singleton(cls):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls()
    return instances[cls]
  return getinstance

class DB(object):
  """
  File-based DB driver
  """

  def __init__(self):
    self.out = './db'





# Bootstrap singleton
DB = singleton(DB)
