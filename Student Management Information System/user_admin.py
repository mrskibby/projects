"""
Group Number: Group178
Member Names: Md Musa, Nazmus Sakib, GuanRu, Chen
"""

from user import User
from unit import Unit

class UserAdmin(User, Unit):
	"""" contains all operations related to an admin """
	def __init__(self, user_id=11111, user_name="admin", user_password="password", user_role="AD", user_status="enabled"):
		""" Initializing the required attributes for the admin """

		# super().__init__(user_id, user_name, user_password, user_role, user_status)
		self.user_role = user_role
		self.user_id = self.generate_user_id()
		self.user_name = user_name
		self.user_role = user_role
		self.user_password = self.encrypt(user_password)
		self.user_status = user_status

	# def __str__(self):
	# 	super().__str__(self)

	def __str__(self):
		return f"{self.user_id}, {self.user_name}, {self.user_password}, {self.user_role}, {self.user_status}"

	def admin_menu(self):
		""" displaying the menu for the admin"""
		print("The Menu for the Admin to choose from:")
		print("1. Search for user information ")
		print("2. List all users' information ")
		print("3. List all units' information ")
		print("4. Enable/Disable user ")
		print("5. Add user ")
		print("6. Delete user")
		print("7. Logout")

	def search_user(self, user_name):
		with open(self.user_url, 'r') as file:
			for line in file:
				user_data = line.strip().split(', ')
				if user_data[1] == user_name:
					print(line.strip())
		# print(f"{user_name} not found in user data")
		return None

	def list_all_users(self):
		with open(self.user_url, 'r') as file:
			for line in file:
				user_data = line.strip().split(", ")
				user_id = user_data[0]
				user_name = user_data[1]
				user_password = user_data[2]
				user_role = user_data[3]
				user_status = user_data[4]
				user_course = user_data[5:]
				if len(user_course)<1:
					print("User ID: ", user_id,"| User Name: ", user_name,"| User Password: ", user_password,"| User Role: ", user_role,"| User Status: ", user_status)
				else:
					print("User ID: ", user_id,"| User Name: ", user_name,"| User Password: ", user_password,"| User Role: ", user_role,"| User Status: ", user_status,"| User Course: ",user_course)

	def list_all_units(self):
		with open(self.unit_url, 'r') as file:
			for line in file:
				unit_data = line.strip().split(", ")
				unit_id = unit_data[0]
				unit_code = unit_data[1]
				unit_name = unit_data[2]
				unit_capacity = unit_data[3]

				if len(unit_data)<1:
					print("No unit is given in the file")
				else:
					print("Unit ID: ",unit_id,"| Unit Name: ",unit_name,"| Unit Code: ",unit_code,"| Unit Capacity: ", unit_capacity)


	def enable_disable_user(self, user_name):
		with open(self.user_url, 'r') as file:
			users = file.readlines()

		user_names = [user.split(', ')[1] for user in users]
		if user_name not in user_names:
			print(f'there is no user named {user_name}')
		else:
			user_idx = user_names.index(user_name)
			if 'disabled' in users[user_idx].split(', ')[4]:
				temp = users[user_idx].split(', ')
				temp[4] = 'enabled'
				temp[-1] = temp[-1].rstrip()
				temp[-1] += '\n'
				updated_status = ', '.join(temp)
				users[user_idx] = updated_status

				with open(self.user_url, 'w') as file:
					file.writelines(users)

				print(f"{user_name}'s status has been updated to enabled")
			else:
				temp = users[user_idx].split(', ')
				temp[4] = 'disabled'
				temp[-1] = temp[-1].rstrip()
				temp[-1] += '\n'
				updated_status = ', '.join(temp)
				users[user_idx] = updated_status

				with open(self.user_url, 'w') as file:
					file.writelines(users)

				print(f"{user_name}'s status has been updated to disabled")


	# def add_user(self, user_obj):
	# 	"""Add a new user to the system with all the required attributes"""
	# 	"""Checking if the user exists"""
	# 	for user in self.user_data:
	# 		if user[self.username] == user_name:
	# 			print(f"User '{user_name}' already exists")
	# 		else:
	# 			pass
	#
	# 	"""Adding a new user to the system"""
	# 	new_user = [user_obj.user_id, user_obj.user_name, user_obj.user_password, user_obb.user_role, user_obj.user_status]
	# 	"""making sure the user data is updated in actual file"""
	# 	self.user_data.append(new_user)
	#
	# 	""" Persisting the data to user.text """
	# 	with open(self.user_url, "w") as f:
	# 		for user in self.user_data:
	# 			f.write(",".join(user) + "\n")
	#
	# 	print(f"user name '{user_obj.user_name}' has been added to the system!")

	# def add_user(self,user_obj):
	# 	with open(self.user_url, "r+") as f:
	# 		lines = f.readlines()
	# 		usernames = [line.split(", ")[1] for line in lines]
	# 		if user_obj.user_name in usernames:
	# 			print("User already exists.")
	# 		else:
	# 			user_obj.user_id = self.generate_user_id()
	# 			user_obj.user_password = self.encrypt(self.user_password)
	# 			if user_obj.user_role == 'ST':
	# 				user_obj.enrolled_units = ['']
	# 			elif user_obj.user_role == 'TA':
	# 				user_obj.teach_units = ['']
	# 			f.write(str(user_obj))
	# 			f.write("\n")
	# 			print("User added successfully.")

	def add_user(self, user_obj):
		with open(self.user_url, 'r') as file:
			users = file.readlines()

		user_names = [user.split(', ')[1] for user in users]

		if user_obj.user_name in user_names:
			print(f'user name {user_obj.user_name} has already been taken')
		elif user_obj.user_role == 'TA':
			users.append(
				f'{user_obj.user_id}, {user_obj.user_name}, {user_obj.user_password}, {user_obj.user_role}, {user_obj.user_status}, {user_obj.teach_units}\n')

			with open(self.user_url, 'w') as file:
				file.writelines(users)

			print(f"user {user_obj.user_name} has been added")
		elif user_obj.user_role == 'ST':
			users.append(
				f'{user_obj.user_id}, {user_obj.user_name}, {user_obj.user_password}, {user_obj.user_role}, {user_obj.user_status}, {user_obj.enrolled_units}\n')

			with open(self.user_url, 'w') as file:
				file.writelines(users)

			print(f"user {user_obj.user_name} has been added")
		elif user_obj.user_role == 'AD':
			users.append(
				f'{user_obj.user_id}, {user_obj.user_name}, {user_obj.user_password}, {user_obj.user_role}, {user_obj.user_status}\n')


	def delete_user(self,user_name):
		with open(self.user_url, 'r') as file:
			lines = file.readlines()
		found_user = False
		with open(self.user_url, 'w') as file:
			for line in lines:
				if line.split(', ')[1] != user_name:
					file.write(line)
				else:
					found_user = True
		if not found_user:
			print("User could not be found")
		else:
			print("User deleted successfully")


# test = UserAdmin()
# print(test.admin_menu())
# print(test.search_user('xxxx'))
# print(test.list_all_users())
# print(test.list_all_units())
# print(test.enable_disable_user("Nazmus"))
# user_obj = User(12345,"Skibby","Sakib12345","ST","enabled")
# print(test.add_user(user_obj))
# print(test.delete_user("Nazmus"))