"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""
from user import User
from unit import Unit

import random

class UserStudent(User, Unit):
    def __init__(self, user_id=22222, user_name="Musa", user_password="password", user_role="ST", user_status="enabled", enrolled_units="[('FIT9136', 50)"):

        """
        Constructs a student object
        """

        # super().__init__(user_id, user_name, user_password, 'ST', user_status)
        self.user_id = self.generate_user_id()
        self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status
        self.enrolled_units = enrolled_units
        self.user_name = user_name

    def __str__(self):
        """
        Return the student information as a formatted string
        """
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}, {self.enrolled_units}"

    def student_menu(self):
        """
        Display a list of all operations that can only be performed by a student.
        """
        menu = [
            '1. List all available units information',
            '2. List all enrolled units',
            '3. Enrol a unit',
            '4. Drop a unit',
            '5. Check the score of a unit',
            '6. Generate score',
            '7. Log out'
        ]
        for options in menu:
            print(options)

    def list_available_units(self):
        """
        Display all the units that can be enrolled by the current student.
        """
        with open('data/unit.txt', 'r') as file:
            units = file.readlines()
            code = [unit.split(', ')[1] for unit in units if int(unit.split(', ')[3]) > 0]
            enrolled_units = [unit[0] for unit in self.enrolled_units]
            available_units = set(code).difference(set(enrolled_units))

            if len(available_units) == 0:
                print('There is no unit available for you to enrol')
            else:
                for i, unit_code in enumerate(available_units):
                    print(f"{i + 1}. {unit_code}")


    def list_enrolled_units(self):
        """
        Display all the units that the student enrolled.
        """
        enrolled_units = [unit[0] for unit in self.enrolled_units]

        for i, unit_code in enumerate(enrolled_units):
            print(f"{i + 1}. . {unit_code}")


    def enrol_unit(self, unit_code):
        """
        Enrol the current student into a unit. One student can enrol a maximum of 3 units and each unit has its own capacity.
        After enrollment, initialise the score as -1.
        """
        with open(self.user_url, 'r') as file:
                users = file.readlines()

        user_names = [user.split(', ')[1] for user in users]
        user_idx = user_names.index(self.user_name)

        with open(self.unit_url, 'r') as file:
                units = file.readlines()

        units_code = [unit.split(', ')[1] for unit in units if unit.split(', ')[3] != 0]
        enrolled_units = [unit[0] for unit in self.enrolled_units]
        available_units = set(units_code).difference(set(enrolled_units))

        # Check for if there's previous selection or typing error
        if unit_code not in available_units:
            print(f"You have already enrolled {unit_code}, or unit code you entered is not valid")
        else:
            unit_idx = units_code.index(unit_code)
            remain_capacity = units[unit_idx].split(', ')[3]
            if len(self.enrolled_units) <= 3:
                temp = self.enrolled_units
                temp.append((unit_code, -1))
                self.enrolled_units = str(temp)

                users[user_idx] = f"{', '.join(users[user_idx].split(', ')[:5])}, {str(temp)}\n"
                with open(self.user_url, 'w') as file:
                    file.writelines(users)

                units[unit_idx] = f"{', '.join(units[unit_idx].split(', ')[:3])}, {int(remain_capacity)-1}\n"
                with open(self.unit_url, 'w') as file:
                    file.writelines(units)

                print(f"Enrolment into {unit_code} has succeed for {self.user_name}")
            else:
                print("Enrolment is not successful")


    def drop_unit(self, unit_code):
        """
        Remove the unit from the list of units in which the student is currently enrolled
        """
        with open(self.user_url, 'r') as file:
            users = file.readlines()

        user_names = [user.split(', ')[1] for user in users]

        user_idx = user_names.index(self.user_name)

        with open(self.unit_url, 'r') as file:
            units = file.readlines()

        units_code = [unit.split(', ')[1] for unit in units]
        unit_idx = units_code.index(unit_code)
        remain_capacity = units[unit_idx].split(', ')[3]
        enrolledunits_list = [unit[0] for unit in self.enrolled_units]
        enrolledunit_idx = enrolledunits_list.index(unit_code)

        temp = self.enrolled_units
        temp.pop(enrolledunit_idx)
        self.enrolled_units = str(temp)

        users[user_idx] = f"{', '.join(users[user_idx].split(', ')[:5])}, {str(temp)}\n"
        with open('data/user.txt', 'w') as file:
            file.writelines(users)

        units[unit_idx] = f"{', '.join(units[unit_idx].split(', ')[:3])}, {int(remain_capacity)+1}\n"
        with open('data/unit.txt', 'w') as file:
            file.writelines(units)

        print(f"The unit {unit_code} has been dropped for {self.user_name}")


    def check_score(self, unit_code=None):
        """
        Display the unit score for selected unit, or display score for all units which the student have enrolled.
        """
        if unit_code:
            enrolledunits_list = [unit[0] for unit in self.enrolled_units]
            if unit_code not in enrolledunits_list:
                print(f"The Student {self.user_name} is not enrolled in the course {unit_code}")
            else:
                unit_idx = enrolledunits_list.index(unit_code)
                score = self.enrolled_units[unit_idx][1]
                print(f"{unit_code} score: {score}")
        else:
            for unit in self.enrolled_units:
                print(f"{unit[0]} score: {unit[1]}")


    def generate_score(self, unit_code):
        """
        A random score between 0 and 100 (inclusive) should be generated for a unit. This resulting score should then
        be added to the student's list of enrolled units in the 'user.txt' file.
        """
        random_score = random.randint(0, 100)

        with open('data/user.txt', 'r') as file:
            users = file.readlines()
        user_names = [user.split(', ')[1] for user in users]
        # print(user_names)
        user_idx = user_names.index(self.user_name)
        enrolledunits_list = [unit[0] for unit in self.enrolled_units]
        if unit_code not in enrolledunits_list:
            print(f"The Student {self.user_name} is not enrolled in the course {unit_code}")
        else:
            enrolledunit_idx = enrolledunits_list.index(unit_code)
            temp = self.enrolled_units
            temp[enrolledunit_idx] = (unit_code, random_score)
            self.enrolled_units = str(temp)
            users[user_idx] = f"{', '.join(users[user_idx].split(', ')[:5])}, {str(temp)}\n"
            with open('data/user.txt', 'w') as file:
                file.writelines(users)
            print(f"The score of {random_score} is given to the student {self.user_name}.")


# test = UserStudent(user_name="Ovi", user_password="^^^v!J#T$R%K&X(Y)Z*1+2-$$$", user_role="ST", user_status="enabled", enrolled_units=[('FIT9137', -1), ('FIT5157', 50), ('FIT5047', 50)])
# print(test.student_menu())
# print(test.list_available_units())
# print(test.list_enrolled_units())
# print(test.enrol_unit('FIT5047'))
# print(test.drop_unit('FIT5047'))
# print(test.check_score('FIT9147'))
# print(test.generate_score('FIT9149'))
