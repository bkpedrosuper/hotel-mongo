from app import mongo

class Hospede():
    tablename = 'hospede'
    def __init__(self):
        self.db = mongo.db
        self.collection = mongo.db["hospede"]

def select_all():
    hospede = Hospede()
    hospedes = hospede.collection.find({}, {"csrf_token": 0})
    return hospedes

def insert_in_mongo(data: dict):
    hospede = Hospede()
    return hospede.collection.insert_one(data)