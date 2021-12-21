from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import contrato_dao as dao
from forms import ContratoForm


blue = Blueprint('contrato', __name__, static_folder='static', template_folder='templates')


@blue.route('/contrato')
def contrato():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Contrato', table=table)


@blue.route('/contrato_form', methods=['GET', 'POST'])
def contrato_form():
    form = ContratoForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Realizar Reserva para um Hóspede', form=form, erro=erro)
        return redirect('/reserva')
    return render_template('form.html', title='Novo Contrato de Reserva', form=form, erro=erro)
