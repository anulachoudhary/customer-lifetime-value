Shutterfly
Code Challenge


## ASSUMPTIONS:
* Data is in JSON format
* Currency is in USD
* We will use US calendar weeks (Sunday to Saturday)
* 53rd week of previous year will be combined with 0th week of next year
* Solution leverages Python and SQL            

##PRE-REQUISITES:
* Coding in Python 3.0
* Data management in PostgreSQL

##LIBRARIES USED:
* SQLAlchemy
* Other typical Python libraries for date, JSON, etc


##CODE:
The source has two major parts: ETL and reporting. 
ETL has three parts: Extract, Transform and Load. 
There is a single function in reporting section. 
There is also a Data layer to talk to Postgres.

- extract.py
    - This is the first step - extract
    - In this step we will read provided input file for all events
    - In future we can read data from file or any other external source

- transform.py:
    - Confirm all mandatory fields (primary keys) are present.
    - In future more business validations can be added to this step.
    - In future false data can also be transformed (e.g. dates, city names, state names, etc)

- load.py:
    - This class will load data into data store.
    - This class will uses SQLAlchemy for pushing data into database.
    - We handle the custom logic of events coming out of order in this class.
    - When an order event for customer comes before the customer event,
      we create empty customer record (with nulls or empty data).
    - When a customer event comes, we first check if customer exists
      before creation to take care of scenario above.
    - We have a Fact table for weekly aggregates of site visits and expenditure per customer
      We have used buckets per week via key: YYYY-week_number

- data.py:
    - Connections to Postgres via SQLAlchemy
    - Basic data setup 

- report.py:
    - Analytical methods for reporting

##SQL:
* All sql code resides in *.sql files in 'src' folder.
* There is a file with all the SQL schema.
* There is also a SQL view to efficiently fetch weekly aggregated data for expenditure and visits. 
* Each event has a table
* There is a Fact table to aggregate weekly stats



##FUTURE CHALLENGES:
* data cleansing data needs more work
* handle edge cases 
* improve redundant checks if records exist - and leverage stored procedures 
* refactor code so that each event can have its own class, validation, etc. 
