from pymongo import MongoClient
from os import getenv
from pprint import pprint

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["sample_mflix"]
collection = db["movies"]

filter={
    'countries': 'Canada'
}

project={
    'title': 1, 
    'released': 1, 
    '_id': -1
}

sort=list({
    'released': -1
}.items())

limit=3

result = collection.find(
  filter=filter,
  projection=project,
  sort=sort,
  limit=limit
)