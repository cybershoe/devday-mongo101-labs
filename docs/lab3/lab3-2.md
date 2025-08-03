# Multi-predicate queries

So far we have only been querying on individual fields; however, you can specify multiple fields in a query document. MongoDB will return only documents that match *all* predicates in the query filter.

1. Open the file lab3-2/multi-predicate.py. Note that the `find()` method has no arguments. Create a query that will return all restaurants in the Bronx that serve Greek cuisine.

  <details>
  <summary>Hint</summary>

  ```python
  {"borough": "Bronx", "cuisine": "Greek"}
  ```
  </details>

2. Run `multi_predicate.py` and check your results.

  <details>
  <summary>Expected result</summary>

  ```bash
  ubuntu@ip-10-0-1-116:~/lab/lab3-2$ python multi-predicate.py 
  'Gyro King'
  'Christos Gyro & Souvlaki'
  'Greek Express'
  'Gold Mine Cafe'
  ubuntu@ip-10-0-1-116:~/lab/lab3-2$
  ```
  </details>