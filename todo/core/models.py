from todo import db
from datetime import datetime

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
