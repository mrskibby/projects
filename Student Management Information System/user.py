"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""

import random
import regex as re

class User:
    """contains all the operations related to a user."""

    user_url = "data/user.txt"

    # The index of the data provided in each line of user.txt
    id = 0
    username = 1
    password = 2
    role = 3
    status = 4

    def __init__(self, user_id=0, user_name="Sakib", user_password="password", user_role="ST", user_status="enabled"):
        """
        Initialize user with provided attributes.
        """
        self.user_id = self.generate_user_id()
        self.user_name = user_name
        self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status

    def __str__(self):
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

    def generate_user_id(self):
        """
        return a unique user id
        """
        # for all user_ids in the user.txt file
        all_user_id = []

        with open(self.user_url, 'r') as file:
            for line in file.readlines():
                # Find the user_id for each line
                line_user_id = line.split(",")[self.id].strip()
                # change the user_id to int, and append it to the all_user_id
                all_user_id.append(int(line_user_id))

        while True:
            # generate unique 5 digit number
            user_id = random.randint(10000, 99999)
            # return if the user_id is not in the user.txt file
            if user_id not in all_user_id:
                return user_id

    def check_username_exist(self, user_name):
        """
        Return a boolean value to indicate username existence
        """
        # for all the user_names in the user.txt file
        all_user_names = []

        with open(self.user_url, 'r') as file:
            for line in file.readlines():
                # Find the user_name of each line in the user.txt
                line_user_name = line.split(",")[self.username].strip()
                # store the user_name in the all_user_names list
                all_user_names.append(line_user_name)

        # check if the user_name exists
        if user_name in all_user_names:
            return True
        else:
            return False

    def encrypt(self, user_password):
        """Encrypt a given user password using a custom encryption algorithm."""
        # Define character sets for encryption for str_1 and str_2
        str_1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        str_2 = "!#$%&()*+-./:;<=>?@\^_`{|}~"

        # This is to store the encrypted password
        encrypted_password = ""

        # Encrypt each letter in the password
        for index, letter in enumerate(user_password):
            # 1: get ascii code of the letter
            ascii_code = ord(letter)
            # 2: Get the remainder of the ASCII code number divided by the length of the str_1.
            remainder_1 = ascii_code % len(str_1)
            # 3: Use the remainder as an index to locate a character in str_1.
            char_1 = str_1[remainder_1]
            # 4: Get the remainder of the letter index in the user-provided password divided by the length of the str_2.
            remainder_2 = index % len(str_2)
            # 5: Use the remainder as an index to locate a character in str_2.
            char_2 = str_2[remainder_2]
            # 6: The characters obtained from step 3 and step 5 are used to encrypt the letter
            encrypted_letter = char_1 + char_2
            # add encrypted_letter to encrypted_password
            encrypted_password += encrypted_letter

        # after finishing the encryption, Add "^^^" at the beginning and "$$$" at the end of the encrypted password
        encrypted_password = "^^^" + encrypted_password + "$$$"

        return encrypted_password

    def login(self, user_name, user_password):
        """
        Attempt to log in a user with the provided username and password.
        """
        with open(self.user_url) as userfile:
            for line in userfile:
                fields = line.strip().split(', ')
                if len(fields) < 5:
                    continue  # skip invalid lines
                if self.check_username_exist(user_name):
                    # check if the username and password is correct
                    if fields[1] == user_name and fields[2] == self.encrypt(user_password):
                        # check if the user is enabled
                        if fields[4] == "enabled":
                            return line.strip()
                        else:
                            print("The User is disabled")
                            return None
                    elif fields[2] != self.encrypt(user_password):
                        print("The Password is incorrect")
                        return None
                else:
                    print("The username is invalid")
                    return None
        return None

    def save_user_data(self, user_data):
        """
        write 2 dimensional list of user data into the database
        :param user_data: 2 dimensional list of user data
        :return: N/A
        """
        with open(self.user_url, 'w') as file:
            for line in user_data:
                # change the line into  a string
                # 1. make items in the line be string type
                line_str_lst = [str(item) for item in line]
                line_str = ", ".join(line_str_lst)
                file.write(line_str + "\n")

    # load user data into 2D list
    def load_user_data(self):
        """
        Turn user data from string type into 2 dimensional list and change the data type
        :return: 2 Dimensional list of user data: [[11111, 'admin', '^^^Y!J#2$2%6&X(1)M*$$$', 'AD', 'enabled'],
        [37504, 'stu2', '^^^Y!J#2$2%6&X(1)M*$$$', 'ST', 'enabled', [('FIT1111', -1), ('FIT2222', -1), ('FIT3333', -1)]]
        """
        new_user_data = []
        with open(self.user_url, 'r') as file:
            for line in file:
                new_line_lst = []
                line_items = line.split(', ')
                # escape the empty line
                if len(line_items) > 0:
                    stripped_line_items = [item.strip() for item in line_items]
                    # change the user_id from string type to the integer type
                    stripped_line_items[0] = int(stripped_line_items[0])
                    new_line_lst = stripped_line_items[0:5]
                    # If there is list as the sixth item
                    if len(line_items) > 5:
                        start_index = line.find("[")
                        end_index = line.rfind("]")

                        # Extract the list from the string
                        lst_str = line[start_index:end_index + 1]
                        # evaluate the list string to a list
                        lst = eval(lst_str)
                        new_line_lst.append(lst)
                new_user_data.append(new_line_lst)
        return new_user_data


# test = User()
# print(test._load_data("data/user.txt"))
# print(test.generate_user_id())
# print(test.check_username_exist("Nazmus"))
# print(test.encrypt("password"))
# print(test.login(user_name="admin", user_password="password"))
# print(test.user_data())