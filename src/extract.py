import json

import datetime

import dateutil

from src.transform import Transform


"""
This is the first step - extract 
In this step we will read provided input file for all events

In future we can read data from file or any other external source
"""
class Extract:

    def __init__(self):
        pass


    """
    Validate data from events 
    Based on type of events, invoke respective validation and loading logic
    In future more transformations can be added
    """
    def ingest(self, data):

        transform = Transform()

        # loop over all events inside data
        for dic in data:

            # for each item print out what type of event it is
            event_type = (dic.get("type"))
            # For every event type create new model
            if event_type == "CUSTOMER":
                transform.transform_before_loading_customer(dic)

            elif event_type == "SITE_VISIT":
                transform.transform_before_loading_site_visit(dic)

            elif event_type == "IMAGE":
                transform.transform_before_loading_image(dic)

            elif event_type == "ORDER":
                transform.transform_before_loading_order(dic)


    """
    Read the provided events data in a JSON file
    """
    def get_events_data_from_file(self, file_name):

        data = {}

        try:
            with open(file_name) as f:
                data = json.load(f)
        except ValueError:
            print("Error in data file")
            exit(0)

        return data

