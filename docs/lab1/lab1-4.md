# Connecting with language-specifc drivers (Python)

## Language-specific drivers
MongoDB provides [native drivers](https://www.mongodb.com/docs/drivers/) 
for all modern programming languages, and some less-modern ones too. These 
drivers are idiomatic to their languages, i.e.: they implement the classes,
methods, and helpers needed to interact with MongoDB in a way that matches the
style and conventions of the particular programming language for which they
are written. This is in contrast to most relational databases, which require a
different language (i.e.: SQL) to describe database operations.

## The Python driver
The official MongoDB Python driver is called 
[PyMongo](https://www.mongodb.com/docs/languages/python/). You may have heard
of another driver, motor, used for async Python. Motor is now deprecated in
favour of the PyMongo Async API now included in PyMongo. Some classes you will
interact with include:

- `pymongo.MongoClient`/`pymongo.AsyncMongoClient`: The client instance that 
  connects to a MongoDB cluster
- `pymongo.database.Database`: An instance of a database
- `pymongo.collection.Collection`: A colletion in a database
- `pymongo.cursor.Cursor`: An iterable cursor returned by database operations

## LAB: Connect with PyMongo

1. On your jumphost, double-click the "VSCodium" icon on your desktop.
![Desktop showing the VSCodium Icon](images/vscodium-icon.png)

> 👆 **Note**: [VSCodium](https://vscodium.com/) is an open-source binary build
  of [vscode](https://github.com/Microsoft/vscode).

