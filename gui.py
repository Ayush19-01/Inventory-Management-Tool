from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class MainWindow(QMainWindow):

	#init window
	def __init__(self):

		super(MainWindow, self).__init__()
		self.setGeometry(200, 200, 300,  300)
		self.setWindowTitle("Inventory Management")
		self.initUI()

	#init content
	def initUI(self):

		
		self.label = QtWidgets.QLabel(self)
		self.label.setText("Heading 1")
		self.label.move(50,50)

		self.b1 = QtWidgets.QPushButton(self)
		self.b1.setText("Exit")
		self.b1.clicked.connect(self.clicked)

	
	#button functionality
	def clicked(self):

		self.label.setText("Button pressed which means this program will deffo work!!!")
		self.update()

	#update all sizes
	def update(self):

		self.label.adjustSize()




def clicked():

	print("clicked")


def window():

	app = QApplication(sys.argv)
	
	win = MainWindow()
	
	#show window
	win.show()
	sys.exit(app.exec_())

window()