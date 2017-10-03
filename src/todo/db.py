import os
import json
import sqlite3

# From: https://goo.gl/YzypOI
def singleton(cls):
  instances = {}
  def getinstance():
    if cls not in instances:
      instances[cls] = cls()
    return instances[cls]
  return getinstance

class DB(object):
  """
  DB driver for the Todo app - deals with writing entities
  to the DB and reading entities from the DB
  """

  def __init__(self):
    self.conn = sqlite3.connect("todo.db", check_same_thread=False)
    self.example_create_table()
    # TODO - Create all other tables here

  def create_task_table(self):
    # TODO - Implement this to create a task table
    pass

  def delete_task_table(self):
    # TODO - Implement this to delete a task table
    pass

  def example_create_table(self):
    """
    Demonstrates how to make a table. Silently error-handles
    (try-except) because the table might already exist.
    """
    try:
      self.conn.execute("""
        CREATE TABLE example
        (ID INT PRIMARY KEY NOT NULL,
        NAME TEXT NOT NULL,
        ADDRESS CHAR(50) NOT NULL);
      """)
    except Exception as e: print e

  def example_query(self):
    """
    Demonstrates how to execute a query.
    """
    cursor = self.conn.execute("""
      SELECT * FROM example;
    """)

    for row in cursor:
      print "ID = ", row[0]
      print "NAME = ", row[1]
      print "ADDRESS = ", row[2], "\n"

  def example_insert(self):
    """
    Demonstrates how to perform an insert operation.
    """
    self.conn.execute("""
      INSERT INTO example (ID,NAME,ADDRESS)
      VALUES (1, "Joe", "Ithaca, NY");
    """)
    self.conn.commit()


# Only <=1 instance of the DB driver
# exists within the app at all times
DB = singleton(DB)
