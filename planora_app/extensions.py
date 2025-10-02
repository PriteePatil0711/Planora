<<<<<<< HEAD
=======
from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

_client = None
_db = None

def get_db():
    global _client, _db
    if _db is None:
        _client = MongoClient(MONGO_URI)
        _db = _client[DB_NAME]
    return _db


>>>>>>> 69acf346a534693072f84e091c7dfafa6036be5e
