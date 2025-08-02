from pymongo import MongoClient
from os import getenv
from pprint import pformat

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["lab2_db"]
collection = db["people"]

many_people = [
  {
    "name": {
      "first": "Homer",
      "last": "Simpson"
    },
    "age": 39,
    "email": "donutfan@example.com",
    "address": {
      "street": "742 Evergreen Terrace",
      "city": "Springfield",
      "state": "MU",
      "zip": "19981"
    },
    "phone": [
      {
        "type": "home",
        "number": "302-555-1337"
      },
      {
        "type": "work",
        "number": "888-555-4823",
        "extension": "1234"
      }
    ]
  },
  {
    "name": {
      "first": "Marge",
      "last": "Simpson"
    },
    "age": 38,
    "email": "pretzel_queen@example.com",
    "address": {
      "street": "742 Evergreen Terrace",
      "city": "Springfield",
      "state": "MU",
      "zip": "19981"
    },
    "phone": [
      {
        "type": "home",
        "number": "302-555-1337"
      }
    ]
  },
  {
    "name": {
      "first": "Montgomery",
      "last": "Burns"
    },
    "age": 119,
    "email": "excellent@example.com",
    "phone": [
      {
        "type": "work",
        "number": "888-555-4823",
        "extension": "1001"
      }
    ],
    "net_worth": 9999999999.99
  }
]

response = collection.insert_many(many_people)  # The objects are inserted directly with no mapping to flat tables

print(f"Acknowledged: {response.acknowledged}\nInserted _ids: \n{pformat(response.inserted_ids)}")
