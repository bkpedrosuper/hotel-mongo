from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField, SelectField
from wtforms.fields.html5 import DateField, DateTimeLocalField
from wtforms.validators import DataRequired, Length
from bson.objectid import ObjectId

from model import quarto_dao



class ReservaForm(FlaskForm):
    quarto = SelectField("Quarto *", validators=[DataRequired()], coerce=ObjectId)
    dt_entrada = DateTimeLocalField("Data de Entrada *", format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    dt_saida = DateTimeLocalField("Data de Saída *", format='%Y-%m-%dT%H:%M', validators=[DataRequired()])

    def __init__(self):

        super(ReservaForm, self).__init__()
        self.quarto.choices = [(
                                quarto.get('_id'),
                                'Numero: ' + str(quarto.get('numero')) + ' Andar: ' + str(quarto.get('andar')) 
                                )
                                for quarto in quarto_dao.select_all()]