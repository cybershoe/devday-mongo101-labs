from pymongo import MongoClient
from os import getenv
from pprint import pprint

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["sample_restaurants"]
collection = db["restaurants"]

response = collection.find_one({"restaurant_id": "40356151"}, {"_id": 0})

pprint(response)