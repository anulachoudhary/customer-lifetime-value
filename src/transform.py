import json
import dateutil.parser
from src.load import Load



class Transform:

    loader = None

    def __init__(self):
        self.loader = Load()


    """
    Confirm all mandatory fields of Customer 
    In future more business validations can be added to this step
    In future false data can also be transformed (e.g. dates, city names, 
    state names, etc) 
    """
    def transform_before_loading_customer(self, dic):
        # validate
        verb = dic.get("verb", None)
        key = dic.get("key", "")
        event_time = dic.get("event_time", None)
        last_name = dic.get("last_name", "")
        adr_city = dic.get("adr_city", "")
        adr_state = dic.get("adr_state", "")

        if verb not in ("NEW", "UPDATE"):
            print("Invalid event in customer event_type!")
            return

        if key is "":
            print("Invalid key in customer!")
            return

        try:
            valid_date = dateutil.parser.parse(event_time)
        except ValueError:
            print("Invalid Date in customer event_type!!")
            return

        # Insert into DB
        self.loader.add_customer_entry(key, valid_date, last_name, adr_city, adr_state)

    """
    Confirm all mandatory fields of site_visit event
    In future more business validations can be added to this step
    In future false data can also be transformed (e.g. event time conversion, 
    confirming tags are in right format, etc) 
    """
    def transform_before_loading_site_visit(self, dic):
        # validate
        verb = dic.get("verb", None)
        key = dic.get("key", "")
        event_time = dic.get("event_time", None)
        customer_id = dic.get("customer_id", "")
        tags = dic.get("tags", "")

        if verb not in "NEW":
            print("Invalid event in site_visit event_type!")
            return

        if key is "":
            print("Invalid Page (site_visit) key! ")
            return

        if customer_id is "":
            print("Invalid customer_id in site_visit! ")
            return

        try:
            dateutil.parser.parse(event_time)
        except ValueError:
            print("Invalid Date in site_visit event_type!")
            return

        if tags is not "":
            # tags = "{" + tags + "}"
            try:
                json.dumps(tags)
            except ValueError:
                print("Invalid JSON format in site_visit tags!")
                return

        # Insert into DB
        self.loader.add_site_visit_entry(key, event_time, customer_id, json.dumps(tags))



    """
    Confirm all mandatory fields of image event
    In future more business validations can be added to this step
    In future false data can also be transformed (e.g. event time conversion) 
    """
    def transform_before_loading_image(self, dic):
        # validate
        verb = dic.get("verb", None)
        key = dic.get("key", "")
        event_time = dic.get("event_time", None)
        customer_id = dic.get("customer_id", "")

        if verb not in "UPLOAD":
            print("Invalid event in image event_type!")
            return

        if key is "":
            print("Invalid key in image event_type!")
            return

        if customer_id is "":
            print("Invalid customer_id in image! ")
            return

        try:
            valid_date = dateutil.parser.parse(event_time)
        except ValueError:
            print("Invalid Date in image event_type!")
            return

        # Insert into DB
        self.loader.add_image_entry(key, event_time, customer_id)



    """
    Confirm all mandatory fields of order event
    In future more business validations can be added to this step
    In future false data can also be transformed (e.g. event time conversion, 
    confirming tags are in right format, etc) 
    """
    def transform_before_loading_order(self, dic):
        # validate
        verb = dic.get("verb", None)
        key = dic.get("key", "")
        event_time = dic.get("event_time", None)
        customer_id = dic.get("customer_id", "")
        total_amount = dic.get("total_amount", "")

        if verb not in ("NEW", "UPDATE"):
            print("Invalid event in order event_type!")
            return

        if key is "":
            print("Invalid key in order event_type!")
            return

        if customer_id is "":
            print("Invalid customer_id in order! ")
            return

        if total_amount is "":
            print("Invalid total_amount in order! ")
            return

        else:
            # Assuming that total amount is always in USD
            # So truncating the last 4 characters to get float value
            try:
                total_amount = total_amount[:-4]
                total_amount_float = "{:.2f}".format(float(total_amount))
            except ValueError:
                print("Invalid total_amount in order! ")

        try:
            valid_date = dateutil.parser.parse(event_time)
            weekly_visit_key = ""
            # Calculate weekly_visit key
            # We will use US calendar weeks (Sunday to Saturday)
            year = valid_date.strftime("%Y")
            week = valid_date.strftime("%U")

            # 53rd week of previous year will be combined with 0th week of next year
            if week == "53":
                week = '00'
                temp_year = int(year) + 1
                year = str(temp_year)

            weekly_visit_key = year + '-' + week

        except ValueError:
            print("Invalid Date in order event_type!")
            return

        # Insert into DB
        self.loader.add_order_entry(key, event_time, customer_id, total_amount, weekly_visit_key)
