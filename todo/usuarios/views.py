# -*- coding: utf-8 -*-

from flask import  Blueprint, request, g, url_for, redirect, render_template, session, flash, abort
from werkzeug.security import check_password_hash
from todo.usuarios.forms import LoginForm
from todo.usuarios.models import Usuario
from todo.decorators import requires_login
from todo import db

usuarios = Blueprint('usuarios', __name__, url_prefix='/usuarios')

@usuarios.before_request
def before_request():
    """
    Si el usuario esta logueado, buscarlo en la db
    """
    g.usuario = None

    if 'usuario_id' in session:
        g.usuario = Usuario.query.get(session['usuario_id'])

@usuarios.route('/login', methods=['GET', 'POST'])
def login():
    """
    Login para usuarios
    """

    #verificar si esta logueado
    if g.usuario is not None:
        return redirect(url_for('.index'))

    # inicializamos la validacion
    form = LoginForm(request.form)

    # validar datos del formulario cuando se haga un POST
    if form.validate_on_submit():
        usuario = Usuario.query.filter_by(email=form.email.data).first()

        if usuario and check_password_hash(usuario.password, form.password.data):
            session['usuario_id'] = usuario.id
            return redirect(url_for('.index'))
        flash(u'Email o Contrasena incorrectos', 'error')

    return render_template('login.html', form=form)

@usuarios.route('/logout')
def logout():
    """
    Desloguear usuario
    """
    if g.usuario is not None:
        session.pop('usuario_id', None)
    return redirect(url_for('.login'))

@usuarios.route('/')
@requires_login
def index():
    return 'Hello World!'
