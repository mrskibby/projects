import re
import time
from model_admin import Admin
from operation_user import UserOperation
class AdminOperation:
    user_url = "data/users.txt"

    # The column index of the list of a line
    user_id_index = 0
    user_name_index = 1
    user_password_index = 2
    user_register_time_index = 3
    user_role_index = 4
    def register_admin(self, user_name, user_password):
        user_id = UserOperation().generate_user_id()
        user_register_time = UserOperation()._get_current_time()
        if not UserOperation().check_username_exist(user_name):
            if UserOperation().validate_username(user_name):
                if UserOperation().validate_password(user_password):
                    try:
                        with open(self.user_url, "a") as file:
                            file.write(str(Admin(user_id, user_name, UserOperation().encrypt_password(user_password), user_register_time)))
                            print(f"The admin data has been stored for {user_name}")
                        return True
                    except IOError:
                        return False
                else:
                    print("The password is invalid, it must have 5 chars with 1 letter and 1 digit")
                    return False
            else:
                print("The username is invalid. Must be 5 chars and only letters or _")
                return False
        else:
            print("The username is already used. Give a new username")
            return False

# test = AdminOperation()
# test.register_admin("sakib", "sakib1") #correct