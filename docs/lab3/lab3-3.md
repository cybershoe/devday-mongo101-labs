# Querying within embedded documents

MongoDB is a document database. Unlike SQL databases, where one-to-one relationships are modelled using separate tables, documents can contain embedded documents, just like objects can contain nested objects. You can query on individual fields in embedded documents using dot notation, similarly to how other language represent nested properties of objects.

> [!NOTE]
> In mongosh and other JavaScript-like environments, you need to enclose object keys in quotes if they contain a dot character, even if you wouldn't need to otherwise.

Consider the `restaurant` collection: the `address` field is an embedded document, which contains multiple fields representing the restaurant's address. How could we find all restaurants in a particular zip code?

<details>
<summary>Hint</summary>

`zipcode` is a field in the `address` embedded document, so you can refer to that field directly as `"address.zipcode"`.
</details>

1. Open Compass and navigate to the `restaurants` collection in the `sample_restaurants` database, if you haven't already done so.

2. Create a query that will return all restaurants in the 11371 zip code. Run the query and check your results.

  > [!TIP]
  > Remember your quotes! The field name is in dot notation, and the `address.zipcode` field is a string field, even though it only contains numeric characters. Both the key and value need to be quoted.

  <details>
  <summary>Hint</summary>

  ```js
  {"address.zipcode": "11371"}
  ```
  </details>

2. Run `embedded.py` and check your results.

  <details>
  <summary>Expected result</summary>
  
  21 documents:
  ```js
  [
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Terminal Cafe/Yankee Clipper",
      "restaurant_id": "40364262"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Yankee Clipper",
      "restaurant_id": "40379994"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Bottled beverages, including water, sodas, juices, etc.",
      "grades": [...],
      "name": "Samuel Adams",
      "restaurant_id": "41117836"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Sandwiches",
      "grades": [...],
      "name": "Go Natural",
      "restaurant_id": "41117842"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Donuts",
      "grades": [...],
      "name": "Dunkin' Donuts",
      "restaurant_id": "41142675"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Donuts",
      "grades": [...],
      "name": "Dunkin' Donuts, Baskin Robbins",
      "restaurant_id": "41142665"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Figs",
      "restaurant_id": "41187508"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Bagels/Pretzels",
      "grades": [...],
      "name": "Auntie Anne'S Pretzels",
      "restaurant_id": "41235116"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Bagels/Pretzels",
      "grades": [...],
      "name": "Auntie Anne'S Pretzels",
      "restaurant_id": "41235119"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Hamburgers",
      "grades": [...],
      "name": "Five Guys Burgers And Fries",
      "restaurant_id": "41481310"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Maple Leaf Lounge",
      "restaurant_id": "41619912"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Café/Coffee/Tea",
      "grades": [...],
      "name": "Fix Coffee & Bakery",
      "restaurant_id": "41645303"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Empire Tavern",
      "restaurant_id": "41693597"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Bakery",
      "grades": [...],
      "name": "Cotto Market-Gate C30",
      "restaurant_id": "41693601"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Cibo Express-Main",
      "restaurant_id": "41693614"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Us Airways Club",
      "restaurant_id": "41721588"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "American",
      "grades": [...],
      "name": "Voyage",
      "restaurant_id": "50003888"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Italian",
      "grades": [...],
      "name": "Villa Italian Kitchen",
      "restaurant_id": "50014290"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Jewish/Kosher",
      "grades": [...],
      "name": "Harry'S Deli",
      "restaurant_id": "50017147"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Other",
      "grades": [...],
      "name": "Wibar",
      "restaurant_id": "50016849"
    },
    {
      "_id": {...},
      "address": {...},
      "borough": "Queens",
      "cuisine": "Other",
      "grades": [...],
      "name": "Piccolo  Mercato",
      "restaurant_id": "50018798"
    },
  ]
  ```
  </details>

  🎓 *Extra Credit*: Looking at the results, can you guess where zip code 11371 is? Modify `embedded.py` to find a hamburger while waiting for your flight and check your results.

When you are done, proceed to the next lab.