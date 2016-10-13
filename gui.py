import os, sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog
from PyQt5.QtGui import QPixmap

app = QApplication(sys.argv)

class window(QtWidgets.QWidget):	
	def __init__(self):
		super().__init__()
		self.init_ui()
	
	def init_ui(self):
		logo = QtWidgets.QLabel(self)
		logo.setGeometry(75, 10, 128, 128)
		logo.setPixmap(QPixmap(os.getcwd() + "/res/logo.png"))

		heading = QtWidgets.QLabel(self)
		heading.setText("Welcome to Eagle Eye")
		heading.move(75,0)

		importBtn = QPushButton(self)
		importBtn.setText("Import Video")
		importBtn.move(20,128)
		importBtn.clicked.connect(self.importBtn_clicked)
	
		camBtn = QPushButton(self)
		camBtn.setText("Use Webcam")
		camBtn.move(180,128)
		camBtn.clicked.connect(self.camBtn_clicked)

		label = QtWidgets.QLabel(self)
		label.setText("OR")
		label.move(140,128)

		self.setGeometry(100, 100, 300, 180)
		self.setWindowTitle("Eagle Eye")
		self.show()
		sys.exit(app.exec_())

	def importBtn_clicked(self):
		self.setGeometry(100, 100, 300, 280)
		self.camBtn.move(200,200)
		print ("import button was clicked")

	def camBtn_clicked():
		print ("webcam button was clicked")

if __name__ == '__main__':
	window()
