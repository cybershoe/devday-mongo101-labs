from pymongo import MongoClient
from os import getenv
from pprint import pprint
from datetime import datetime

MONGO_URI = getenv("MDB_URI")  # Don't worry about your connection string being in the code; it's set as an environment variable.

client = MongoClient(MONGO_URI)
db = client["sample_airbnb"]
collection = db["listingsAndReviews"]

last_review_date = datetime(2018, 1, 1)  # Example date for filtering documents

response = collection.delete_many() # Specify the filter for the documents you want to delete

pprint(response)