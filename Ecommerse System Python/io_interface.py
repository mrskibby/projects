class IOInterface:

    def get_user_input(self, message, num_of_args):
        # Print the message and get user input as a string
        user_input = input(message)

        # Split the input string into arguments
        args = user_input.split()

        # If there are less arguments than expected, fill the rest with empty strings
        while len(args) < num_of_args:
            args.append("")

        # If there are more arguments than expected, ignore the rest
        args = args[:num_of_args]
        # print(len(args))
        return args

    def main_menu(self):
        print("Login Menu: ")
        print("1. Login")
        print("2. Register")
        print("3. Quit")

    def admin_menu(self):
        print("Admin Menu: ")
        print("1. Show products")
        print("2. Add customers")
        print("3. Show customers")
        print("4. Show orders")
        print("5. Generate test data")
        print("6. Generate all statistical figures")
        print("7. Delete all data")
        print("8. Delete customer using customer id")
        print("9. Delete order using order id")
        print("10. Delete product using product id")
        print("11. Logout")

    def customer_menu(self):
        print("Customer Menu: ")
        print("1. Show profile")
        print("2. Update profile")
        print("3. Show products")
        print("4. Show history orders")
        print("5. Generate all consumption figures")
        print("6. Get product using product id")
        print("7. Place an order")
        print("8. Logout")

    def show_list(self, user_role, list_type, object_list):
        # Check the user_role and list_type
        if user_role == 'Customer' and list_type == 'Customer':
            print("Sorry, as a customer you cannot view the customer list.")
            return

        # Extract the list, page number, and total page from the object_list
        list_objects, page_number, total_page = object_list

        # Check if the list is empty
        if not list_objects:
            print(f"No {list_type} found.")
            return

        # Display the list type, page number, and total page
        print(f"{list_type} List (Page {page_number} of {total_page}):")

        # Display the list objects
        for i, obj in enumerate(list_objects, 1):
            print(f"{i}. {obj}")

    def print_error_message(self, error_source, error_message):
        print(f"Error occurred in {error_source}: {error_message}")

    def print_message(self, message):
        print(message)

    def print_object(self, target_object):
        print(str(target_object))

    def print_update(self):
        print("1. Username")
        print("2. Password")
        print("3. Email")
        print("4. Mobile")


# test = IOInterface()
# test.get_user_input('This is not anything', 3)
# test.main_menu()
# test.admin_menu()
# test.show_list("")