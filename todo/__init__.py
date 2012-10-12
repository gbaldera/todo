# -*- coding: utf-8 -*-

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config') #configurar app usando variables en config.py

db = SQLAlchemy(app)

# importamos modelos luego de crear el objecto db ya que es una dependencia circular
from todo.usuarios.views import usuarios

# registrar blueprints
app.register_blueprint(usuarios)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
