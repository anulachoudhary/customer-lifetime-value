from src.data import Data, Customer, Image, SiteVisit, Order, WeeklyVisit, TopCustomerLTV
import datetime

"""
This class will load data into data store. 
This class will uses SQLAlchemy for pushing data into database.
We handle the custom logic of events coming out of order in this class. 
When an order event for customer comes before the customer event, we create 
empty customer record (with nulls or empty data). 
When a customer event comes, we first check if customer exists before creation 
to take care of scenario above. 

We have a Fact table for weekly aggregates of site visits and expenditure per customer
We have used buckets per week via key: YYYY-week_number
"""
class Load:

    db_session = None
    data = None

    def __init__(self):
        self.data = Data()
        self.db_session = self.data.get_db_connection()

    """
    Check and insert/update customer record
    """
    def add_customer_entry(self, key, event_time, last_name, adr_city, adr_state):
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(key)

        if customer_record is not None:
            # Exists, hence update
            customer_record.event_time = event_time
            customer_record.last_name = last_name
            customer_record.adr_city = adr_city
            customer_record.adr_state = adr_state

            self.db_session.commit()

        else:
        # Create
            customer = Customer(key, event_time, last_name, 'RWC', adr_state)
            self.db_session.add(customer)
            self.db_session.commit()

    """
    Check and insert/update order entry
    Once an order is entered we also enter a record in weekly_visit table to capture aggregates
    Key to weekly_visit table is combination of year+week number
    """
    def add_order_entry(self, key, event_time, customer_id, total_amount, weekly_visit_key):

        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(customer_id)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state feils
            customer = Customer(customer_id, datetime.datetime.now(), "", "", "")
            self.db_session.add(customer)
            self.db_session.commit()

        order_record = self.db_session.query(Order).get(key)
        # Check if this order id exists
        # Update the record
        if order_record is not None:
            # Exists, hence update
            order_record.event_time = event_time
            order_record.customer_id = customer_id
            order_record.total_amount = total_amount

            self.db_session.commit()

        else:
            # Create
            order = Order(key, event_time, customer_id, total_amount)
            self.db_session.add(order)
            self.db_session.commit()

        # Now also update weekly table and update weekly_total
        # First get value for weekly_visit_key & customer_id
        weekly_visit_record = self.db_session.query(WeeklyVisit).filter(WeeklyVisit.customer_id == customer_id, WeeklyVisit.week_id == weekly_visit_key).first()
        # If exists, add to weekly_total
        if weekly_visit_record is not None:
            temp_total = float(weekly_visit_record.weekly_total) + float(total_amount)
            weekly_visit_record.weekly_total = str(temp_total)

            self.db_session.commit()

        else:
            # Create
            weekly_visit_record = WeeklyVisit(weekly_visit_key, customer_id, week_start=None, week_end=None, weekly_total=total_amount)
            self.db_session.add(weekly_visit_record)
            self.db_session.commit()


    """
    Check and insert/update visit entry
    Once a visit is entered we also enter a record in weekly_visit table to capture aggregates
    We simply increment number of visits
    Key to weekly_visit table is combination of year+week number
    """
    def add_site_visit_entry(self, key, event_time, customer_id, tags, weekly_visit_key):
        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(customer_id)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state fields
            customer = Customer(customer_id, datetime.datetime.now(), "", "", "")
            self.db_session.add(customer)
            self.db_session.commit()

        page_records = self.db_session.query(SiteVisit).get(key)

        # Check if this order id exists
        # Update the record
        if page_records is not None:
            # Exists, hence update
            page_records.event_time = event_time
            page_records.customer_id = customer_id
            page_records.tags = tags

            self.db_session.commit()

        else:
            # Create
            page = SiteVisit(key, event_time, customer_id, tags)
            self.db_session.add(page)
            self.db_session.commit()

        # Now also update weekly table and update visit count
        # First get value for weekly_visit_key & customer_id
        weekly_visit_record = self.db_session.query(WeeklyVisit).filter(WeeklyVisit.customer_id == customer_id, WeeklyVisit.week_id == weekly_visit_key).first()
        # If exists, add to weekly visits
        if weekly_visit_record is not None:
            weekly_visit_record.weekly_visits += 1

            self.db_session.commit()

        else:
            # Create
            weekly_visit_record = WeeklyVisit(weekly_visit_key, customer_id, week_start=None, week_end=None, weekly_total=0, weekly_visits=1)
            self.db_session.add(weekly_visit_record)
            self.db_session.commit()


    """
    Check and insert/update record in image
    """
    def add_image_entry(self, key, event_time, customer_id):
        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(customer_id)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state feils
            customer = Customer(customer_id, datetime.datetime.now(), "", "")
            self.db_session.add(customer)
            self.db_session.commit()

        image_record = self.db_session.query(Image).get(key)

        # Check if this order id exists
        # Update the record
        if image_record is not None:
            # Exists, hence update
            image_record.event_time = event_time
            image_record.customer_id = customer_id

            self.db_session.commit()

        else:
            # Create
            image = Image(key, event_time, customer_id)
            self.db_session.add(image)
            self.db_session.commit()

    # def add_weekly_stats(self):
    #     # Based on date figure out which week it belongs
    #     # Query based on week date and for specific user
    #     # If record exists, read
    #     # Increment total
    #     # save again
    #
    #     # There is customer_id FK.
    #     # First check if that customer exists, else create that customer
    #     # First check if customer with this key exists
    #     customer_record = self.db_session.query(Customer).get(key)
    #     if customer_record is None:
    #         # Create customer record with current event_time and empty adr_city and adr_state feils
    #         customer = Customer(customer_id, datetime.datetime.now(), "", "")
    #         self.db_session.add(customer)
    #         self.db_session.commit()


    """
    Query an existing View to get Top LTV customers
    """
    def get_top_customer_ltv(self, x):
        # Get data from view
        top_customer_view = self.db_session.query(TopCustomerLTV).limit(x).all()

        return top_customer_view
