SHUTTERFLY
Code Challenge


ASSUMPTIONS:
Data is in JSON format
Currency is in USD
We will use US calendar weeks (Sunday to Saturday)
53rd week of previous year will be combined with 0th week of next year
Solution leverages Python and SQL            

PERQUISITES:
Coding in Python 3.0
Data management in PostgreSQL

LIBRARIES USED:
SQLAlchemy
Other Python libraries


CODE:
I have divided my code into three parts (ETL) : Extract, Transform and Load.
- extract.py
    - This is the first step - extract
    - In this step we will read provided input file for all events
    - In future we can read data from file or any other external source

- Transform:
    - Confirm all mandatory fields (primary keys) are present.
    - In future more business validations can be added to this step.
    - In future false data can also be transformed (e.g. dates, city names, state names, etc)

- Load:
    - This class will load data into data store.
    - This class will uses SQLAlchemy for pushing data into database.
    - We handle the custom logic of events coming out of order in this class.
    - When an order event for customer comes before the customer event,
      we create empty customer record (with nulls or empty data).
    - When a customer event comes, we first check if customer exists
      before creation to take care of scenario above.
    - We have a Fact table for weekly aggregates of site visits and expenditure per customer
      We have used buckets per week via key: YYYY-week_number


SQL:
All sql code resides in *.sql files in 'src' folder.
There is a file with all the SQL schema.
There is also a SQL view to efficiently fetch weekly aggregated data for expenditure and visits. 



FUTURE CHALLENGES:
data cleansing data needs more work
handle edge cases 
improve redundant checks if records exist - and leverage stored procedures 
refactor code so that each event can have its own class, validation, etc. 
