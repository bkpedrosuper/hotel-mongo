from flask_wtf import FlaskForm
from wtforms import IntegerField, SelectField, StringField
from wtforms.validators import Length, DataRequired
from bson.objectid import ObjectId

from model import empregado_dao
default_manager_id = ObjectId("507f191e810c19729de860ea")

class EmpregadoForm(FlaskForm):
    nome = StringField('Nome *', validators=[DataRequired()])
    cpf = StringField('CPF *', validators=[DataRequired(), Length(min=11, max=11)])
    pis = StringField('PIS *', validators=[DataRequired(), Length(min=11, max=11)])
    cargo = StringField('Cargo *', validators=[DataRequired(), Length(max=25)])
    gerente = SelectField("Gerente", validators=[], coerce=ObjectId)
    
    numero = StringField('Numero da Casa', validators=[Length(max=5)])
    rua = StringField('Rua', validators=[Length(max=50)])
    bairro = StringField('Bairro', validators=[Length(max=25)])

    def __init__(self):
        super(EmpregadoForm, self).__init__()
        self.gerente.choices = [(default_manager_id, "---")] + [(
                                empregado.get("_id"),
                                empregado.get('nome') + ' - ' + empregado.get('cpf')
                                )
                                for empregado in empregado_dao.select_all()]