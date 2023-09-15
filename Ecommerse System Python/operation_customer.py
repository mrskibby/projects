import re
import time
import ast
from model_customer import Customer
from operation_user import UserOperation
from io_interface import IOInterface


class CustomerOperation(Customer):
    user_url = "data/users.txt"

    def validate_email(self, user_email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if re.match(pattern, user_email):
            return True
        else:
            return False

    def validate_mobile(self, user_mobile):
        if len(user_mobile) != 10:
            return False
        if not user_mobile.isdigit():
            return False
        if not (user_mobile.startswith('04') or user_mobile.startswith('03')):
            return False
        return True

    def register_customer(self, user_name, user_password, user_email, user_mobile):
        user_id = UserOperation().generate_user_id()
        user_role = "Customer"
        user_register_time = UserOperation()._get_current_time()
        if not UserOperation().check_username_exist(user_name):
            if UserOperation().validate_username(user_name):
                if self.validate_email(user_email):
                    if self.validate_mobile(user_mobile):
                        if UserOperation().validate_password(user_password):
                            try:
                                with open(self.user_url, "a") as file:
                                    file.write(
                                        str(Customer(user_id, user_name, UserOperation().encrypt_password(user_password), user_register_time, user_role, user_email, user_mobile)))
                                    print(f"The customer data has been stored for {user_name}")
                                return True
                            except IOError:
                                return False
                        else:
                            print("The password is invalid, it must have 5 chars with 1 letter and 1 digit")
                            return False
                    else:
                        print("The Mobile number is invalid, it must be 10 digits long and must contain only digits")
                        return False
                else:
                    print("The email is invalid")
                    return False
            else:
                print("The username is invalid. Must be 5 chars and only letter or _")
                return False
        else:
            print("The username is already used. Give a new username")
            return False


    def update_profile(self, attribute_name, value, customer_object):
        if attribute_name == 1:
            # value = IOInterface().get_user_input("Please enter new username: ", 1)[0]
            if UserOperation().validate_username(value):
                with open(self.user_url, "r") as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    user_data = ast.literal_eval(line.strip('\n'))
                    if user_data['user_id'] == customer_object['user_id']:
                        user_data['user_name'] = value
                    updated_lines.append(str(user_data) + '\n')

                with open(self.user_url, "w") as file:
                    file.writelines(updated_lines)

                return True

        elif attribute_name == 2:
            # value = IOInterface().get_user_input("Please enter new password: ", 1)[0]
            if UserOperation().validate_password(value):
                with open(self.user_url, "r") as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    user_data = ast.literal_eval(line.strip('\n'))
                    if user_data['user_id'] == customer_object['user_id']:
                        user_data['user_password'] = UserOperation().encrypt_password(value)
                    updated_lines.append(str(user_data) + '\n')

                with open(self.user_url, "w") as file:
                    file.writelines(updated_lines)

                return True

        elif attribute_name == 3:
            # value = IOInterface().get_user_input("Please enter new email: ", 1)[0]
            if self.validate_email(value):
                with open(self.user_url, "r") as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    user_data = ast.literal_eval(line.strip('\n'))
                    if user_data['user_id'] == customer_object['user_id']:
                        user_data['user_email'] = value
                    updated_lines.append(str(user_data) + '\n')

                with open(self.user_url, "w") as file:
                    file.writelines(updated_lines)

                return True
        elif attribute_name == 4:
            # value = IOInterface().get_user_input("Please enter new mobile number: ", 1)[0]
            if self.validate_mobile(value):
                with open(self.user_url, "r") as file:
                    lines = file.readlines()

                updated_lines = []
                for line in lines:
                    user_data = ast.literal_eval(line.strip('\n'))
                    if user_data['user_id'] == customer_object['user_id']:
                        user_data['user_mobile'] = value
                    updated_lines.append(str(user_data) + '\n')

                with open(self.user_url, "w") as file:
                    file.writelines(updated_lines)

                return True


    def delete_customer(self, customer_id):
        with open(self.user_url, 'r') as file:
            lines = file.readlines()
        found_user = False
        with open(self.user_url, 'w') as file:
            for line in lines:
                user_data = ast.literal_eval(line)
                if user_data['user_id'] != customer_id:
                    file.write(line)
                elif user_data['user_role'] == "Admin":
                    file.write(line)
                else:
                    found_user = True
        if not found_user:
            print("User could not be found")
        else:
            print("User deleted successfully")

    def get_customer_list(self, page_number):
        try:
            with open(self.user_url, "r") as file:
                lines = file.readlines()

                # Calculate the total number of pages
                total_pages = (len(lines) // 10) + 1

                if page_number > total_pages:
                    print(f"There is no page number: {page_number}. Total Pages: {total_pages}")

                # Calculate the starting and ending indices for the requested page
                start_index = (page_number - 1) * 10
                end_index = page_number * 10
                # Retrieve the customers for the requested page
                customer_list = []
                for line in lines[start_index:end_index]:
                    data = eval(line)
                    if data['user_role'] == 'Customer':
                        customer_list.append(line.strip('\n'))

                return customer_list, page_number, total_pages
        except IOError:
            return None, None, None

    def delete_all_customers(self):
        try:
            with open(self.user_url, 'r') as file:
                lines = file.readlines()

            with open(self.user_url, "w") as file:
                for line in lines:
                    user_data = ast.literal_eval(line)
                    if user_data['user_role'] != "Customer":
                        file.write(line)

            # print("All the customers are deleted")
            return True
        except IOError:
            pass


# test = CustomerOperation()
# test.register_customer("Bokaaa", "boka1", "nsakib360@gmail.com", "0447096494") #correct
# test.delete_customer("u_4034517227") #correct
# test.get_customer_list(1) #correct
# test.delete_all_customers() #correct
# test.update_profile('attribute_name', 'value', 'customer_object')