
from app import db, mongo
from model.reserva_dao import increase_occupants_of_reservation

class Contrato():
    tablename = 'contrato'
    def __init__(self):
        self.db = mongo.db
        self.collection = mongo.db["contrato"]

def insert(data: dict):
    contrato = Contrato()
    try:
        increase_occupants_of_reservation(data['reserva'])
        return contrato.collection.insert_one(data)
    except:
        return
    