import time

class User:

    def __init__(self, user_id="u_1111111111", user_name="Sakib", user_password="123456789",
                 user_register_time="DD-MM-YYYY_HH:MM:SS", user_role="Customer"):
        """
        Initialize user with provided attributes.
        """
        self.user_id = user_id
        self.user_name = user_name
        self.user_password = user_password
        self.user_role = user_role
        self.user_register_time = user_register_time


    def __str__(self):
        """
        Returns a string representation of the User instance.
        """
        if self.user_role == "Admin":
            user_data = {
                'user_id': self.user_id,
                'user_name': self.user_name,
                'user_password': self.user_password,
                'user_register_time': self.user_register_time,
                'user_role': self.user_role
            }
            return user_data
        elif self.user_role == "Customer":
            user_data = {
                'user_id': self.user_id,
                'user_name': self.user_name,
                'user_password': self.user_password,
                'user_register_time': self.user_register_time,
                'user_role': self.user_role,
                'user_email': self.user_email,
                'user_mobile': self.user_mobile
            }
            return user_data

    def _get_current_time(self):
        current_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())
        return current_time

# test = User(user_id="u_1111111111", user_name="Sakib", user_password="123456789", user_register_time="DD-MM-YYYY_HH:MM:SS", user_role="Customer")
# test.__str__()
