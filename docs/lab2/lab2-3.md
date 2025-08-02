# Updating documents

So far we have only inserted documents. What if you want to make a change to an existing document?

## Repeated inserts

To see what *not* to do, let's try just repeating the same insert with the updated data.

1. In VSCodium, open the file lab2-3/insert_book.py and examine the code. This should be familiar; it inserts a record into the "books" collection, creating the collection if it doesn't already exist.

2. In the terminal window, change to the lab2-3 directory, and run the `insert_book.py` program.
  ```bash
  cd ~/lab/lab2-3
  python insert_book.py 
  ```

3. Make a note of the ObjectID returned by the call to `insert_one()`. Open Compass, navigate to the "lab2_db" database, and the "books" collection.

4. Inspect the document in the books collection. There is an error in this document: The Great Gatsby was written by F. Scott Fitzgerald, not F. Steve Fitzgerald.

5. Make a copy of the `insert_book.py` called `insert_book_again.py`:
  ```bash
  cp insert_book.py insert_book_again.py
  ```

6. Open `insert_book_again.py`, and correct the `book` object to show the proper author's first name, F. Scott. Save the file, either by pressing <kbd>Ctrl</kbd>+<kbd>S</kbd> or navigating to File -> Save.

7. Run the `insert_book_again.py` program and note the output. You should get a different ObjectID.

8. Look at your collection in Compass. You'll see that both versions of the document have been inserted; the original document was not corrected.

9. Run `reset.py` to drop the books collection before the next steps.
  ```bash
  python reset.py
  ```

## Replacing a document

As you saw, re-running the insert simply created a new document. To replace an existing document, we use the `replace_one()` method. This method takes a query filter *and* a document to update. It first finds a document matching the query predicate, and replaces it with the new document.

> [!NOTE]
> The mongosh/JavaScript equivalent method is replaceOne()

1. In the terminal, run the `insert_book.py` program again, to insert the book back into the database. Make a note of the inserted _id.
  ```bash
  python insert_book.py 
  ```

2. Open the `replace_book.py` program, and look at the code. You'll see that the `collection.insert_one()` instruction has been replaced by `collection.replace_one`. 

3. Replace the `"your object _id here"` string literal with the object `_id` from `insert_book.py` and save the file.
  > [!TIP]
  > Remember, to copy from the terminal, the key combination is <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd>, to paste into VSCodium is <kbd>Ctrl</kbd>+<kbd>V</kbd>, and to save the file is <kbd>Ctrl</kbd>+<kbd>S</kbd>

  > [!NOTE]
  > We're using the `_id` of the document as the filter condition because it is guaranteed to be unique. We don't need to do this, you can use any query filter that will return the correct record; however, since `replace_one()` only replaces one document, even if more than one match the query filter, using a unique key ensures that we replace the document that we intend to.

4. Run `replace_book.py` and observe the output.
  <details>
  <summary>Expected results</summary>

  `replace_one()` returns an object with, amongst other properties, the write acknowledgement, the number of documents that matched the query filter, and the number of documents modified by the operation.

  ```bash
  ubuntu@ip-10-0-1-219:~/lab/lab2-3$ python replace_book.py 
  Acknowledged: True
  Documents matched: 1
  Documents modified: 1
  ubuntu@ip-10-0-1-219:~/lab/lab2-3$
  ```
  </details>

5. Look at your collection in Compass: note that the document has been updated in place, and it still has the same `_id`.

## Upserts

What if you want only one instance of a document in your collection, but you don't know whether it already exists? The `upsert` argument to `replace_one()` instructs MongoDB to perform an upsert: if a document matching the query filter exists, it is updated in place; if it doesn't exist, it is created with the contents of the replacement document.

1. Open the `upsert_book.py` program and examine the code. What do you expect to happen when this program is run for the first time?

2. Run `upsert_book.py` and observe the output.

<details>
  <summary>Expected results</summary>

  Because `replace_one()` is looking for a document where `title` is equal to `"War and Peace"`. and no such document exists, it does not modify the collection.

  ```bash
  ubuntu@ip-10-0-1-219:~/lab/lab2-3$ python replace_book.py 
  Acknowledged: True
  Documents matched: 0
  Documents modified: 0
  ubuntu@ip-10-0-1-219:~/lab/lab2-3$
  ```
  </details>
