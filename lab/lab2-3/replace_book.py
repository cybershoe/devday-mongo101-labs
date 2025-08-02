from pymongo import MongoClient
from os import getenv
from bson.objectid import ObjectId

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["lab2_db"]
collection = db["books"]

book = {
  "title": "The Great Gatsby",
  "author": {
    "first": "F. Scott",
    "last": "Fitzgerald"
  },
  "published_year": 1924
}

response = collection.replace_one({"_id": ObjectId("your object _id here")}, book)

print(f"Acknowledged: {response.acknowledged}")
print(f"Documents matched: {response.matched_count}")
print(f"Documents modified: {response.modified_count}")
