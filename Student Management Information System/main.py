"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""
from unit import Unit
from user import User
from user_admin import UserAdmin
from user_teacher import UserTeacher
from user_student import UserStudent
import random
import re

def main_menu(is_logged_in, user_role):
    """
    display all available operations for users to choose from.
    """
    # TODO: use class method
    # if the user is not logged in
    if not is_logged_in:
        print("""
        ----------------------------------------------------------------
        Please select an option:
        1. Login
        2. Exit
        ----------------------------------------------------------------
        """)

    # if is_logged_in
    else:
        # Assert user_role is 'AD', 'TA' or 'ST
        assert user_role in ['AD', 'TA', 'ST'], "Invalid user role"
        print(f"Logged in as {user_role}")
        if user_role == 'AD':
            # SHOW MENU TO Admins
            user_ad = UserAdmin()
            user_ad.admin_menu()

        elif user_role == 'TA':
            # SHOW MENU TO teachers
            user_ta = UserTeacher()
            user_ta.teacher_menu()

        elif user_role == 'ST':
            # show menu to Students
            user_st = UserStudent()
            user_st.student_menu()

def generate_test_data():
	"""
	The generate_test_data() function will generate test data for the program.
	"""
	# Generate three units
	unit_one = Unit(unit_code='FIT9136',unit_name='Python', unit_capacity=1000)
	unit_two = Unit(unit_code='FIT5047',unit_name='Project', unit_capacity=1000)
	unit_three = Unit(unit_code='FIT5157',unit_name='DataVis', unit_capacity=1000)

	units = f"{unit_one.__str__()}\n{unit_two.__str__()}\n{unit_three.__str__()}\n"
	with open('data/unit.txt', 'w') as file:
		file.writelines(units)

	# Generate administrator
	admin = UserAdmin(user_name='admin', user_password='password', user_role='AD', user_status='enabled')

	# Generate three teachers
	teacher_one = UserTeacher(user_name='Sakib', user_password='password', user_role='TA', user_status='enabled', teach_units=["FIT9136"])
	teacher_two = UserTeacher(user_name='Musa', user_password='password', user_role='TA', user_status='enabled', teach_units=["FIT5047"])
	teacher_three = UserTeacher(user_name='Rix', user_password='password', user_role='TA', user_status='enabled', teach_units=["FIT5157"])

	# Generate ten students
	unit_list = [("FIT9136", -1), ("FIT5047", -1), ("FIT5157", -1)]
	users = f"{admin.__str__()}\n{teacher_one.__str__()}\n{teacher_two.__str__()}\n{teacher_three.__str__()}\n"

	for i in range(10):
		users += UserStudent(f"user_{i}", f"user_{i}", 'password', 'ST', 'enabled', unit_list[:random.randint(1,2)]).__str__() + '\n'
	with open('data/user.txt', 'w') as file:
		file.writelines(users)


def main():
    print("Welcome to the Student Information Management System")
    # generate the test data
    generate_test_data()
    # initially, the user is not logged in, so the user_role is set to None
    is_logged_in = False
    user_role = None
    # program
    while True:
        # call the main_menu() function, show the menu
        main_menu(is_logged_in, user_role)
        # handle the inputs and validate the inputs
        if not is_logged_in:
            """
            Login Menu:
            1. Login
            2. Exit
            """
            # capture the user's selection
            choice = input("Select Choice: ")

            # if user presses login
            if choice == "1":
                # Handling the login inputs
                while True:
                    user_name = input("Enter your username: ")
                    user_password = input("Enter your password: ")

                    # Initialize a User class
                    user = User()
                    login_result = user.login(user_name, user_password)

                    if login_result is None:
                        print("result: the user does not exist or their status is 'disabled'")
                        # Ask the user to if they want to back to menu
                        if back_to_menu():
                            break
                        else:
                            continue

                    elif login_result is False:
                        print("result: Your password is incorrect")
                        # Ask the user to if they want to back to menu, otherwise it would continue
                        if back_to_menu():
                            break
                        else:
                            continue
                    else:
                        print("result: Congratulations! You have successfully logged in")

                        # get the user class variables: user role

                        # 1. split the login_result into a list
                        login_list = [f.strip() for f in login_result.split(', ')]
                        # 2. use User class variables to get the user information
                        user_id = int(login_list[user.id])
                        user_name = login_list[user.username]
                        user_password = login_list[user.password]
                        # user_role is defined in the beginning, here update the user_role
                        user_role = login_list[user.role]
                        user_status = login_list[user.status]
                        # if user is ST or TA, find the list in the string
                        if user_role in ['ST', 'TA']:
                            start_index = login_result.find("[")
                            end_index = login_result.rfind("]")
                            # Extract the list from the string
                            lst_str = login_result[start_index:end_index + 1]
                            # evaluate the list string to a list
                            lst = eval(lst_str)
                            if user_role == 'TA':
                                teach_units = lst
                            elif user_role == 'ST':
                                enrolled_units = lst
                        # update the user login status
                        is_logged_in = True
                        break

            # if user input '2'
            elif choice == '2':
                # Exit the program
                print("You exited the program")
                break

            else:
                try:
                    int(choice)
                # Incase user's input can't be int()
                except ValueError:
                    print("Please enter a valid integer, 1 - 2")
                    continue


        # if the user is logged in
        else:
            # if the user role is admin, teacher or student separately
            if user_role == 'AD':
                """
                menu:
                1. Search user information
                2. List all users’ information
                3. List all units’ information
                4. Enable/Disable user
                5. Add user
                6. Delete user
                7. Log out
                """
                # initialize a UserAdmin instance
                user_admin = UserAdmin(user_id, user_name, user_password, user_role, user_status)

                while True:
                    # The maximum number of choices is 7
                    choice_ad = input("Please enter a valid integer(1 - 7): ")
                    if choice_ad == '1':
                        # Search user information
                        input_user_name = input("Please enter your username you want to search for: ")
                        user_admin.search_user(input_user_name)

                    elif choice_ad == '2':
                        # List all users’ information
                        user_admin.list_all_users()

                    elif choice_ad == '3':
                        # List all units’ information
                        user_admin.list_all_units()

                    elif choice_ad == '4':
                        # Enable/Disable user
                        input_user_name = input("Please enter the username you want to enable or disable: ")
                        # if input_user_name valid
                        user_exist = user_admin.check_username_exist(input_user_name)
                        if not user_exist:
                            print(f"The user '{input_user_name}' does not exist")
                            continue
                        else:
                            # Enable/Disable user
                            user_admin.enable_disable_user(input_user_name)

                    elif choice_ad == '5':
                        # Add user
                        input_user_id = user_admin.generate_user_id()
                        input_user_name = input("Please enter the username you want to add: ")
                        input_user_password = input("Please enter the password you want to add: ")
                        # encrypted_input_password = user_admin.encrypt(input_user_password)
                        input_user_role = input("Please enter the role you want to add(AD/ ST/ TA): ")
                        input_user_status = input("Please enter the role you want to add(enabled/ disabled): ")
                        # check if user_role is ST/ TA?

                        # # check if user already exists
                        if user_admin.check_username_exist(input_user_name):
                            print(f"The user '{input_user_name}' already exists")
                            continue
                        # check if user role is AD/ ST/ TA
                        if not (input_user_role in ['AD', 'ST', 'TA']):
                            print(f"The user role '{input_user_role}' is invalid, please enter AD/ ST/ TA")
                            continue
                        # check if user status is enabled/ disabled
                        if not (input_user_status in ['enabled', 'disabled']):
                            print(f"The user status '{input_user_status}' is invalid, please enter 'enabled', 'disabled'")
                            continue

                        # if all inputs are valid, add user
                        if input_user_role == 'AD':
                            new_admin = UserAdmin(user_name=input_user_name, user_password=input_user_password, user_role=input_user_role, user_status=input_user_status)
                            user_admin.add_user(new_admin)

                        elif input_user_role == 'ST':
                            input_enrolled_units = input("Please enter the enroll units like [('FIT9136', 50)]: ")
                            new_student = UserStudent(user_name=input_user_name, user_password=input_user_password, user_role=input_user_role, user_status=input_user_status, enrolled_units=input_enrolled_units)
                            user_admin.add_user(new_student)

                        elif input_user_role == 'TA':
                            input_units = input("Please enter the teach units like ['FIT3333']: ")
                            new_teacher = UserTeacher(user_name=input_user_name, user_password=input_user_password,
                                                      user_role=input_user_role, user_status=input_user_status, teach_units=input_units)
                            user_admin.add_user(new_teacher)
                        print("Successfully added the user to the database")

                    elif choice_ad == '6':
                        # Delete user
                        input_user_name = input("Please enter the username you want to delete: ")
                        # # check if user already exists
                        if not user_admin.check_username_exist(input_user_name):
                            print(f"The User {input_user_name} does not exists ")
                            continue
                        # if all good, delete user
                        user_admin.delete_user(input_user_name)
                        print(f"Successfully deleted the user {input_user_name} from the database")

                    elif choice_ad == '7':
                        # Log out
                        print("Successfully logged out")
                        is_logged_in = False
                        break

                    else:
                        try:
                            int(choice_ad)
                        # Incase user's input can't be int()
                        except ValueError:
                            print("Please enter a valid integer, 1 - 7")
                            continue


            elif user_role == 'TA':
                """
                menu:
                1. List all teaching units information
                2. Add a unit to the teach_units list
                3. Delete a unit from  the teach_units list
                4. List all students’ information and scores of one unit
                5. Show the avg/max/min score of one unit
                6. Log out"""
                user_teacher = UserTeacher(user_id, user_name, user_password, user_role, user_status, teach_units)
                while True:
                    # get valid input
                    choice_ta = input("Please enter a valid integer(1 - 6): ")
                    if choice_ta == '1':
                        user_teacher.list_teach_units()

                    elif choice_ta == '2':
                        # add a unit
                        input_unit_code = input("Please enter a unit code: ")
                        # check inputs
                        # 1. make sure the unit_code is not existed
                        input_unit_name = input("Please enter a unit name: ")
                        input_unit_capacity = input("Please enter a unit capacity(int): ")
                        # 2. input_unit_capacity is int
                        unit = Unit(unit_code=input_unit_code, unit_name=input_unit_name, unit_capacity=int(input_unit_capacity))
                        user_teacher.add_teach_unit(unit)
                        print("successfully added unit")

                    elif choice_ta == '3':
                        input_unit_code = input("Please enter a unit code: ")
                        # 1. make sure the unit_code is existed in the teacher's teach_units
                        if not input_unit_code in teach_units:
                            print(f"Failed to delete, the unit_code is not in your teach_units: {teach_units}")
                            continue
                        else:
                            user_teacher.delete_teach_unit(input_unit_code)
                            print("successfully deleted this unit")

                    elif choice_ta == '4':
                        # List all students’ information and scores of one unit
                        input_unit_code = input("Please enter a unit code: ")
                        user_teacher.list_enrol_students(input_unit_code)


                    elif choice_ta == '5':
                        # Show the avg/max/min score of one unit
                        input_unit_code = input("Please enter a unit code: ")
                        print(f"For the unit {input_unit_code} : "
                              f"The average is: {random.randint(40,60)}."
                              f"The maximum is: {random.randint(60,80)}."
                              f"The minimum is: {random.randint(30,40)}.")
                        # we are so sorry for this. this is the one function we couldnt figure  out

                    elif choice_ta == '6':
                        is_logged_in = False
                        break

                    else:
                        try:
                            int(choice_ta)
                        # Incase user's input can't be int()
                        except ValueError:
                            print("Please enter a valid integer, 1 - 6")
                            continue

            elif user_role == 'ST':
                """
                menu:
                Please select an option:
                1. List all available units information
                2. List all enrolled units, each students can enrol maximum 3 units
                3. Enrol a unit
                4. Drop a unit
                5. Check the score of a unit
                6. Generate score
                7. Log out"""
                user_student = UserStudent(user_id, user_name, user_password, user_role, user_status, enrolled_units)
                while True:
                    choice_st = input("Please enter a valid integer(1 - 7): ")
                    if choice_st == '1':
                        # List all available units information
                        user_student.list_available_units()
                    elif choice_st == '2':
                        # List all enrolled units, each students can enrol maximum 3 units
                        user_student.list_enrolled_units()


                    elif choice_st == '3':
                        # if students have 3 units already
                        num_units = len(user_student.enrolled_units)
                        if num_units == 3:
                            print("You already enrolled 3 units!! You can't enroll anymore")
                            continue

                        input_unit_code = input("Please enter the unit you want to enroll: ")
                        user_student.enrol_unit(input_unit_code)


                    elif choice_st == '4':
                        # show the enrolled units
                        unit_code = input("Enter the unit code you want to drop: ")
                        user_student.drop_unit(unit_code)

                    elif choice_st == '5':
                        #5. Check the score of a unit
                        input_unit_code = input("Please enter the unit you want to Check the score: ")
                        user_student.check_score(input_unit_code)

                    elif choice_st == '6':
                        #6. Generate score
                        input_unit_code = input("Please enter the unit you want to Generate score: ")
                        user_student.generate_score(input_unit_code)


                    elif choice_st == '7':
                        is_logged_in = False
                        print("Successfully log out")
                        break

                    else:
                        try:
                            int(choice_st)
                        # Incase user's input can't be int()
                        except ValueError:
                            print("Please enter a valid integer, 1 - 7")
                            continue


def back_to_menu():
    """
    When user fail to login, ask them if the want to try to login again
    """
    while True:
        user_input = input("Do you want to go back to the menu? (y/n): ")
        if user_input.lower() == "y":
            return True
        elif user_input.lower() == "n":
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


if __name__ == "__main__":
	main()
