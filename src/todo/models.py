from abc import ABCMeta
import uuid

class Model(object):
  """
  Abstract base class for all models -
  all models should extend this class 
  """
  __metaclass__ = ABCMeta

  def __init__(self, id):
    """
    Initializes the model with a Universal Unique
    Identifier as an id
    """
    self.id = str(uuid.uuid1())



# TODO - Add models here
