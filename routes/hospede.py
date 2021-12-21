from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import hospede_dao as dao
from forms import HospedeForm


blue = Blueprint('hospede', __name__, static_folder='static', template_folder='templates')


@blue.route('/hospede')
def hospede():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Hospede', table=table)


@blue.route('/hospede_form', methods=['GET', 'POST'])
def hospede_form():
    form = HospedeForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Hospede', form=form, erro=erro)
        return redirect('/hospede')
    return render_template('form.html', title='Hospede', form=form, erro=erro)
