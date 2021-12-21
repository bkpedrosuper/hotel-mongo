from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import empregado_dao as dao
from forms import EmpregadoForm


blue = Blueprint('empregado', __name__, static_folder='static', template_folder='templates')


@blue.route('/empregado')
def empregado():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Empregado', table=table)


@blue.route('/empregado_form', methods=['GET', 'POST'])
def empregado_form():
    form = EmpregadoForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Empregado', form=form, erro=erro)
        return redirect('/empregado')
    return render_template('form.html', title='Empregado', form=form, erro=erro)
