__author__ = 'gbaldera'

from core import db
from datetime import datetime

class Usuario(db.Model):

    __tablename__ = 'usuarios' #por defecto seria el nombre del modelo en miniscula

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(20))
    todos = db.relationship('Todo', backref=db.backref('usuario', lazy='dynamic'))

    def __init__(self, nombre=None, email=None, password=None):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Usuario %r>' % self.nombre

class Todo(db.Model):

    __tablename__ = 'todos'

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(20))
    descripcion = db.Column(db.Text, nullable=True)
    fecha = db.Column(db.DateTime)
    listo = db.Column(db.Boolean, default=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))

    def __init__(self, titulo=None, descripcion=None, fecha=None, listo=None):
        self.titulo = titulo
        self.descripcion = descripcion
        self.listo = listo

        if fecha is None:
            fecha = datetime.utcnow()

        self.fecha = fecha

    def __repr__(self):
        return '<Todo %r>' % self.titulo
