
class Product:

    def __init__(self, pro_id=1111111111, pro_model="Model Sakib", pro_category="Category", pro_name="Sakib",
                 pro_current_price=0.00, pro_raw_price=0.00, pro_discount=0, pro_likes_count=0):
        """
        Initialize user with provided attributes.
        """
        self.pro_id = pro_id
        self.pro_model = pro_model
        self.pro_category = pro_category
        self.pro_name = pro_name
        self.pro_current_price = pro_current_price
        self.pro_raw_price = pro_raw_price
        self.pro_discount = pro_discount
        self.pro_likes_count = pro_likes_count

    def __str__(self):
        """
        Returns a string representation of the User instance.
        """
        product_data = {
            'pro_id': self.pro_id,
            'pro_model': self.pro_model,
            'pro_category': self.pro_category,
            'pro_name': self.pro_name,
            'pro_current_price': self.pro_current_price,
            'pro_raw_price': self.pro_raw_price,
            'pro_discount': self.pro_discount,
            'pro_likes_count': self.pro_likes_count
        }
        return product_data


