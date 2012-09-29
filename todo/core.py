from flask import Flask, request, url_for, redirect, abort, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #configurar app usando variables en config.py

db = SQLAlchemy(app)

#importamos modelos luego de crear el objecto db ya que es una dependencia circular
from models import *

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
