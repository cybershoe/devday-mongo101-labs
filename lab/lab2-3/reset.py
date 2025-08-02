from pymongo import MongoClient
from os import getenv

MONGO_URI = getenv("MDB_URI")

db_name = "lab2_db"
collection_name = "books"

client = MongoClient(MONGO_URI)
db = client[db_name]

try:
    response = db.drop_collection(collection_name)
except Exception as e:
    print(f"Error dropping collection {collection_name}")
    raise(e)
else:
    print(f"Dropped collection {collection_name}")
