# Aggregations

One of the more powerful tools available in MongoDB for real-time analytics is the [aggregation pipeline](https://www.mongodb.com/docs/manual/core/aggregation-pipeline/). MongoDB aggregations are a series of stages, which allow you to procedurally match, sort, aggregate, project, and transform data in a logical, step-by-step process, with the output of each stage feeding into the next. The result is a highly flexible and maintainable framework for real-time data analytics.


We will be working mostly in Compass, as the GUI makes it easier to visualize how a pipeline get built; however, the resulting pipeline is expressed a JSON object, which makes it simple to programmatically create or compose a pipeline in code.
