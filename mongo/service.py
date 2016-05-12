from pymongo import MongoClient


def _get_database_session():
    client = MongoClient('localhost', 27017)
    db = client.p2_database

def get_collection(collection):
    col = db[collection]
    return col
