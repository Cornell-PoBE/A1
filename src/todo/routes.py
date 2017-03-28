from flask import jsonify
from todo import app
import models

@app.route('/', methods=['GET'])
def index():
  return jsonify({ 'hello': 'world' })
