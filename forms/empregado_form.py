from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import Length, DataRequired

from model import empregado_dao

class EmpregadoForm(FlaskForm):
    nome = StringField('Nome *', validators=[DataRequired()])
    cpf = StringField('CPF *', validators=[DataRequired(), Length(min=11, max=11)])
    pis = StringField('PIS *', validators=[DataRequired(), Length(min=11, max=11)])
    cargo = StringField('Cargo *', validators=[DataRequired(), Length(max=25)])
    gerente = SelectField("Gerente", validators=[], coerce=int)
    
    numero = StringField('Numero da Casa', validators=[Length(max=5)])
    rua = StringField('Rua', validators=[Length(max=50)])
    bairro = StringField('Bairro', validators=[Length(max=25)])

    def __init__(self):
        super(EmpregadoForm, self).__init__()
        self.gerente.choices = [(0, "---")] + [(empregado.code,
                                empregado['Nome'])
                                for empregado in empregado_dao.select_all()]