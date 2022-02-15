from app import db, mongo

class Quarto():
    tablename = 'quarto'
    def __init__(self):
        self.db = mongo.db
        self.collection = mongo.db["quarto"]

def select_all():
    quarto = Quarto()
    quartos = quarto.collection.find({}, {"csrf_token": 0})
    return quartos

def insert_in_mongo(data: dict):
    quarto = Quarto()
    quarto.collection.insert_one(data)