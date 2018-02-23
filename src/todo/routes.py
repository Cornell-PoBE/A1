from flask import jsonify, request
from todo import app
from todo import Db as db
from models import Task
from datetime import datetime
import json

@app.route('/', methods=['GET'])
def index():
  return jsonify({ 'hello': 'world' })
