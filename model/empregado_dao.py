
from app import db
from sqlalchemy.sql.functions import coalesce
from sqlalchemy import func, null
from app import db, mongo
from bson.objectid import ObjectId

class Empregado():
    tablename = 'empregado'
    def __init__(self):
        self.db = mongo.db
        self.collection = mongo.db["empregado"]

def select_all():
    empregado = Empregado()
    empregados = empregado.collection.find({}, {"csrf_token": 0})
    return empregados

def insert(data: dict):
    empregado = Empregado()
    empregado.collection.insert_one(data)