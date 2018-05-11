
class Report:

    def __init__(self):
        pass


    def TopXSimpleLTVCustomers(self, x_top_customers):



        customers = ['10', '20', '30']

        output_text = 'TopXSimpleLTVCustomers are: ' + ' '.join(customers)

        with open('../output/output.txt', 'w') as file:
            file.write(output_text)


