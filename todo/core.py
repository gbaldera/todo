# -*- coding: utf-8 -*-

from flask import Flask, request, g, url_for, redirect, abort, render_template, session, flash
from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash
from .decorators import requires_login
from .forms import LoginForm

app = Flask(__name__)
app.config.from_object('config') #configurar app usando variables en config.py

db = SQLAlchemy(app)

#importamos modelos luego de crear el objecto db ya que es una dependencia circular
from .models import Usuario, Todo

@app.before_request
def before_request():
    """
    Si el usuario esta logueado, buscarlo en la db
    """
    g.usuario = None

    if 'usuario_id' in session:
        g.usuario = Usuario.query.get(session['usuario_id'])

@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login para usuarios
    """

    #verificar si esta logueado
    if g.usuario is not None:
        return redirect(url_for('index'))

    # inicializamos la validacion
    form = LoginForm(request.form)

    # validar datos del formulario cuando se haga un POST
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario and check_password_hash(usuario.password, form.password.data):
            session['usuario_id'] = usuario.id
            return redirect(url_for('index'))
        flash(u'Email o Contrasena incorrectos', 'error')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    """
    Desloguear usuario
    """
    if g.usuario is not None:
        session.pop('usuario_id', None)
    return redirect(url_for('login'))

@app.route('/')
@requires_login
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
