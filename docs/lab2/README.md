# Basic CRUD Operations

Now you've connected to your cluster, let's start working with documents. In these next labs, you'll learn how to create, read, update, and delete documents in MongoDB. This lab shows how to perform these CRUD operations in code, using the Python language-specific driver as an example. 

Python was chosen because it is well-known, and is very human-readable. The methods we will be using are not unique to the Python driver, but they may be named differently in different languages to match the naming conventions of those languages. For example, the `.insert_one()` method in PyMongo is called `.insertOne()` in mongosh/JavasScript, or `.InsertOne()` in .NET/C#, but they all perform the same function. Similarly, where PyMongo supports named parameters for additional options passed to its methods, in JavaScript (which lacks named parameters), those options are passed in an object that maps optional parameters to values. This is what is meant when we say our drivers are "idiomatic": they look and behave like other methods in the language for which they are written. You can find more details in the [MongoDB Documentation](https://www.mongodb.com/docs/drivers/) for your programming language of choice.

> [!NOTE]
> There won't be as many screenshots in this section for things like accessing Compass or opening lab files in VSCodium. Refer back to [lab 1](/lab1/) if you need a refresher.

> [!NOTE]
> You can complete most of this lab by copying and pasting commands and running the pre-written code in the lab folder; where changes to the code are required, the modified code will be provided. However, there are some steps marked as 🎓 *Extra Credit*. These are an opportunity to make changes to the code on your own and see how those changes affect the results. Don't be afriad to experiment!

