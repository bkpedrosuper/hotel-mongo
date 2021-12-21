from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email

from model import reserva_dao
from model import hospede_dao



class ContratoForm(FlaskForm):
    reserva = SelectField("Quarto *", validators=[DataRequired()], coerce=int)
    hospede = SelectField("Hospede *", validators=[DataRequired()], coerce=int)

    def __init__(self):
        super(ContratoForm, self).__init__()
        self.reserva.choices = [(reserva.codr,
                                f'Quarto: {reserva.numero} nº ocupantes: {reserva.numero_ocupantes}) Data Fim: {reserva.dt_saida}')
                                for reserva in reserva_dao.select_query()]
        self.hospede.choices = [(hospede.codh,
                                f'{hospede.nome} - {hospede.cpf}')
                                for hospede in hospede_dao.select_all()]