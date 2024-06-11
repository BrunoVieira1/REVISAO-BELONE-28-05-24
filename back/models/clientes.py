from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Clientes(db.Model):
    def to_dict(self):
        return {
            'nome': self.nome,
            'email': self.email,
            'cargo_id': self.cargo_id
        }
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cargo_id = db.Column(ForeignKey('cargos.id'))

    cargo = relationship('Cargos', backref='clientes')

    def __init__(self, nome, email, cargo_id):
        self.nome = nome
        self.email = email
        self.cargo_id = cargo_id
