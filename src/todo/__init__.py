from flask import Flask, render_template
import os


app = Flask(__name__)
app.config.from_object('config.Config')

@app.errorhandler(404)
def not_found(error):
  return render_template('404.html'), 404

# Import all endpoints
import todo.routes
