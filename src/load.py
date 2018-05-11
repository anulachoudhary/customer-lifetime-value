from src.data import Data, Customer, Image, SiteVisit, Order, WeeklyVisit
import datetime

"""
This class will load data into data store. 
This class will uses SQLAlchemy for pushing data into database.
We handle the custom logic of events coming out of order in this class. 
When an order event for customer comes before the customer event, we create 
empty customer record (with nulls or empty data). 
When a customer event comes, we first check if customer exists before creation 
to take care of scenario above. 
"""
class Load:

    db_session = None

    def __init__(self):
        data = Data()
        self.db_session = data.get_db_connection()


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


    def add_order_entry(self, key, event_time, customer_id, total_amount):

        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(key)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state feils
            customer = Customer(customer_id, datetime.datetime.now(), "", "")
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



            # If exists, then update
        # Else create



        # Now also update weekly table


    def add_site_visit_entry(self, key, event_time, customer_id, tags):
        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(key)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state fields
            customer = Customer(customer_id, datetime.datetime.now(), "", "")
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



    def add_image_entry(self, key, event_time, customer_id):
        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(key)
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

    def add_weekly_stats(self):
        # Based on date figure out which week it belongs
        # Query based on week date and for specific user
        # If record exists, read
        # Increment total
        # save again

        # There is customer_id FK.
        # First check if that customer exists, else create that customer
        # First check if customer with this key exists
        customer_record = self.db_session.query(Customer).get(key)
        if customer_record is None:
            # Create customer record with current event_time and empty adr_city and adr_state feils
            customer = Customer(customer_id, datetime.datetime.now(), "", "")
            self.db_session.add(customer)
            self.db_session.commit()


# if __name__ == "__main__":
#     session = loadSession()
#
#     rows = session.query(Customer).all()
#     print(rows[0].adr_city)
#
