from flask import Flask, render_template
import db
import os

# App instance
app = Flask(__name__)
app.config.from_object('config.Config')

# Database driver instance
Db = db.DB()

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

# Import all endpoints
import todo.routes
