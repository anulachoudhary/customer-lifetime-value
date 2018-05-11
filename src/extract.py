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
    def validate_transform_load(self, data):

        transform = Transform()

        # loop over all events inside data
        for dic in data:
            # print(dict)

            # for each item print out what type of event it is
            event_type = (dic.get("type"))
            # For every event type create new model
            if event_type == "CUSTOMER":
                transform.transform_before_loading_customer(dic)
                pass

            elif event_type == "SITE_VISIT":
                transform.transform_before_loading_site_visit(dic)
                pass

            elif event_type == "IMAGE":
                transform.transform_before_loading_image(dic)
                pass

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


if __name__ == "__main__":
    extract = Extract()

    data = extract.get_events_data_from_file("../sample_input/events.json")
    extract.validate_transform_load(data)
    #
    # dt = dateutil.parser.parse('2018-01-01T01:56:35.450686Z')
    # # print (dt.strftime("%Y-%U"))
    #
    # dt = dateutil.parser.parse('2018-01-05T01:56:35.450686Z')
    # # print (dt.strftime("%Y-%U"))
    #
    # dt = dateutil.parser.parse('2018-01-07T01:56:35.450686Z')
    # # print (dt.strftime("%Y-%U"))
    #
    # dt = dateutil.parser.parse('2017-12-31T01:56:35.450686Z')
    # print (dt.strftime("%Y-%U"))
    # week = dt.strftime("%U")
    # year = dt.strftime("%Y")
    #
    # # 53rd week of previous year will be combined with 0th week of next year
    # if week == "53":
    #     week = '00'
    #     temp_year = int(year) + 1
    #     year = str(temp_year)
    #
    # weekly_visit_key = year + '-' + week
    # print (weekly_visit_key)
    #
    #
    #
    # # d = "2017-01-06T12:45:52.041Z"
    # # r = datetime.datetime.strptime(d + '-0', "%Y-%M-%DT%H-%M-W%W-%w")
    # # print(r)