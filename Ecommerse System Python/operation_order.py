import os
import pandas as pd
import random
import ast
import time
import math
import string
import matplotlib.pyplot as plt
import webbrowser
import re

from model_order import Order
from operation_user import UserOperation
from operation_customer import Customer

class OrderOperation(Order):
    order_url = "data/orders.txt"

    def __init__(self, order_id="u_12345", user_id="", pro_id="", order_time=""):
        super().__init__(order_id, user_id, pro_id, order_time)

    def __str__(self):
        """
        Returns a string representation of the Order instance.
        """
        return f"{super().__str__()}\n"
    def generate_unique_order_id(self):
        """
        return a unique order id
        """
        # get all the existing user ids
        all_order_id = []

        with open(self.order_url, 'r') as file:
            for line in file.readlines():
                # append all user_id to the all_user_id
                order_data = ast.literal_eval(line)
                all_order_id.append(order_data['order_id'])

        while True:
            # generate unique 5 digit number
            order_generated_id = str(random.randint(10000, 99999))

            # add with u_ with the generated id
            order_id = 'o_' + order_generated_id
            if order_id not in all_order_id:
                # print(order_id)
                return order_id
    def create_an_order(self, customer_id, product_id, create_time=None):
        # Generate a unique order ID
        self.order_id = self.generate_unique_order_id()

        # Use the current time if create_time is not provided
        if create_time is None:
            create_time = time.strftime("%Y-%m-%d_%H:%M:%S")

        self.user_id = customer_id
        self.pro_id = product_id
        self.order_time = create_time

        # Append the order data to the orders.txt file
        try:
            with open(self.order_url, "a") as file:
                file.write(str(self))
                # print('The order has been placed')
            return True
        except Exception as e:
            print(f"Failed to write to file: {e}")
            return False

    def delete_order(self, order_id):
        with open(self.order_url, 'r') as file:
            lines = file.readlines()
        found_order = False
        with open(self.order_url, 'w') as file:
            for line in lines:
                order_data = ast.literal_eval(line)
                if order_data['order_id'] != order_id:
                    file.write(line)
                else:
                    found_order = True
        if not found_order:
            print("Order could not be found")
        else:
            print("Order deleted successfully")

    def get_order_list(self, customer_id, page_number):
        try:
            orders_per_page = 10
            total_pages = 0
            order_list = []
            total_orders = 0

            # Read the product data from the file
            with open(self.order_url, "r") as file:
                lines = file.readlines()

                # Extract the orders for the given page
                for line in lines:
                    order_dict = eval(line)
                    if order_dict['user_id'] == customer_id:
                        total_orders += 1  # Count only the customer's orders

                total_pages = (total_orders - 1) // orders_per_page + 1

                if page_number > total_pages:
                    print(f"There is no page number: {page_number}. Total Pages: {total_pages}")
                    # return None, None, None

                # Calculate the start and end indices of the products for the given page
                start_index = (page_number - 1) * orders_per_page
                end_index = start_index + orders_per_page

                current_index = 0
                # Go through the file again to find the customer's orders for the specific page
                for line in lines:
                    order_dict = eval(line)
                    if order_dict['user_id'] == customer_id:
                        if current_index >= start_index and current_index < end_index:
                            order = Order(order_dict["order_id"], order_dict["user_id"], order_dict["pro_id"],
                                          order_dict["order_time"])
                            order_list.append(line.strip('\n'))
                        current_index += 1
            # print(f"{order_list}, {page_number}, {total_pages}")
            return order_list, page_number, total_pages
        except IOError:
            return None, None, None

    def generate_test_order_data(self):
        # Create 10 customers
        users = self.generate_random_users()

        # Save the users to the users.txt file
        with open(UserOperation().user_url, 'a') as f:
            for user in users:
                f.write(str(user))

        # Read the product data from the file
        # products = pd.read_csv('data/products.txt')['pro_id'].tolist()
        products = []
        with open("data/products.txt", 'r') as file:
            lines = file.readlines()
            for line in lines:
                order_test_data = ast.literal_eval(line)
                # order_test_data['pro_id'] == pro_id:
                products.append(order_test_data['pro_id'])
        # print(products)

        # Generate 50 to 200 orders for each customer
        for user in users:
            num_orders = random.randint(50, 200)
            for _ in range(num_orders):
                # Randomly choose a product
                pro_id = random.choice(products)

                # Generate a random timestamp within the past year
                end_time = time.time()
                start_time = end_time - 60 * 60 * 24 * 365  # One year ago
                random_timestamp = random.uniform(start_time, end_time)
                order_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(random_timestamp))

                # Create the order
                self.create_an_order(user.user_id, pro_id, order_time)
                # print(pro_id)

        # print("Test Data Has been Generated")
        return True


    def generate_single_customer_consumption_figure(self, customer_id):
        # Calculate the monthly consumption for the customer
        monthly_consumption = {}

        # Read the orders from the orders file
        with open("data/orders.txt", "r", encoding="utf-8") as file:
            order_lines = file.readlines()

        # Read the products from the products file
        with open("data/products.txt", "r", encoding="utf-8") as file:
            product_lines = file.readlines()

        # Create a dictionary to map product IDs to their current prices
        product_prices = {}
        for line in product_lines:
            product_data = eval(line.strip())
            product_id = product_data["pro_id"]
            product_price = float(product_data["pro_current_price"])
            product_prices[product_id] = product_price

        # Iterate over the orders and calculate the monthly consumption
        for line in order_lines:
            order_data = eval(line.strip())
            if order_data["user_id"] == customer_id:
                product_id = order_data["pro_id"]
                product_price = product_prices.get(product_id, 0)
                order_month = int(order_data["order_time"].split("-")[1])
                monthly_consumption[order_month] = monthly_consumption.get(order_month, 0) + product_price

        # Prepare the data for the chart
        months = range(1, 13)

        consumption = [monthly_consumption.get(month, 0) for month in months]

        # Create the bar chart
        plt.bar(months, consumption)
        plt.xlabel("Month")
        plt.ylabel("Consumption")
        plt.title("Monthly Consumption for Customer {}".format(customer_id))
        plt.xticks(months)

        # Save the figure
        figure_filename = f"data/figure/consumption_figure_{customer_id}.png"
        plt.savefig(figure_filename)

        # Display the figure in the browser
        webbrowser.open('file://' + os.path.realpath(figure_filename))

        plt.close()

    def generate_all_customers_consumption_figure(self):
        # Get all orders from the database
        orders = []
        with open('data/orders.txt', 'r') as file:
            for line in file:
                order_data = eval(line)
                order = Order(order_data['order_id'], order_data['user_id'], order_data['pro_id'],
                              order_data['order_time'])
                orders.append(order)

        # Initialize a dictionary to store the monthly consumption
        monthly_consumption = {}

        # Calculate the monthly consumption for each order
        for order in orders:
            month = order.order_time.split('-')[1]  # Extract the month value from the order time
            if month not in monthly_consumption:
                monthly_consumption[month] = 0

            monthly_consumption[month] += 1

        # Prepare the data for the chart
        months = list(monthly_consumption.keys())
        consumption = [monthly_consumption[month] for month in months]

        # Convert months to integers for sorting
        months = [int(month) for month in months]

        # Combine months and consumption, sort by month, and split again
        combined = list(zip(months, consumption))
        combined.sort()
        months, consumption = zip(*combined)

        # Convert months back to strings for the plot
        months = [str(month) for month in months]

        # Create a bar chart to visualize the monthly consumption
        plt.bar(months, consumption)
        plt.xlabel('Month')
        plt.ylabel('Consumption')
        plt.title('Monthly Consumption for All Customers')

        # Save the figure
        figure_filename = f"data/figure/all_customer_consumption_figure.png"
        plt.savefig(figure_filename)

        # Display the figure in the browser
        webbrowser.open('file://' + os.path.realpath(figure_filename))

        plt.close()

    def generate_all_top_10_best_sellers_figure(self):
        # Read the orders from the file
        with open('data/orders.txt', 'r') as f:
            orders_dicts = [ast.literal_eval(line.strip()) for line in f]

        # Create a dataframe from the list of dictionaries
        orders_df = pd.DataFrame(orders_dicts)

        # Now you should be able to count the occurrences of each product
        product_counts = orders_df['pro_id'].value_counts()

        # Get the top 10 products
        top_10_products = product_counts[:10]

        # Create a bar plot of the top 10 products
        plt.figure(figsize=(10, 6))
        plt.barh(top_10_products.index, top_10_products.values, color='purple')
        plt.xlabel('Number of Orders')
        plt.ylabel('Product ID')
        plt.title('Top 10 Best-Selling Products')
        plt.gca().invert_yaxis()  # reverse the order of the products on the y-axis

        # Save the figure
        figure_filename = "data/figure/top_10_best_sellers_figure.png"
        plt.savefig(figure_filename)

        # Display the figure in the browser
        webbrowser.open('file://' + os.path.realpath(figure_filename))

        plt.close()

    def delete_all_orders(self):
        # Open the file in write mode, which automatically erases all the data
        with open('data/orders.txt', 'w') as f:
            pass  # Do nothing

    def generate_random_users(self):

        # Create 10 customers
        users = []
        for i in range(10):
            user_id = UserOperation().generate_user_id()
            user_name = self.generate_unique_random_username()
            user_password = UserOperation().encrypt_password('password1')
            user_role = "Customer"
            user_register_time = self.generate_random_time()
            user_email = self.generate_random_email()
            user_mobile = self.generate_random_mobile_number()
            user = Customer(user_id, user_name, user_password, user_register_time, user_role, user_email, user_mobile)
            users.append(user)
        # print(len(users))
        return users

    def generate_random_email(self):
        # List of common email domains
        email_domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com', 'aol.com']

        # Generate a random username
        username = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))

        # Choose a random domain
        domain = random.choice(email_domains)

        # Create the email address
        email = f"{username}@{domain}"

        # print(email)
        return email

    def generate_random_mobile_number(self):
        prefix = random.choice(["04", "03"])
        number = ''.join(random.choice("0123456789") for _ in range(8))
        mobile_number = prefix + number
        # print(mobile_number)
        return mobile_number

    def generate_unique_random_username(self):
        # Read existing usernames
        try:
            df = pd.read_csv('data/users.txt', header=None)
            existing_usernames = df['user_name'].tolist()  # assuming username is the second column
        except:
            existing_usernames = []

        # Define valid characters
        valid_chars = string.ascii_letters + "_"

        # Generate a unique username
        username = ""
        while username in existing_usernames or len(username) < 5:
            username = "".join(
                random.choice(valid_chars) for _ in range(5, 10))  # generate a username with length between 5 and 10
        # print(username)
        return username

    def generate_random_time(self):
        # Generate a random timestamp within the past year
        end_time = time.time()
        start_time = end_time - 60 * 60 * 24 * 365  # One year ago
        random_timestamp = random.uniform(start_time, end_time)
        random_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime(random_timestamp))
        # print(random_time)
        return random_time


# test = OrderOperation()
# test.generate_unique_order_id() #correct
# test.create_an_order('u_1231231223', '123123') #correct
# test.delete_order('o_16059') #correct
# test.get_order_list('u_1231134318', 7) #correct
# test.generate_test_order_data() # correct
# test.generate_single_customer_consumption_figure('u_9201955074') #correct
# test.generate_all_customers_consumption_figure() #correct
# test.generate_all_top_10_best_sellers_figure() #correct
# test.delete_all_orders() #correct