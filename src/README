SHUTTERFLY
Code Challenge


Your source files reside in this directory

ASSUMPTIONS:
Data is in JSON format
Currency is in USD


PERQUISITES:
Coding in Python 3.0
Data management in PostgreSQL

LIBRARIES USED:
json
dateutil.parser


CODE:
I have divided my code into three parts (ETL) : Extract, Transform and Load.
- extract.py
    - This is the first step - extract
    - In this step we will read provided input file for all events
    - In future we can read data from file or any other external source

- Load:
    - This class will load data into data store.
    - This class will uses SQLAlchemy for pushing data into database.
    - We handle the custom logic of events coming out of order in this class.
    - When an order event for customer comes before the customer event,
      we create empty customer record (with nulls or empty data).
    - When a customer event comes, we first check if customer exists
      before creation to take care of scenario above.

- Transform:
    - Confirm all mandatory fields (primary keys) are present.
    - In future more business validations can be added to this step.
    - In future false data can also be transformed (e.g. dates, city names, state names, etc)

SQL:
All sql code resides in *.sql files in 'src' folder.
There is 1 file for creating objects and another file to populate data.
I am not calling SQL filed from python file because we create DB objects once
and there is no point keep checking their existence before every execution

TEST CASES:


FUTURE CHALLENGES:
data cleansing data needs more work
Methodology to parse bad splitters and ignore them is needed.