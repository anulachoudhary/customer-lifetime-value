from src.extract import Extract
from src.report import Report

if __name__ == "__main__":
    extract = Extract()
    # Ingest data
    # data = extract.get_events_data_from_file("../input/input.txt")
    # extract.ingest(data)

    # Run report
    report = Report()
    report.TopXSimpleLTVCustomers(10)


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