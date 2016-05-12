from pymongo import MongoClient
import json

def _get_database_session():
    client = MongoClient('localhost', 27017)
    db = client.p2_database
    return db


def get_collection(collection):
    db = _get_database_session()
    col = db[collection]
    return col


def insertItem(c, i):
    col = get_collection(c)
    a = col.insert_one(json.loads(i))
    print a

def getItmes(c):
    col = get_collection(c)
    a = col.find()
    return a
