from pymongo import MongoClient
from os import getenv

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["lab2_db"]
collection = db["books"]

book = {
  "title": "The Great Gatsby",
  "author": {
    "first": "F. Steve",
    "last": "Fitzgerald"
  },
  "published_year": 1924
}

response = collection.insert_one(book)

print(f"Acknowledged: {response.acknowledged}\nInserted _id: {response.inserted_id}")
