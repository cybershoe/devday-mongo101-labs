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

## Retrieving multiple documents

Much like `insert_one()`&mdash;which takes a single document&mdash;has its counterpart `insert_many()` that takes a list of document, `find_one()` also has a counterpart, `find()`, which returns a [cursor](https://www.mongodb.com/docs/manual/core/cursors/) instead of a single record. A cursor is an iterable object that allows you to process query results sequentially or in batches.

1. In VSCodium, open the file lab2-2/find.py and examine the code. Notice how this find operation looks a bit different than previous operations. Instead of simply outputting the response, we have this code:
  ```python
  for doc in response:
      pprint(doc['name'])
  ```
  What do you think the output of this program will be?

2. In the terminal window, change to the lab2-2 directory, and run the `find_one.py` program.
  ```bash
  cd ~/lab/lab2-2
  python find.py 
  ```

3. Observe the output:
  <details>
  <summary>Expected results</summary>
  
  `find()` will return a cursor to a set of all records where the `cuisine` field is equal to `Soups`. The `for:` loop will iterate over this cursor, and for each document returned, it will print out the `name` field of that record to the console.
  
  ```bash
  ubuntu@ip-10-0-1-219:~/lab/lab2-2$ python find.py
  'Wichcraft Express'
  'Original Soupman Of Staten Island'
  'The Original Soupman'
  'Peasant Stock'
  ubuntu@ip-10-0-1-219:~/lab/lab2-2$
  ```
  </details>

  4. 🎓 *Extra Credit*: Modify find.py to return a different type of cuisine. You can explore the collection in Compass to find other values that exist in the database. What do you think would happen if you specified a non-existent cuisine? What about lowercase `soups`?

When you are done, proceed to the next lab.