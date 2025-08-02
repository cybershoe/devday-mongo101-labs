# Retrieving documents

In this section we'll be looking at retrieving data from MongoDB. We'll go over retreieving one or many documents, basic query syntax, and projection.

## Retrieving one document

1. In VSCodium, open the file lab2-2/find_one.py and examine the code. Note the `collection.find_one` instruction. `find_one()` is a collection method that takes a query filter as its first argument, and returns a single document if at least one documement matching the query filter exists in the collection, and returns `None` otherwise.

> [!TIP]
> The analagous mongosh/JavaScript method is `findOne()`

Read through the code of `find_one.py`. What do you expect to see on the console when you run it?

2. In the terminal window, change to the lab2-2 directory, and run the `find_one.py` program.
  ```bash
  cd ~/lab/lab2-2
  python find_one.py 
  ```

3. You should see the same restaurant details that you saw in lab 1-4. Note that the document comes back as a Python dict, with arrays and embedded fields. It is not necessary to rehydrate the original object from multuple flat tables.

4. 🎓 *Extra Credit*: Modify the code to find the restaurant named "Blue Bay Restaurant".
  <details>
  <summary>Solution:</summary>

  ```python
  response = collection.find_one({"name": "Blue Bay Restaurant"})
  ```
  </details>

## Projections

Notice that we included a [projection](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/) argument in the `find_one()` instruction above. Projections restrict the fields returned in a query to only include relevant information. The projection argument is a document (e.g.: dict), where the keys correspond to fields to either include or exclude from the results. 

### Inclusion
You can return only specific fields by giving the fields you want to include a value of "1" in the projection document. For example, to include only the object ID, name and address in a response, your projection document would be:
```python
{"name": 1, "address": 1}
```
> [!NOTE]
> The `_id` field is always included, unless explicitly excluded.

### Exclusion
You can retun all fields except for specific ones by giving the fields you want to exclude a value of "0" in the projection response. For example, to return all fields except for inspection grades, your projection document would be:
```python
{"grades": 0}
```

> [!NOTE]
> With the exception of excluding the `_id` field, you cannot combine inclusion and exclusion statements in projection documents.

1. In VSCodium, open the file lab2-2/include_fields.py and examine the code. 

## Retrieving multiple documents

Much like `insert_one()`&mdash;which takes a single document&mdash;has its counterpart `insert_many()` that takes a list of document, `find_one()` also has a counterpart, `find()`, which returns a [cursor](https://www.mongodb.com/docs/manual/core/cursors/) instead of a single record. A cursor is an iterable object that allows you to process query results sequentially or in batches.

1. In VSCodium, open the file lab2-2/find.py and examine the code. 
