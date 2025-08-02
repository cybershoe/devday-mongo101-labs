from pymongo import MongoClient
from os import getenv

MONGO_URI = getenv("MDB_URI")

db_name = "lab2_db"

client = MongoClient(MONGO_URI)

try:
    response = client.drop_database(db_name)
except Exception as e:
    print(f"Error dropping database {db_name}")
    raise(e)
else:
    print(f"Dropped database {db_name}")
