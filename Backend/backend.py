import mysql.connector as mysql

class InventoryInstance:

	def __init__(self, username):

		self.connection = mysql.connect(user='root',password='ayush123')
		self.cursor = self.connection.cursor()
		self.cursor.execute("use inventory_man")
		
	def extract_data(self,username):

		self.current_table =[]
		self.username = username
		self.cursor.execute(f"select * from inventory i join items t on i.username=t.username and i.item_id=t.item_id where i.username='{username}'")
		self.data = self.cursor.fetchall()
		for i in self.data:
			m = []
			for j in i:

				if j not in m:
					m.append(j)
			self.current_table.append(m)
		return self.current_table

			

	"""MainWindow.resize(800, 500)
        MainWindow.setFixedSize(800, 350)"""

	def add_data(self, l):
		x = l[0]
		y = l[1]
		z = l[4]
		a = l[2]
		b = l[3]

		try:
			self.cursor.execute(f"insert into inventory values('{self.username}','{x}',{b})")
			self.cursor.execute(f"insert into items values('{self.username}','{x}','{y}',{z},'{a}')")
			self.cursor.execute("commit")
			return 1
		except:
			return 0

		return 0


	def del_data(self,itm_c):
		
		try:
			self.cursor.execute(f"delete from items where username='{self.username}' and item_id='{itm_c}'")
			self.cursor.execute(f"delete from inventory where username='{self.username}' and item_id='{itm_c}'")
			self.cursor.execute("commit")
			return 1
		except:
			return 0


	#def modify_data(self, username):


class ConnectionAPI:

	def __init__(self):

		self.connection = mysql.connect(user='root',password='ayush123')

		self.cursor = self.connection.cursor()
		self.cursor.execute("use inventory_man")
		

	def commit_changes(self):

		self.cursor.execute("commit")


	
	def check_user_credentials(self,username,password):
		username1 = f"'{username}'"
		x = self.get_user_data("username", username1)
		if not len(x) == 0:
			if x[0][2] == password:
				print("Access Granted")
				self.close_conn()
				self.user_table_instance = InventoryInstance(username)
				return 1

			else:
				print("incorrect credentials")
				return 0
		else:
			print("Incorrect Username")



	def get_user_data(self, field, key_data):

		self.cursor.execute(f"select * from user_data where {field} = {key_data}")
		l = self.cursor.fetchall()
		return l



	def get_user_metadata(self):

		self.cursor.execute("select * from user_data")

		l = self.cursor.fetchall()
		print(l)




	def post_into_user_metadata(self, user, pass1, name,email):

		
		

		try:
			self.cursor.execute(f"insert into user_data values('{name}','{user}','{pass1}','{email}')")

			self.commit_changes()

			return 1

		except mysql.errors.IntegrityError as err:

			print(err)

			print("User Name already exists!!")

			return 0

		return 0


	def close_conn(self):

		self.connection.close()

def main():

	main_conn = ConnectionAPI()

	while True:

		print("1.Register 2.Login 3.Get Data 4.Get all data  5.Exit")
		ch = input("Enter your choice:")
		if ch == "1":
			main_conn.post_into_user_metadata()		

		elif ch == "2":

			main_conn.check_user_credentials("'Ayush19_1'","Ayush@123")


		elif ch == "3":
			a = input("Enter your username: ")
			
			print(main_conn.get_user_data("username", f"'{a}'"))

		elif ch == "4":

			main_conn.get_user_metadata()

		else:
			main_conn.close_conn()
			break

