from todo import Db as db
from todo import app
import simplejson as json
import unittest
from datetime import datetime
from flask import Flask, jsonify

class test(unittest.TestCase):
	def is_sub(self, sub, lst):
		lst_s = set(lst)
		for s in sub:
		  if s not in lst_s:
		    return False
		return True

	def setUp(self):
		self.app = app.test_client()
		self.app.testing = True
		db.create_task_table()

	def tearDown(self):
		db.delete_task_table()

	def test_create_task(self):
		input_data = dict(
	     name="jogging",
	     description="Need to jog",
	     tags="run,jog,sprint",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		result = json.loads(self.app.post('/tasks', data=input_data, follow_redirects=False).data)
		assert(result["name"] == input_data["name"])
		assert(result["description"] == input_data["description"])
		assert(result["tags"] == input_data["tags"])
		assert(result["due_date"] == input_data["due_date"])

	def test_get_tasks(self):
		input_data = dict(
	     name="jogging",
	     description="Need to jog",
	     tags="run,jog,sprint",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		input_data2 = dict(
	     name="shopping",
	     description="Need to shop",
	     tags="buy,stuff,money",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		self.app.post('/tasks', data=input_data, follow_redirects=False)
		self.app.post('/tasks', data=input_data2, follow_redirects=False)
		result = json.loads(self.app.get("/tasks").data)
		columns = ['DUE_DATE', 'NAME', 'TAGS', 'CREATED_AT', 'ID', 'DESCRIPTION']
		for row in result:
			assert(self.is_sub(row.keys(),columns))
		assert(len(result) == 2)

	def test_delete_task(self):
		input_data = dict(
	     name="jogging",
	     description="Need to jog",
	     tags="run,jog,sprint",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		result_id = json.loads(self.app.post('/tasks', data=input_data, follow_redirects=False).data)["id"]
		result = json.loads(self.app.get("/tasks", data={"id": result_id}).data)
		assert(len(result) == 1)
		result = self.app.delete("/tasks", data={"id": result_id})
		result = json.loads(self.app.get("/tasks", data={"id": result_id}).data)
		assert(len(result) == 0)

	def test_delete_tasks(self):
		input_data = dict(
	     name="jogging",
	     description="Need to jog",
	     tags="run,jog,sprint",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		input_data2 = dict(
	     name="shopping",
	     description="Need to shop",
	     tags="buy,stuff,money",
	     due_date=int((datetime.now()-datetime(1970,1,1)).total_seconds()))
		self.app.post('/tasks', data=input_data, follow_redirects=False)
		self.app.post('/tasks', data=input_data2, follow_redirects=False)
		result = json.loads(self.app.get("/tasks").data)
		assert(len(result) == 2)
		self.app.delete("/tasks/all")
		result = json.loads(self.app.get("/tasks").data)
		assert(len(result) == 0)

if __name__ == '__main__':
	unittest.main()
