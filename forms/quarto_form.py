from flask_wtf import FlaskForm
from wtforms import FloatField, IntegerField
from wtforms.validators import DataRequired, Length, Email


class QuartoForm(FlaskForm):
    
    numero = IntegerField('Número *', validators=[DataRequired()])
    ramal = IntegerField('Ramal *', validators=[DataRequired()])
    andar = IntegerField('Andar *', validators=[DataRequired()])
    preco_dia = FloatField('Preço do Quarto *', validators=[DataRequired()])
