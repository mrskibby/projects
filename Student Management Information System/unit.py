"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""
import random

class Unit:
    """contains all the operations related to a unit."""

    unit_url = "data/unit.txt"

    # The index of data provided in the unit.txt file
    id = 0
    code = 1
    name = 2
    capacity = 3

    def __init__(self, unit_id=0, unit_code="FIT9136", unit_name="Python", unit_capacity=1000):
        """
        Initialized unit with provided attributes.
        """
        self.unit_id = self.generate_unit_id()
        self.unit_code = unit_code
        self.unit_name = unit_name
        self.unit_capacity = unit_capacity

    def __str__(self):
        """
        Returns a string representation of the Unit instance.
        """
        return f"{self.unit_id}, {self.unit_code}, {self.unit_name}, {self.unit_capacity}"

    def generate_unit_id(self):
        """
        return a unique unit id(7 digits number)
        """
        # for all unit_ids in the unit.txt file
        all_unit_id = []

        with open(self.unit_url, 'r') as file:
            for line in file.readlines():
                # find the unit_id for each line
                line_unit_id = line.split(",")[self.id].strip()
                # change the unit_id to int and append it to the all_unit_id
                all_unit_id.append(int(line_unit_id))

        while True:
            # generate unique 7 digit number
            unit_id = random.randint(1000000,9999999)
            # return if the unit_id is not in the unit.txt file
            if unit_id not in all_unit_id:
                return unit_id


# test = Unit()
# print(test.generate_unit_id())