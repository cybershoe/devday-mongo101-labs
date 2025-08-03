from pymongo import MongoClient
from os import getenv
from pprint import pprint

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["sample_airbnb"]
collection = db["listingsAndReviews"]

response = collection.delete_one() # Specify the filter for the document you want to delete

pprint(response)