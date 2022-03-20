import mysql.connector as mysql


class connection_api:

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

		except mysql.errors.IntegrityError:

			print("User Name already exists!!")


	def close_conn(self):

		self.connection.close()

def main():

	main_conn = connection_api()

	while True:

		print("1.Register 2.Login 3.Get Data 4.Get all data  5.Exit")
		ch = input("Enter your choice:")
		if ch == "1":
			main_conn.post_into_user_metadata()		

		elif ch == "2":

			main_conn.check_user_credentials("'Ayush19_1'","Ayush@123")

		elif ch == "3":

			print(main_conn.get_user_data("name", "'Ayush Sharma'"))

		elif ch == "4":

			main_conn.get_user_metadata()

		else:
			main_conn.close_conn()
			break

if __name__ == "__main__":

	main()


