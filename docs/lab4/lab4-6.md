# $lookup (JOINs)

In MongoDB, JOINs are less necessary than they are in relational databases. The ability to embed nested documents and arrays into documents means that data that is used together is usually stored together. However, there are situations where it makes more sense to reference data rather than embed it. In those scenarios, we can use the `$lookup` operator to perform the equivalent of a left outer join on another collection in the same database.

For this example, we will be using a database with sample account data. For a given account, we will lookup the customer owning that account, and include fields from that record in our result.

1. Open Compass and navigate to the `accounts` collection in the `sample_analytics` database, and click on "Aggregations".

2. Click "Add Stage".

3. In the dropdown, select `$match`. The stage will pre-populate with placeholder stage definition.

4. Edit the `$match` stage definition to find the record where `account_id` is equal to `376846`.

  <details>
  <summary>Hint</summary>

  ```js
  {
    account_id: 376846
  }
  ```
  </details>

5. Click "Add Stage", and in the dropdown, select `$lookup`.

  The `$lookup` stage has 4 key fields:
   * `from`: the collection to join from
   * `localField`: the local field with the value to match in the foreign collection
   * `foreignField`: the field in the foreign collection to match against the local field value
   * `as`: the field for the results.

6. Modify the `$lookup` stage to join from the `customers` collection, finding records where the local `account_id` field matches a value in the `accounts` array in the foreign collection, and put the result in the `customer` field.
  <details>
  <summary>Hint</summary>

  ```js
  {
    from: "customers",
    localField: "account_id",
    foreignField: "accounts",
    as: "customer"
  }
  ```
  </details>

7. Look at the results in the preview.
  <details>
  <summary>Expected Results</summary>

  The output document now has an additional `customer` field, which is an array with one element containing the customer record from the `customers` table.

  ```js
  {
    "_id": {...},
    "account_id": 376846,
    "limit": 10000,
    "products": [...],
    "customer": [
      {
        "_id": {...},
        "username": "millerrenee",
        "name": "Joshua Parker",
        "address": "932 Jeremy Springs Suite 144\nJohnmouth, NM 02561",
        "birthdate": {...},
        "email": "nicoleanderson@hotmail.com",
        "accounts": [...],
        "tier_and_details": {}
      }
    ]
  }
  ```

  > [!NOTE]
  > The customer field is an array; accounts to customers is a many-to-one relationship, but a `$lookup` can be on a one-to-many or many-to-many relationship, and more than one document may be returned from the foreign collection.

  </details>

When you are done, stay on this screen and proceed to the next lab.
