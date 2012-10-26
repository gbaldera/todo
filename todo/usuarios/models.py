__author__ = 'gbaldera'

from todo import db

class Usuario(db.Model):

    __tablename__ = 'usuarios' #por defecto seria el nombre del modelo en miniscula

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    email = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(60))
    todos = db.relationship('Todo', backref=db.backref('usuario', lazy='joined'), lazy='dynamic')

    def __init__(self, nombre=None, email=None, password=None):
        self.nombre = nombre
        self.email = email
        self.password = password

    def __repr__(self):
        return '<Usuario %r>' % self.nombre
