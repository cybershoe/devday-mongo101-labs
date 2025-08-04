# Querying within arrays

In the last module we saw how we can query on fields that are inside of an embedded document. What about fields that are within an array? In this module we will look at different methods of querying against an embedded array.

We're going to look at a different collection for this example. The documents in the `customers` collection in the `sample_analytics` database contains an array of account numbers:

```js
{
  "_id":{...},
  "username":"fmiller",
  "name":"Elizabeth Ray",
  "address":"9286 Bethany Glens\nVasqueztown, CO 22939",
  "birthdate":{...},
  "email":"arroyocolton@gmail.com",
  "active":true,
  "accounts":[
    371138,
    324287,
    276528,
    332179,
    422649,
    387979
  ],
  "tier_and_details":{...}
}
```

## Matching a single array element

What if we wanted to find the customer with account numner `436090`?

1. Open Compass, if you haven't already done so, and navigate to the `customers` collection in the `sample_analytics` database.

2. Consider this query: 
  ```js
  {accounts: [436090]}
  ```

  What do you expect to happen when you run this query? Run it and see whether it returns the results you expect.

  <details>
  <summary>Expected results</summary>
  
  The query returns no results. Much like the embedded document in the previous lab, this is asking MongoDB to find documents where the `accounts` field is *exactly* equal to `[436090]`, i.e. and array with only that exact value. In this case, the customer has more than one account, so this query does not match their record.
  </details>

3. Create a query that will return any documents where the value `436090` appears in the `accounts` embedded array. Run the query and check your results.

  <details>
  <summary>Hint</summary>

  When you specify a scalar (i.e. a single value) to match against a field that contains an embedded array, MongoDB will return any documents where the array field *contains* that value. A matching query would be:

  ```js
  {accounts: 436090}
  ```
  </details>

  <details>
  <summary>Expected results</summary>

  ```js
    {
    "_id": {...},
    "username": "ashley97",
    "name": "James Smith",
    "address": "0511 Rice Fords\nWaynemouth, SD 28444",
    "birthdate": {...},
    "email": "kevin84@yahoo.com",
    "accounts": [
      725209,
      738462,
      57161,
      436090,
      714030
    ],
    "tier_and_details": {...}
  }
  ```

## Matching embedded documents in an array

You can combine array query syntax with dot notation to match on fields inside of an array of embedded documents.

1. Switch back to the `restaurants` collection in the `sample_restaurants` database. 

2. Create a query that will return any restraurant that were inspected on January 17, 2015. Run the query and check your results.

  > [TIP]
  > The `ISODate()` helper lets you use an ISO-8601 string representation of a date to query against values of the BSON type `Date`.

  <details>
  <summary>Hint</summary>

  ```js
  {"grades.date": ISODate('2015-01-17')}
  ```
  </details>

  <details>
  <summary>Expected results</summary>
  The query should return all 17 restaurants that were inspected on January 17, 2015:
  
  ```
  "Cafe Un Deux Trois"
  "Trattoria Alba"
  "Mcdonald'S"
  "Albion"
  "Cock'S Bajan Restaurant"
  "Il Sapore Italiano Pizzeria"
  "New Fat Cheng"
  "Sweet Afton"
  "Dunkin Donuts"
  "Mcdonalds"
  "Little Caesars"
  "Little Italy Pizza/Papaya Dog"
  "Bell Diner"
  "Peachwave"
  "New Giant Chinese Food"
  "Crown Fried Chicken And Pizza"
  "George And Jacks"
  ```