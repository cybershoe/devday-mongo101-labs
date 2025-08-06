# Query operators

So far we have only been matching on equality. To query based on ranges, by exclusion, or by combinations of criteria, MongoDB supports a wide range of [query operators](https://www.mongodb.com/docs/manual/reference/operator/query/) for inequalities, logical AND and OR, element existence or type, and more. We'll go over a few examples here.

## Using a query operator
<h5><span style="color:#1c00ff">{ age: </span><span style="color:#ff0000">{ $gte: </span><span style="color:#04a200">42</span><span style="color:#ff0000"> }</span><span style="color:#1c00ff"> }</span></h5>

- <span style="color:#1c00ff">age</span>: The field to evaluate
- <span style="color:#ff0000">$gte</span>: The operator to evaluate this field with
- <span style="color:#04a200">42</span>: The argument(s) for the operator. An operator may take a scalar value, an array, or a document of multiple parameters.

## Searching for an inequality

MongoDB has 6 primary scalar comparison operators:

| Operator | Meaning                  |
|:--------:|--------------------------|
| $eq      | Equal to                 |
| $ne      | Not equal to             |
| $gt      | Greater than             |
| $gte     | Greater than or equal to |
| $lte     | Less than or equal to    |
| $lt      | Less than                |

1. Open Compass and navigate to the `restaurants` collection in the `sample_restaurants` database, if you haven't already done so.

2. Examine the query below. What do you think will be returned by this query? Run it and check your results.

  ```js
  {"grades.date": {$gte: ISODate('2015-01-01')}}
  ```

  <details>
  <summary>Expected results:</summary>

  This query should return the 2135 restaurants that have had at least one inspection since January 1, 2015.
  </details>

## Searching for a range

Query operators can be combined; all operators must evaluate to true in order for the document to match. We can use this to create a range.

1. Modify the query from the previous exercise to match all restaurants that were inspected in November 2014. Run the query and check your results.

  > [!TIP]
  > When searching for a range, consider whether you want to include the start and end of your range in your results when choosing between `$gte`/`$lte` and `$gt`/`$lt`.

  <details>
  <summary>Hint</summary>

  ```js
  {"grades.date": {$gte: ISODate('2014-11-01'), $lt: ISODate('2014-12-01')}}
  ```
  </details>

  <details>
  <summary>Expected result</summary>

  The query should return all 6319 restaurants that were inspected in November, 2014. If your query returned more, you are including dates outside of the intended search range.
  </details>

## Negation

The `$not` operator inverts the result of a query predicate. This is useful for excluding results that match a particular criteria. 

1. Create a query using the `$not` operator that will return all pizza restaurants in Manhattan that have *never* received a "C" rating. Run it and check your results.

  > [!TIP]
  > The `$not` operator inverts another operator, not a scalar value. What comparison operator might you use to match "C" ratings?

  <details>
  <summary>Hint</summary>

  ```js
  {borough: "Manhattan", cuisine: "Pizza", "grades.grade": {$not: {$eq: "C"}}}
  ```
  </details>

  <details>
  <summary>Expected results</summary>

  There are 295 pizza joints in Manhattan that have never received a "C" rating. 
  </details>

  🎓 *Extra credit*: The point of this exercise was to use the `$not` operator, but there is another, more concise way to get the same result, can you figure it out?
