from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class HospedeForm(FlaskForm):
    nome = StringField('Nome *', validators=[DataRequired()])
    telefone = StringField('Telefone *', validators=[DataRequired()])
    email = StringField('E-mail *', validators=[DataRequired(), Email(message="Seu e-mail precisa ser válido!")])
    cpf = StringField('CPF *', validators=[DataRequired(), Length(min=11, max=11)])
