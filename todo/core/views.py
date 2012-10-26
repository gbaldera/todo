# -*- coding: utf-8 -*-

from flask import  Blueprint, request, g, url_for, redirect, render_template, session, flash, abort
from todo.decorators import requires_login
from todo.usuarios.models import Usuario
from todo.core.models import Todo
from todo import db

mod = Blueprint('core', __name__, url_prefix='/')

@mod.before_request
def before_request():
    """
    Si el usuario esta logueado, buscarlo en la db
    """
    g.usuario = None

    if 'usuario_id' in session:
        g.usuario = Usuario.query.get(session['usuario_id'])

@mod.route('/')
@requires_login
def index():
    return 'Hello World!'
