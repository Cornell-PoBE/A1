from flask import jsonify
from todo import app
from todo import Db as db
import models

@app.route('/', methods=['GET'])
def index():
  return jsonify({ 'hello': 'world' })
