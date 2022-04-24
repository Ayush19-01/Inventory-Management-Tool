import mysql.connector as mysql

class UserTableInstance:

	def __init__(self, username):

		self.connection = mysql.connect(user='root',password='ayush123')
		self.cursor = self.connection.cursor()
		self.cursor.execute("use inventory_man")
		self.extract_data(username[1:-1])
		
	def extract_data(self,username):

		self.cursor.execute(f"select * from {username}")
		self.data = self.cursor.fetchall()
		print(self.data)


	#def add_data(self, usrname):


	#def modify_data(self, username):


class ConnectionAPI:

	def __init__(self):

		self.connection = mysql.connect(user='root',password='ayush123')

		self.cursor = self.connection.cursor()
		self.cursor.execute("use inventory_man")
		

	def commit_changes(self):

		self.cursor.execute("commit")


	
	def check_user_credentials(self,username,password):

		x = self.get_user_data("username", username)

		if x[0][2] == password:
			print("Access Granted")
			self.close_conn()
			self.user_table_instance = UserTableInstance(username)

		else:
			print("incorrect credentials")



	def get_user_data(self, field, key_data):

		self.cursor.execute(f"select * from user_data where {field} = {key_data}")
		l = self.cursor.fetchall()
		return l



	def get_user_metadata(self):

		self.cursor.execute("select * from user_data")

		l = self.cursor.fetchall()
		print(l)




	def post_into_user_metadata(self):

		
		l = (input("Enter your name: "), input("Enter your username: "), input("Enter a password: ") ,input("Enter your email-id: "))
		

		try:
			self.cursor.execute("insert into user_data values(%s,%s,%s,%s)",l)

			self.commit_changes()

			self.inventory_creation(l[1])

		except mysql.errors.IntegrityError as err:

			print(err)

			print("User Name already exists!!")

	def inventory_creation(self, usr):

		self.connection.execute(f"create table {usr} (id int primary key, item_name varchar(100) not null, purchase_date datetime not null, reference_id int unique not null, quantity int not null, price_per_unit float(20,4)) not null, total_price float(30,4)")

		self.commit_changes()



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

if __name__ == "__main__":

	main()


