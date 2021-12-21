
from app import db
from sqlalchemy.sql.functions import coalesce
from sqlalchemy import func

class Empregado(db.Model):
    __tablename__ = 'empregado'
    code = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    pis = db.Column(db.String(11), nullable=False)
    cargo = db.Column(db.String(25), nullable=False)
    codg = db.Column(db.Integer, db.ForeignKey('empregado.code'))
    numero = db.Column(db.Integer)
    rua = db.Column(db.String(50))
    bairro = db.Column(db.String(25))

def select_next_id() -> int:
    f = db.func.nextval('empregado_code_seq')
    return db.session.query(f).first()[0]

def select_all():
    empregado_alias = db.aliased(Empregado)
    return db.session.query(Empregado.code, Empregado.nome.label('Nome'), Empregado.cargo.label('Cargo'), func.coalesce(empregado_alias.nome, 'Nenhum').label('Gerente')) \
        .outerjoin(empregado_alias, empregado_alias.code == Empregado.codg) \
        .all()

def insert_from_dict(data: dict):
    empregado = from_dict(data)
    insert(empregado)

def insert(empregado: Empregado):
    db.session.add(empregado)
    db.session.commit()

def from_dict(_dict: dict) -> Empregado:
    return  Empregado (
        code=(_dict['code'] if 'code' in _dict else None),
        nome = _dict['nome'],
        cpf = _dict['cpf'],
        pis = _dict['pis'],
        cargo = _dict['cargo'],
        numero = (int(_dict['numero']) if _dict['numero'] else None),
        rua = _dict['rua'] if _dict['rua'] else None,
        bairro = _dict['bairro'] if _dict['bairro'] else None,
        codg = (_dict['gerente'] if _dict['gerente'] > 0 else None)
    )