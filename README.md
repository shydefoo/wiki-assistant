# wiki_assistant

UI endpoint: http://206.189.40.160/

Data can be downloaded at 


Tables currently loaded into MySQL db: 
* categorylinks
* page
* pagelinks
* revision

Example Query: 
```SELECT COUNT(*) FROM page;```

Example Category:
``` Microsoft```


Things to note:
* This query submitted has full access to the Database. Don't drop any of the tables or database
* Spent an excessive amount of time trying to upload data to database server. A simple source xx.sql throught the mysql
console could have done the trick but I went a big round trying to trigger the upload from the UI. 

Things to improve:
* Add extra user for executing input query from UI --> Grant privileges that are a subset of root privileges

