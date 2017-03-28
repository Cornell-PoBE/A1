import os
import json

class DB(object):
  """
  File-based DB driver
  """

  def __init__(self, db_class):
    self.out = './db'
    self.cls = db_class
