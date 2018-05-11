from src.load import Load

class Report:

    def __init__(self):
        pass


    def TopXSimpleLTVCustomers(self, x_top_customers):

        load = Load()
        top_customers = load.get_top_customer_ltv(x_top_customers)

        output_text = 'TopXSimpleLTVCustomers are:'

        for record in top_customers:
            output_text += '\ncustomer_id: ' + record.customer_id + ', LTV:' + str(52 * (record.average_weekly_revenue) * 10)

        with open('../output/output.txt', 'w') as file:
            file.write(output_text)


