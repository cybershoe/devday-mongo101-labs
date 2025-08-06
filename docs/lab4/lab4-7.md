# Transforming

We have the data we need, but also a lot that we don't need. In this last stage, we're going to cherry-pick fields to be returned, and replace our output document with this new document.

1. Click "Add Stage"

2. In the dropdown, select `$replaceRoot`. The stage will pre-populate with placeholder stage definition.

  `$replaceRoot`, as the name implies, replaces the root of the document with another document.

3. Modify the `$replaceRoot` stage definition to replace the document root with this new document:
  ```js
  {
    newRoot: {
      account: "$account_id",
      email: {$arrayElemAt: ["$customer.email", 0]},
      owner: {$arrayElemAt: ["$customer.name", 0]}
    }
  }
  ```

4. Switch to text mode and look at the resulting pipeline. Just like queries in Compass, you can export this pipeline to the language of your choice by clicking the "Export to Language" button.

  <details>
  <summary>Expected Results</summary>

  ```js
  [
    {
      $match:
        {
          account_id: 376846
        }
    },
    {
      $lookup:
        {
          from: "customers",
          localField: "account_id",
          foreignField: "accounts",
          as: "customer"
        }
    },
    {
      $replaceRoot:
        {
          newRoot: {
            account: "$account_id",
            email: {
              $arrayElemAt: ["$customer.email", 0]
            },
            owner: {
              $arrayElemAt: ["$customer.name", 0]
            }
          }
        }
    }
  ]
  ```
When you are done, proceed to the end of this lab.
