from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, render_template, redirect

from model import reserva_dao as dao
from forms import ReservaForm


blue = Blueprint('reserva', __name__, static_folder='static', template_folder='templates')


@blue.route('/reserva')
def reserva():
    rows = dao.select_all()
    table = [dict(row) for row in rows]
    return render_template('table.html', title='Reserva', table=table)


@blue.route('/reserva_form', methods=['GET', 'POST'])
def reserva_form():
    form = ReservaForm()
    erro = None
    if form.validate_on_submit():
        try:
            dao.insert(form.data)
        except SQLAlchemyError as e:
            erro = e
            return render_template('form.html', title='Reserva', form=form, erro=erro)
        return redirect('/reserva')
    return render_template('form.html', title='Reserva', form=form, erro=erro)
