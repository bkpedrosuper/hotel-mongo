
from app import db


class Hospede(db.Model):
    __tablename__ = 'hospede'
    codh = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telefone = db.Column(db.String(15), nullable=False)


def select_next_id() -> int:
    f = db.func.nextval('hospede_codh_seq')
    return db.session.query(f).first()[0]

def select_all():
    return db.session.query(Hospede.codh, Hospede.nome, Hospede.telefone, Hospede.cpf).all()

def insert_from_dict(data: dict):
    hospede = from_dict(data)
    insert(hospede)

def insert(hospede: Hospede):
    db.session.add(hospede)
    db.session.commit()

def from_dict(_dict: dict) -> Hospede:
    return Hospede (
        codh=(_dict['codh'] if 'codh' in _dict else None),
        nome = _dict['nome'],
        cpf = _dict['cpf'],
        email = _dict['email'],
        telefone = _dict['telefone'],
    )