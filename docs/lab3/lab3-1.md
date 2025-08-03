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

  </details>


## Exclusion
You can retun all fields except for specific ones by giving the fields you want to exclude a value of "0" in the projection response. For example, to return all fields except for inspection grades, your projection document would be:
```python
{"grades": 0}
```

> [!NOTE]
> With the exception of excluding the `_id` field, you cannot combine inclusion and exclusion statements in projection documents.

