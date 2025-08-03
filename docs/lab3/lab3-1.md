# Projections

[Projection](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/) restrict the fields returned in a query to only include relevant information. The projection argument is a document (e.g.: dict), where the keys correspond to fields to either include or exclude from the results. 

## Inclusion
You can return only specific fields by giving the fields you want to include a value of "1" in the projection document. For example, in the `restaurants` collection in the `sample_restaurants` database, to include only the object ID, name and address in a response, your projection document would be:
```python
{"name": 1, "address": 1}
```
> [!NOTE]
> The `_id` field is always included, unless explicitly excluded.

1. In VSCodium, open the file lab3-1/include_fields.py and examine the code. The query in the `find_one()` instruction is the same as the one from lab 2-2, but we've added a projection document. What do you expect to see as the output?

2. In the terminal window, change to the lab1-1 directory, and run the `include_fields.py` program.

  <details>
  <summary>Expected results</summary>

  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ python include_fields.py 
  {'_id': ObjectId('5eb3d668b31de5d588f42930'),
  'address': {'building': '8825',
              'coord': [-73.8803827, 40.7643124],
              'street': 'Astoria Boulevard',
              'zipcode': '11369'},
  'name': 'Brunos On The Boulevard'}
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$
  ```
  </details>

3. Modify the projection to also include the `cuisine` field. Re-run `include_fields.py` and check your results.
  <details>
  <summary>Expected results</summary>

  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ python include_fields.py 
  {'_id': ObjectId('5eb3d668b31de5d588f42930'),
  'address': {'building': '8825',
              'coord': [-73.8803827, 40.7643124],
              'street': 'Astoria Boulevard',
              'zipcode': '11369'},
  'cuisine': 'American',
  'name': 'Brunos On The Boulevard'}
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$
  ```
  </details>

## Exclusion
You can retun all fields except for specific ones by giving the fields you want to exclude a value of "0" in the projection response. For example, to return all fields except for inspection grades, your projection document would be:
```python
{"grades": 0}
```

> [!NOTE]
> With the exception of excluding the `_id` field, you cannot combine inclusion and exclusion statements in projection documents.

1. Open the file lab3-1/exclude_fields.py and examine the code. What do you expect to see as the output?

2. Run the `exclude_fields.py` program and observe the output.
  <details>
  <summary>Expected results</summary>

  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ python exclude_fields.py 
  {'_id': ObjectId('5eb3d668b31de5d588f42930'),
  'address': {'building': '8825',
              'coord': [-73.8803827, 40.7643124],
              'street': 'Astoria Boulevard',
              'zipcode': '11369'},
  'borough': 'Queens',
  'cuisine': 'American',
  'name': 'Brunos On The Boulevard',
  'restaurant_id': '40356151'}
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ 
  ```
  </details>
3. Modify `exclude_fields.py` to also exclude the `_id` and `restaurant_id` fields. Re-run `exclude_fields.py` and check your results.
  <details>
  <summary>Expected results</summary>

  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ python exclude_fields.py 
  {'_id': ObjectId('5eb3d668b31de5d588f42930'),
  'address': {'building': '8825',
              'coord': [-73.8803827, 40.7643124],
              'street': 'Astoria Boulevard',
              'zipcode': '11369'},
  'borough': 'Queens',
  'cuisine': 'American',
  'name': 'Brunos On The Boulevard',
  'restaurant_id': '40356151'}
  ubuntu@ip-10-0-1-116:~/lab/lab3-1$ 
  ```
  </details>

🎓 *Extra Credit*: Go back to `include_fields.py`, and modify it to only include the name, address, and cuisine fields, and *not* the `_id` field. Re-run `include_fields.py` and check your work.

When you are done, proceed to the next lab.