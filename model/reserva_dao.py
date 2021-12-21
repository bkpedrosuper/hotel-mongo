
from app import db
from model.empregado_dao import Empregado

class Reserva(db.Model):
    __tablename__ = 'reserva'
    codr = db.Column(db.Integer, primary_key=True)
    codq = db.Column(db.Integer, db.ForeignKey('quarto.codq'))
    code = db.Column(db.Integer, db.ForeignKey('empregado.code'), default=2)
    numero_ocupantes = db.Column(db.Integer, default=0)
    dt_entrada = db.Column(db.Date)
    dt_saida = db.Column(db.Date)

def select_next_id() -> int:
    f = db.func.nextval('reserva_codr_seq')
    return db.session.query(f).first()[0]

def select_all():
    from model import Quarto
    return db.session.query(Reserva.codr, Reserva.numero_ocupantes, Reserva.dt_entrada.label('Data de Entrada'), Reserva.dt_saida.label('Data de Saída'), Quarto.numero.label('Número do Quarto')) \
        .join(Quarto, Quarto.codq == Reserva.codq) \
        .all()

def select_query():
    from model import Quarto
    return db.session.query(Reserva.codr, Reserva.numero_ocupantes, Reserva.dt_entrada, Reserva.dt_saida, Quarto.numero) \
        .join(Quarto, Quarto.codq == Reserva.codq) \
        .all()

def insert_from_dict(data: dict):
    reserva = from_dict(data)
    insert(reserva)

def insert(reserva: Reserva):
    db.session.add(reserva)
    db.session.commit()

def from_dict(_dict: dict) -> Reserva:
    return  Reserva (
        codr=(_dict['codr'] if 'codr' in _dict else None),
        codq = _dict['quarto'],
        dt_entrada = _dict['dt_entrada'],
        dt_saida = _dict['dt_saida'],
    )