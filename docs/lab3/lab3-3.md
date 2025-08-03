# Querying within embedded documents

MongoDB is a document database. Unlike SQL databases, where one-to-one relationships are modelled using separate tables, documents can contain embedded documents, just like objects can contain nested objects. You can query on individual fields in embedded documents using dot notation, similarly to how other language represent nested properties of objects.

> [!NOTE]
> In mongosh and other JavaScript-like environments, you need to enclose object keys in quotes if they contain a dot character, even if you wouldn't need to otherwise.

Consider the `restaurant` collection: the `address` field is an embedded document, which contains multiple fields representing the restaurant's address. How could we find all restaurants in a particular zip code?

<details>
<summary>Hint</summary>

`zipcode` is a field in the `address` embedded document, so you can refer to that field directly as `"address.zipcode"`.
</details>

1. Open the file lab3-3/embedded.py. Modify the empty `find()` instruction with a query that will return all restaurants in the 11371 zip code.

  > [!TIP]
  > Remember that the `address.zipcode` field is a string field, even though it only contains numeric characters.

  <details>
  <summary>Hint</summary>

  ```python
  response = collection.find({"address.zipcode": "11371"})
  ```
  </details>

2. Run `embedded.py` and check your results.

  <details>
  <summary>Expected result</summary>
  
  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-2$ python multi-predicate.py 
  'Gyro King'
  'Christos Gyro & Souvlaki'
  'Greek Express'
  'Gold Mine Cafe'
  ubuntu@ip-10-0-1-116:~/lab/lab3-2$ cd ..
  ubuntu@ip-10-0-1-116:~/lab$ cd lab3-3
  ubuntu@ip-10-0-1-116:~/lab/lab3-3$ python embedded.py 
  'Terminal Cafe/Yankee Clipper'
  'Yankee Clipper'
  'Samuel Adams'
  'Go Natural'
  "Dunkin' Donuts"
  "Dunkin' Donuts, Baskin Robbins"
  'Figs'
  "Auntie Anne'S Pretzels"
  "Auntie Anne'S Pretzels"
  'Five Guys Burgers And Fries'
  'Maple Leaf Lounge'
  'Fix Coffee & Bakery'
  'Empire Tavern'
  'Cotto Market-Gate C30'
  'Cibo Express-Main'
  'Us Airways Club'
  'Voyage'
  'Villa Italian Kitchen'
  "Harry'S Deli"
  'Wibar'
  'Piccolo  Mercato'
  ubuntu@ip-10-0-1-116:~/lab/lab3-3$ 
  ```
  </details>

  🎓 *Extra Credit*: Looking at the results, can you guess where zip code 11371 is? Modify `embedded.py` to find a hamburger while waiting for your flight and check your results.