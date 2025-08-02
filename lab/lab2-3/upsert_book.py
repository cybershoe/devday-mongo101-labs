from pymongo import MongoClient
from os import getenv
from bson.objectid import ObjectId

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["lab2_db"]
collection = db["books"]

book = {
  "title": "War and Peace",
  "author": {
    "first": "Leo",
    "last": "Tolstoy"
  },
  "published_year": 1868
}

response = collection.replace_one({"title": book['title']}, book)

print(f"Acknowledged: {response.acknowledged}")
print(f"Documents matched: {response.matched_count}")
print(f"Documents modified: {response.modified_count}")
if response.did_upsert:
    print(f"Upserted document: {response.upserted_id}")
