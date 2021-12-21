
from app import db


class Quarto(db.Model):
    __tablename__ = 'quarto'
    codq = db.Column(db.Integer, primary_key=True)
    ramal = db.Column(db.Integer)
    preco_dia = db.Column(db.Numeric(precision=2))
    numero = db.Column(db.Integer, nullable=False)
    andar = db.Column(db.Integer, nullable=False)


def select_next_id() -> int:
    f = db.func.nextval('quarto_codq_seq')
    return db.session.query(f).first()[0]

def select_all():
    return db.session.query(Quarto.codq, Quarto.numero, Quarto.andar, Quarto.preco_dia.label(f'Preço do Quarto em R$')).all()

def insert_from_dict(data: dict):
    hospede = from_dict(data)
    insert(hospede)

def insert(hospede: Quarto):
    db.session.add(hospede)
    db.session.commit()

def from_dict(_dict: dict) -> Quarto:
    return Quarto (
        codq=(_dict['codq'] if 'codq' in _dict else None),
        ramal = _dict['ramal'],
        numero = _dict['numero'],
        preco_dia = _dict['preco_dia'],
        andar = _dict['andar'],
    )