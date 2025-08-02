from pymongo import MongoClient
from pprint import pprint
from bson import decode
from os import getenv

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["lab2_db"]
collection = db["people"]

person = {
  "name": {
    "first": "Fred",
    "last": "Flintstone"
  },
  "age": 36,
  "email": "fred.flintstone@example.com",
  "address": {
    "street": "123 Main St",
    "city": "Bedrock",
    "state": "CA",
    "zip": "98765"
  },
  "phone": [
    {
      "type": "home",
      "number": "707-555-1234"
    },
    {
      "type": "work",
      "number": "707-555-5678"
    }
  ]
}

response = collection.insert_one(person)

pprint(response)
