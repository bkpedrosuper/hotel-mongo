from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length, Email

from model import quarto_dao



class ReservaForm(FlaskForm):
    quarto = SelectField("Quarto *", validators=[DataRequired()], coerce=int)
    dt_entrada = DateField("Data de Entrada *", validators=[DataRequired()])
    dt_saida = DateField("Data de Saída *", validators=[DataRequired()])

    def __init__(self):

        super(ReservaForm, self).__init__()
        self.quarto.choices = [(quarto.codq,
                                f'(Número: {quarto.numero}; Andar: {quarto.andar})')
                                for quarto in quarto_dao.select_all()]