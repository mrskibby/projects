
from model_user import User

class Customer(User):

    def __init__(self, user_id="u_1111111111", user_name="Sakib", user_password="123456789", user_register_time="“DD-MM-YYYY_HH:MM:SS",
                 user_role="Customer", user_email="sakib@gmail.com", user_mobile="+61447096494"):
        """
        Initialize user with provided attributes.
        """
        super().__init__(user_id, user_name, user_password, user_register_time, user_role="Customer")
        self.user_email = user_email
        self.user_mobile = user_mobile

    def __str__(self):
        """
        Returns a string representation of the User instance.
        """
        return f"{super().__str__()}\n"

