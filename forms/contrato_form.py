from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from bson.objectid import ObjectId

from model import reserva_dao
from model import hospede_dao



class ContratoForm(FlaskForm):
    reserva = SelectField("Quarto *", validators=[DataRequired()], coerce=ObjectId)
    hospede = SelectField("Hospede *", validators=[DataRequired()], coerce=ObjectId)

    def __init__(self):
        super(ContratoForm, self).__init__()
        self.reserva.choices = [(
                                reserva.get('_id'),
                                'Quarto: ' + str(reserva.get('quarto')) + ' | nº ocupantes: ' + str(reserva.get('numero_ocupantes')) + ' | Data Fim: ' + str(reserva.get('dt_saida'))
                                )
                                for reserva in reserva_dao.select_all()]

        self.hospede.choices = [(
                                hospede.get('_id'),
                                'Nome: ' + hospede.get('nome') + ' | CPF: ' + hospede.get('cpf')
                                )
                                for hospede in hospede_dao.select_all()]
