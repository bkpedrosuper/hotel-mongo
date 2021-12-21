from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import quarto_dao as dao
from forms import QuartoForm


blue = Blueprint('quarto', __name__, static_folder='static', template_folder='templates')


@blue.route('/quarto')
def quarto():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Quarto', table=table)


@blue.route('/quarto_form', methods=['GET', 'POST'])
def quarto_form():
    form = QuartoForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert_from_dict(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Quarto', form=form, erro=erro)
        return redirect('/quarto')
    return render_template('form.html', title='Quarto', form=form, erro=erro)
