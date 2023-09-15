import random
import time
import string
import re
import ast
import string
import pandas as pd

from model_user import User
# from operation_customer import Customer

class UserOperation(User):
    user_url = "data/users.txt"

    # The column index of the list of a line
    user_id_index = 0
    user_name_index = 1
    user_password_index = 2
    user_register_time_index = 3
    user_role_index = 4

    def __int__(self, user_id="u_1111111111", user_name="Nazmus", user_password="123456789", user_register_time="DD-MM-YYYY_HH:MM:SS", user_role="Customer"):
        super.__init__(user_name, user_password, user_register_time, user_role)
        self.user_id = self.generate_user_id()


    def __str__(self):
        return super().__str__()


    def generate_user_id(self):
        """
        return a unique user id
        """
        # get all the existing user ids
        all_user_id = []

        with open(self.user_url, 'r') as file:
            for line in file.readlines():
                # append all user_id to the all_user_id
                user_data = ast.literal_eval(line)
                all_user_id.append(user_data['user_id'])

        while True:
            # generate unique 10 digit number
            user_generated_id = str(random.randint(1000000000, 9999999999))

            # add with u_ with the generated id
            user_id = 'u_'+user_generated_id
            if user_id not in all_user_id:
                # print(user_id)
                return user_id


    def encrypt_password(self, user_password):
        random_string_length = len(user_password) * 2
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=random_string_length))

        encrypted_password = ""
        for i in range(len(user_password)):
            random_chars = random_string[i * 2:i * 2 + 2]
            encrypted_password += random_chars + user_password[i]

        encrypted_password = "^^" + encrypted_password + "$$"
        # print(encrypted_password)
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = ""
        encrypted_password = encrypted_password[2:-2]  # Remove "^^" and "$$" from the encrypted password

        for i in range(0, len(encrypted_password), 3):
            decrypted_password += encrypted_password[i+2]

        # print(decrypted_password)
        return decrypted_password

    def check_username_exist(self, user_name):
        """
        Return a boolean value to indicate username existence
        """
        # for all the user_names in the user.txt file
        all_user_names = []

        with open(self.user_url, 'r') as file:
            for line in file.readlines():
                # Find the user_name of each line in the user.txt
                user_data = ast.literal_eval(line)
                if user_data['user_name'] == user_name:
                    # print("true")
                    return True
        # print("false")
        return False

    def validate_username(self, user_name):
        pattern = r"^[a-zA-Z_]{5,}$"
        if re.match(pattern, user_name):
            # print("True")
            return True
        else:
            # print("False")
            return False

    def validate_password(self, user_password):
        pattern = r"^(?=.*[a-zA-Z])(?=.*\d).{5,}$"
        if re.match(pattern, user_password):
            # print("True")
            return True
        else:
            # print("False")
            return False

    def login(self, user_name, user_password):
        """
        Attempt to log in a user with the provided username and password.
        """
        logged_in = False
        with open(self.user_url) as userfile:
            for line in userfile:
                user_data = eval(line)
                if user_data['user_name'] == user_name:
                    if self.decrypt_password(user_data['user_password']) == user_password:
                        print(f"The user {user_name} has logged in successfully")
                        logged_in = True
                        return user_data

        # if logged_in == True:
        return None

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

    def _get_current_time(self):
        current_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())
        return current_time




# test = UserOperation(user_id="u_1111111111", user_name="Sakib", user_password="Sakib12345!", user_register_time="DD-MM-YYYY_HH:MM:SS", user_role="Customer")
# test.generate_user_id() #correct
# test.encrypt_password("Sakib12345!") #correct
# test.decrypt_password("^^0KS3UaP4kdmiIWb5N1aB2Ad3xw4GF5vh!$$") #correct
# test.check_username_exist("Nishat") #correct
# test.validate_username("Saki1") #correct
# test.validate_password("sakib_!") #correct
# test.login(user_name="admin", user_password="admin1") #correct
# test.generate_random_email()
# test.generate_random_mobile_number()
# test.generate_unique_random_username()
# test.generate_random_time()
# test.generate_random_users()
