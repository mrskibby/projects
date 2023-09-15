from io_interface import IOInterface
from operation_user import UserOperation
from operation_admin import AdminOperation
from operation_customer import CustomerOperation
from opreation_product import ProductOperation
from operation_order import OrderOperation
from model_user import User
from model_customer import Customer
from model_product import Product
from model_order import Order
from model_admin import Admin

def login_control():
    pass


def customer_control(user):
    page_number = 1
    while True:
        IOInterface().customer_menu()
        choice = IOInterface().get_user_input("Enter your choice: ", 1)[0]

        if choice == "1":
            # Show profile

            with open(UserOperation().user_url, 'r') as file:
                lines = file.readlines()

            for line in lines:
                data = eval(line)
                if data['user_id'] == user['user_id']:
                    user = data

            IOInterface().print_object(user)

        elif choice == '2':
            # Update profile
            IOInterface().print_update()
            attribute_name = int(IOInterface().get_user_input("Please enter the attribute you want to change: ", 1)[0])
            if attribute_name > 4 or attribute_name < 1:
                IOInterface().print_message('Please Select from 1 to 4')

            value = IOInterface().get_user_input("Please enter new value: ", 1)[0]

            if CustomerOperation().update_profile(attribute_name, value, user):
                IOInterface().print_message('Successfully updated profile')
            else:
                IOInterface().print_error_message('Error', 'Failed to update profile')

        elif choice == "3":
            # Show products
            user_input = IOInterface().get_user_input("Enter product keyword (Nothing if you wan to show all products): ", 1)[0]
            keyword = user_input.strip()
            if keyword:
                data = ProductOperation().get_product_list_by_keyword(keyword)
                IOInterface().show_list("customer", "Product", [data, 1, 1])
            else:
                page_number = int(IOInterface().get_user_input("Enter page number: ", 1)[0])
                products, current_page, total_pages = ProductOperation().get_product_list(page_number)
                IOInterface().show_list("customer", "Product", [products, current_page, total_pages])

        elif choice == "4":
            # Show history orders

            page_number = int(IOInterface().get_user_input("Enter page number: ", 1)[0])
            orders, page_number, total_pages = OrderOperation().get_order_list(user['user_id'], page_number)
            IOInterface().show_list("customer", "Order", [orders, page_number, total_pages])

        elif choice == "5":
            # Generate all consumption figures
            if OrderOperation().generate_single_customer_consumption_figure(user['user_id']):
                IOInterface().print_message('Graph Generated Successfully')
            else:
                IOInterface().print_error_message("OrderOperation", "Failed to generate graph")

        elif choice == "6":
            # Get Product Data
            product_id = IOInterface().get_user_input("Enter the product ID to display: ", 1)[0]
            data = ProductOperation().get_product_by_id(product_id)
            if data:
                IOInterface().show_list("customer", "Product", [data, 1, 1])
                IOInterface().print_message("Product Displayed successfully")
            else:
                IOInterface().print_error_message("OrderOperation", "Failed to display product")

        elif choice == "7":
            # Place Order
            product_id = IOInterface().get_user_input("Enter the product ID to place an order: ", 1)[0]
            create_time = UserOperation()._get_current_time()
            if OrderOperation().create_an_order(user['user_id'], product_id, create_time):
                IOInterface().print_message("Order placed successfully")
            else:
                IOInterface().print_error_message("OrderOperation", "Failed to place order")

        elif choice == "8":
            # Logout
            IOInterface().print_message("Logged out successfully.")
            break
        else:
            IOInterface().print_error_message("Invalid choice", "Please enter a valid option.")


def admin_control():

    while True:
        IOInterface().admin_menu()
        choice = IOInterface().get_user_input("Enter your choice: ", 1)[0]

        if choice == "1":
            # Show products
            page_number = int(IOInterface().get_user_input("Enter page number: ", 1)[0])
            products, current_page, total_pages = ProductOperation().get_product_list(page_number)
            IOInterface().show_list("admin", "Product", [products, current_page, total_pages])

        elif choice == "2":
            # Add customers
            username = IOInterface().get_user_input("Enter username: ", 1)[0]
            password = IOInterface().get_user_input("Enter password: ", 1)[0]
            email = IOInterface().get_user_input("Enter email: ", 1)[0]
            mobile = IOInterface().get_user_input("Enter mobile number: ", 1)[0]
            if CustomerOperation().register_customer(user_name=username, user_password=password, user_email=email, user_mobile=mobile):
                IOInterface().print_message("Customers added successfully")
            else:
                IOInterface().print_error_message("CustomerOperation", "Could Not register Customer")

        elif choice == "3":
            # Show customers
            page_number = int(IOInterface().get_user_input("Enter page number: ", 1)[0])
            customers, current_page, total_pages = CustomerOperation().get_customer_list(page_number)
            IOInterface().show_list("admin", "Customer", [customers, current_page, total_pages])

        elif choice == "4":
            # Show orders
            customer_id = IOInterface().get_user_input("Enter user_id of Customer: ", 1)[0]
            page_number = int(IOInterface().get_user_input("Enter page number: ", 1)[0])
            orders, current_page, total_pages = OrderOperation().get_order_list(customer_id, page_number)
            IOInterface().show_list("admin", "Order", [orders, current_page, total_pages])

        elif choice == "5":
            # Generate test data
            if OrderOperation().generate_test_order_data():
                IOInterface().print_message("Test data generated successfully")
            else:
                IOInterface().print_error_message("OrderOperation", "Failed to generate test data")

        elif choice == "6":
            # Generate all statistical figures
            userid = IOInterface().get_user_input("Enter user_id for whom the figure should show: ", 1)[0]
            OrderOperation().generate_all_customers_consumption_figure()
            OrderOperation().generate_all_top_10_best_sellers_figure()
            OrderOperation().generate_single_customer_consumption_figure(userid)
            ProductOperation().generate_discount_likes_count_figure()
            ProductOperation().generate_likes_count_figure()
            ProductOperation().generate_category_figure()
            ProductOperation().generate_discount_figure()
            IOInterface().print_message("Statistical Figure generated successfully")


        elif choice == "7":
            # Delete all data
            ProductOperation().delete_all_products()
            OrderOperation().delete_all_orders()
            CustomerOperation().delete_all_customers()
            IOInterface().print_message("All data deleted successfully")

        elif choice == "8":
            # Delete customer using customer id
            customer_id = IOInterface().get_user_input("Enter the user_id of the customer: ", 1)[0]
            CustomerOperation().delete_customer(customer_id)

        elif choice == "9":
            # Delete order using order id
            order_id = IOInterface().get_user_input("Enter the order_id of the order: ", 1)[0]
            OrderOperation().delete_order(order_id)

        elif choice == "10":
            # Delete product using product id
            product_id = IOInterface().get_user_input("Enter the pro_id of the product: ", 1)[0]
            ProductOperation().delete_product(product_id)

        elif choice == "11":
            # Logout
            IOInterface().print_message("Logged out successfully.")
            break
        else:
            IOInterface().print_error_message("Invalid choice", "Please enter a valid choice")



def main():
    print("Welcome to the E-Commerce System")
    print("Please Wait till the products are extracted")
    print("After the products are extracted it will ask you to create an Admin for program")
    # generate_test_data()
    ProductOperation().extract_products_from_files()

    admin_registered = False
    with open("data/users.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        data = eval(line)
        if data['user_role'] == "Admin":
            admin_registered = True


    while admin_registered == False:
        user_name = IOInterface().get_user_input("Please enter username for Admin: ", 1)[0]
        user_password = IOInterface().get_user_input("Please enter password for Admin: ", 1)[0]
        if UserOperation().validate_username(user_name):
            if UserOperation().validate_password(user_password):
                AdminOperation().register_admin(user_name, user_password)
                admin_registered = True
            else:
                print('The password is invalid')
        else:
            print('The username is invalid')


    while True:
        IOInterface().main_menu()
        choice = IOInterface().get_user_input("Enter your choice: ", 1)[0]

        if choice == '1':  # Login
            username = IOInterface().get_user_input("Enter username: ", 1)[0]
            password = IOInterface().get_user_input("Enter password: ", 1)[0]
            user = UserOperation().login(username, password)

            if user is None:
                IOInterface().print_error_message("Login failed", "Username or password incorrect")
            else:
                if user['user_role'] == "Admin":
                    admin_control()

                elif user['user_role'] == "Customer":
                    customer_control(user)


        elif choice == '2':  # Register
            print("Customer Registration:")
            user_name = IOInterface().get_user_input("Enter username: ", 1)[0]
            user_password = IOInterface().get_user_input("Enter password: ", 1)[0]
            user_email = IOInterface().get_user_input("Enter email: ", 1)[0]
            user_mobile = IOInterface().get_user_input("Enter mobile number: ", 1)[0]
            if CustomerOperation().register_customer(user_name, user_password, user_email, user_mobile):
                IOInterface().print_message("Registration successful")
            else:
                IOInterface().print_error_message("Registration failed", "Invalid data or username already exists")

        elif choice == '3':  # Quit
            break
        else:
            IOInterface().print_error_message("Invalid choice", "Please enter a valid choice")

if __name__ == "__main__":
    main()