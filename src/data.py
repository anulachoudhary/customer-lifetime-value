from sqlalchemy import create_engine, MetaData, Table, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import insert, select, update
import psycopg2



"""
This class establishes connection with Postgresql.
We first create DB and then use SQLAlchemy as data layer.
"""


class Customer(object):
    def __init__(self, key, valid_date, last_name, adr_city, adr_state):
        self.customer_id = key
        self.event_time = valid_date
        self.last_name = last_name
        self.adr_city = adr_city
        self.adr_state = adr_state


class SiteVisit(object):
    def __init__(self, page_id, event_time, customer_id, tags):
        self.page_id = page_id
        self.event_time = event_time
        self.customer_id = customer_id
        self.tags = tags

class Image(object):
    def __init__(self, image_id, event_time, customer_id):
        self.image_id = image_id
        self.event_time = event_time
        self.customer_id = customer_id


class Order(object):
    def __init__(self, order_id, event_time, customer_id, total_amount):
        self.order_id = order_id
        self.event_time = event_time
        self.customer_id = customer_id
        self.total_amount = total_amount


class WeeklyVisit(object):
    def __init__(self, week_id, customer_id, week_start, week_end, weekly_total):
        self.week_id = week_id
        self.customer_id = customer_id
        self.week_start = week_start
        self.week_end = week_end
        self.weekly_total = weekly_total


class TopCustomerLTV(object):
    def __init__(self, customer_id, average_weekly_review):
        self.customer_id = customer_id
        self.average_weekly_review = average_weekly_review


class Data:


    def __init__(self):
        pass


    def get_db_connection(self):
        engine = create_engine('postgresql://postgres:admin@localhost:5432/shutterfly_analytics')
        metadata = MetaData(engine)

        customer_table = Table('customer', metadata, autoload=True)
        image_table = Table('image_upload', metadata, autoload=True)
        site_visit_table = Table('site_visit', metadata, autoload=True)
        order_table = Table('order', metadata, autoload=True)
        weekly_visit_table = Table('weekly_visit', metadata, autoload=True)
        customer_ltv_view = Table('top_customer_ltv', metadata, Column('customer_id', String, primary_key=True), autoload=True)

        mapper(Customer, customer_table)
        mapper(Image, image_table)
        mapper(SiteVisit, site_visit_table)
        mapper(Order, order_table)
        mapper(WeeklyVisit, weekly_visit_table)

        mapper(TopCustomerLTV, customer_ltv_view)

        Session = sessionmaker(bind=engine)
        session = Session()

        return session
