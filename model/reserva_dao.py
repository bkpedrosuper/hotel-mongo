from app import db, mongo
from routes.reserva import reserva
from bson.objectid import ObjectId

class Reserva():
    tablename = 'reserva'
    def __init__(self):
        self.db = mongo.db
        self.collection = mongo.db["reserva"]

def select_next_id() -> int:
    f = db.func.nextval('reserva_codr_seq')
    return db.session.query(f).first()[0]

def select_all():
    # from model import Quarto
    # quarto = Quarto()
    reserva = Reserva()

    # query
    rooms_lookup = {
            "$lookup": {
                "from": "quarto",
                "localField": "quarto",
                "foreignField": "_id",
                "as": "quarto",
            },
    }

    reservation_query = {
        "$unset": ["csrf_token"]
    }

    rooms_query = {
        "$project": {"quarto._id": 0, "quarto.ramal": 0, "quarto.preco_dia": 0, "quarto.csrf_token": 0}
    }

    query = [
        rooms_lookup,
        reservation_query,
        rooms_query
    ]
    results = reserva.collection.aggregate(query)
    return results

def insert(data: dict):
    reserva = Reserva()
    data['numero_ocupantes'] = 0
    reserva.collection.insert_one(data)

def increase_occupants_of_reservation(id: ObjectId):
    reserva = Reserva()
    reserva.collection.update_one( {"_id": id},
        {
            "$inc": {
                "numero_ocupantes": 1
            }
        })