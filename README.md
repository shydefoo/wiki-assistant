# wiki_assistant

Data can be downloaded here at : https://dumps.wikimedia.org/simplewiki/20181120/
categorylinks - sql  simplewiki-20181120-categorylinks.sql.gz
page - sql  simplewiki-20181120-page.sql.gz
pagelinks - sql simplewiki-20181120-pagelinks.sql.gz
revision - xml simplewiki-20181120-stub-meta-current.xml.gz


Tables currently loaded into MySQL db: 
* categorylinks
* page
* pagelinks
* revision

Example Query: 
```SELECT COUNT(*) FROM page;```

Example Category:
``` Microsoft```

* SQL code contains predefined table schema. Easy to upload via python mysql-connector
* xml code had to be parsed using mw_dm.py script to generate sql code for revision data

Deployment:
* MySQL db 5.7.24 used, instantiated using docker swarm for easy deployment on Digital Ocean Droplet.
* Simple HTML UI calling Flask endpoints. 
* 2 services in Docker stack - Webapp service and DB service
* Given time constraint, no restrictions put in place for query.


Approach taken:
* Used SQL dumps provided by wiki to load into MySql db. Simplest approach, Sql dumps stored in /data folder (create folder if folder doesn’t exist)
* Functions used to run sql scripts through python-connect api located in folder db_setup/load_sql_scripts.py
* 2 services exposed via endpoints (Run query, Search outdated page by category)
* Each service extends a base service which provides basic functionality to display results in the same format
* Results returned in the form of a table after submitting input


Requirements:

UI for user to key in sql query 
* In the interest of time, I didn’t put in any checks on the sql query (eg. To limit only select statements)
* Query will run as long as there are no syntax errors
Steps taken:
* Pass query as form to web app. App will run query and pass results back 

Outdated page for a given category:
* Category needs to match letter for letter. 
* Results are displayed in a table on the next page + time taken for query to run
Steps taken:
* Given category, search for page_id’s that fall into category using categorylinks table
* find links in page_id’s using pagelinks table
* get timestamp of page links using revision table
* get timestamp of original page_ids using revision table
* Get largest timestamp difference between each original page_id and its associated pagelinks 
* Get largest timestamp difference amongst original page_ids —> most outdated page given category
* Do all this while taking advantage of indexes of each table (Speeds up query)
* Return result

Common steps shared between 2 services:
* Results are rendered dynamically into a table using Flask-Table
* Time taken for query to complete is measured

Things to note:
* This query submitted has full access to the Database. Don't drop any of the tables or database
* Spent an excessive amount of time trying to upload data to database server. A simple source xx.sql through the mysql
console could have done the trick but I went a big round trying to trigger the upload from the UI (which I eventually took out)

Things to improve:
* Add extra user for executing input query from UI --> Grant privileges that are a subset of root privileges
