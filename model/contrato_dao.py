
from app import db
from model import Hospede

class Contrato(db.Model):
    __tablename__ = 'contrato'
    codr = db.Column(db.Integer, db.ForeignKey('reserva.codr'), primary_key=True)
    codh = db.Column(db.Integer, db.ForeignKey('hospede.codh'))

def insert_from_dict(data: dict):
    contrato = from_dict(data)
    insert(contrato)

def insert(contrato: Contrato):
    db.session.add(contrato)
    db.session.commit()

def from_dict(_dict: dict) -> Contrato:
    return  Contrato (
        codr = _dict['reserva'],
        codh = _dict['hospede'],
    )