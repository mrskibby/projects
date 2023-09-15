import time

class Order:
    def __init__(self, order_id="u_12345", user_id="", pro_id="", order_time=""):
        """
        Initialize user with provided attributes.
        """
        self.order_id = order_id
        self.user_id = user_id
        self.pro_id = pro_id
        self.order_time = order_time

    def __str__(self):
        """
        Returns a string representation of the User instance.
        """
        order_data = {
            'order_id': self.order_id,
            'user_id': self.user_id,
            'pro_id': self.pro_id,
            'order_time': self.order_time
        }
        return order_data
        # return f"{order_data}\n"
        # return f"{{'order_id': '{self.order_id}', 'user_id': '{self.user_id}', 'pro_id': '{self.pro_id}', 'order_time': '{self.order_time}'}}"

    def _get_current_time(self):
        current_time = time.strftime("%d-%m-%Y_%H:%M:%S", time.localtime())
        return current_time
