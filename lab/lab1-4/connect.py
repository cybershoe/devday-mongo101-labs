from pymongo import MongoClient
from pprint import pprint

MONGO_URI = "your connection string here"

client = MongoClient(MONGO_URI)
db = client["sample_restaurants"]
collection = db["restaurants"]

response = collection.find_one({"restaurant_id": "40356151"}, {"_id": 0})

pprint(response)