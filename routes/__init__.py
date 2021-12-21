from routes import hospede
from routes import quarto
from routes import reserva
from routes import contrato
from routes import empregado

blueprints = [
    hospede.blue,
    quarto.blue,
    reserva.blue,
    contrato.blue,
    empregado.blue,
]
