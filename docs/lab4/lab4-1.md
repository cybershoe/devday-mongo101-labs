# Projections

Notice that we included a [projection](https://www.mongodb.com/docs/manual/tutorial/project-fields-from-query-results/) argument in the `find_one()` instruction above. Projections restrict the fields returned in a query to only include relevant information. The projection argument is a document (e.g.: dict), where the keys correspond to fields to either include or exclude from the results. 

## Inclusion
You can return only specific fields by giving the fields you want to include a value of "1" in the projection document. For example, to include only the object ID, name and address in a response, your projection document would be:
```python
{"name": 1, "address": 1}
```
> [!NOTE]
> The `_id` field is always included, unless explicitly excluded.

## Exclusion
You can retun all fields except for specific ones by giving the fields you want to exclude a value of "0" in the projection response. For example, to return all fields except for inspection grades, your projection document would be:
```python
{"grades": 0}
```

> [!NOTE]
> With the exception of excluding the `_id` field, you cannot combine inclusion and exclusion statements in projection documents.

1. In VSCodium, open the file lab2-2/include_fields.py and examine the code. 