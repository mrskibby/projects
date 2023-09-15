"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""
import regex as re
from user import User
from unit import Unit

class UserTeacher(User, Unit):
    def __init__(self, user_id=33333, user_name="Rix", user_password="password", user_role="TA", user_status="enabled", teach_units=['FIT9136', 'FIT5047', 'FIT5157']):
        """
        Constructs a teacher object
        """

        self.user_id = self.generate_user_id()
        self.user_name = user_name
        self.user_password = self.encrypt(user_password)
        self.user_role = user_role
        self.user_status = user_status
        self.teach_units = teach_units

    def __str__(self):
        """Return the teacher information as a formatted string"""
        return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}, {self.teach_units}"

    def teacher_menu(self):
        """
        Display a list of all operations that can only be performed by a teacher.
        """

        print("The Menu for the Teacher to choose from:")
        print("1. List all teaching unit information ")
        print("2. Add a unit ")
        print("3. Delete a unit ")
        print("4. List all students’ information and scores of one unit ")
        print("5. Show the avg/max/min score of one unit ")
        print("6. Logout ")

    def list_teach_units(self):
        """
        Display the information of all units that are taught by the current
        teacher.
        """
        with open(self.unit_url, 'r') as unitfile:
            for line in unitfile:
                unit_data = line.strip().split(", ")
                for units in self.teach_units:
                    if units in unit_data:
                        unit_id = unit_data[0]
                        unit_code = unit_data[1]
                        unit_name = unit_data[2]
                        unit_capacity = unit_data[3]

                        if len(unit_data) <= 1:
                            print("No unit is given in the file")
                            print()
                        else:
                            print("Unit ID: ", unit_id, "| Unit Name: ", unit_name, "| Unit Code: ", unit_code,
                                  "| Unit Capacity: ", unit_capacity)

    def add_teach_unit(self, unit_obj):
        """
        Add a new unit information to the data/unit.txt and add the
        unit_code in the current teacher's 'teach_units' list
        """
        with open(self.unit_url, 'r+') as file:
            lines = file.readlines()
            units_codes = [unit.strip().split(', ')[1] for unit in lines]
            if unit_obj.unit_code in units_codes:
                print(f'The unit {unit_obj.unit_code} is already added')
            else:
                unit_obj.unit_id = self.generate_unit_id()
                file.write(str(unit_obj))
                file.write("\n")
                print(f"Unit '{unit_obj.unit_code}' added successfully.")

                if unit_obj.unit_code not in self.teach_units:
                    self.teach_units.append(unit_obj.unit_code)
                    updated_user_info = self.__str__()
                else:
                    print(f"{self.user_name} is already teaching the course {unit_obj.unit_code}")
                with open(self.user_url, 'r') as file:
                    lines = file.readlines()

                with open(self.user_url,'w') as file:
                    for line in lines:
                        if line.strip().split(', ')[1] == self.user_name:
                            line = updated_user_info+'\n'
                        file.write(line)
            print(f"{unit_obj.unit_code} is added in {self.user_name} record")


    def delete_teach_unit(self, unit_code):
        """
        Delete a unit from the current teacher's 'teach_units' list. If this unit
        has been enrolled by students, remove all associated enrollment records as well.
        """
        deleted_already = False
        # delete the unit_code in user database
        if unit_code not in self.teach_units:
            print(f"The unit {unit_code} is not taught by the Teacher {self.user_name}")
        else:
            self.teach_units.remove(unit_code)
            user_data = self.load_user_data()
            for user in user_data:
                if user[self.id] == self.user_id:
                    teach_units = user[5]
                    if unit_code not in teach_units:
                        print(f"The unit {unit_code} is not taught by the Teacher {self.user_name}")
                    else:
                        teach_units.remove(unit_code)
                        deleted_already = True
                if user[self.role] == 'ST':
                    enrolled_units = user[5]
                    for index, unit in enumerate(enrolled_units):
                        if unit[0] == unit_code:
                            del enrolled_units[index]

            self.save_user_data(user_data)
            if deleted_already == True:
                print(f"The unit {unit_code} has been deleted succesfully from {self.user_name}")

    def list_enrol_students(self, unit_code):
        """
        Display the information of all students currently enrolled in the unit.
        """
        no_results = True
        with open(self.user_url, 'r') as file:
            for line in file:
                if unit_code in line:
                    # make sure it is a enabled student
                    if line.split(', ')[self.role] == 'ST' and line.split(', ')[self.status] == 'enabled':
                        print(line)
                        no_results = False
        if no_results:
            print('No students enrolled the current unit')


    def show_unit_avg_max_min_score(self, unit_code):
        """
        Display the unit’s average, maximum and minimum score.
        """
        # Open the user.txt file from the url
        with open("data/user.txt", 'r') as file:
            # Read all the lines and store it in the user_data variable
            user_data = file.read()
        # filter out all the enrolled units
        enrolled_units_pattern = re.compile(r"ST, enabled, {}', (-?\d+)\)".format(unit_code))
        print(enrolled_units_pattern)
        # Find all the scores in the user_data
        score_lst = enrolled_units_pattern.findall(user_data)
        # Turn all scores to Integer and store it in all_score list
        all_score = [int(s) for s in score_lst]
        # The average score is stored in average-score
        average_score = sum(all_score) / len(all_score)

        # Print the average score
        print(f"The average score: {average_score}")
        # Print the maximum of all the scores
        print(f"The maximum score: {max(all_score)}")
        # Print the minimum of all the scores
        print(f"The minimum score: {min(all_score)}")


# test = UserTeacher(33333, "Rix", "Sakib12345", "TA", "enabled", ['FIT5047', 'FIT5157', 'FIT9147'])
# # print(test.teacher_menu())
# # print(test.list_teach_units())
# unit_obj = Unit(12345,"FIT9147","Database",100)
# print(test.add_teach_unit(unit_obj))
# print(test.delete_teach_unit('FIT9150'))
# print(test.list_enrol_students('FIT9147'))
# print(test.show_unit_avg_max_min_score('FIT9147'))
