import mysql.connector as mysql


class connection_api:

	def __init__(self):

		self.connection = mysql.connect(user='root',password='ayush123')

		self.cursor = self.connection.cursor()
		self.cursor.execute("use inventory_man")
		self.post_into_user_metadata()
		self.get_user_metadata()
		self.close_conn()

	def get_user_metadata(self):

		self.cursor.execute("select * from user_data")

		l = [x for x in self.cursor]
		print(l)

	def post_into_user_metadata(self):

		l = (input("Enter your name: "), input("Enter your username: "), input("Enter a password: ") ,input("Enter your email-id: "))
		self.cursor.execute("insert into user_data values(%s,%s,%s,%s)",l)

	def close_conn(self):

		self.connection.close()

def main():

	main_conn = connection_api()


if __name__ == "__main__":

	main()


