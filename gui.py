import os,sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QPushButton,QDialog
from PyQt5.QtGui import QPixmap

def window():
	app = QApplication(sys.argv)
	win = QtWidgets.QWidget()

	logo = QtWidgets.QLabel(win)
	logo.setGeometry(75, 10, 128, 128)
	logo.setPixmap(QPixmap(os.getcwd() + "/res/logo.png"))

	heading = QtWidgets.QLabel(win)
	heading.setText("Welcome to Eagle Eye")
	heading.move(75,0)

	importBtn = QPushButton(win)
	importBtn.setText("Import Video")
	importBtn.move(20,128)
	importBtn.clicked.connect(importBtn_clicked)
	
	#eBox = QLineEdit()
	#eBox.setMaxLength(200)
	#eBox.setAlignment(Qt.AlignLeft)
	#eBox.setFont(QFont("Arial", 14))
	#eBox.setReadOnly(False)
	#eBox.setInputMask("")
	#eBox.setGeometry(50, 50, 50, 50)
	
	camBtn = QPushButton(win)
	camBtn.setText("Use Webcam")
	camBtn.move(180,128)
	camBtn.clicked.connect(camBtn_clicked)

	label = QtWidgets.QLabel(win)
	label.setText("OR")
	label.move(140,128)

	win.setGeometry(100, 100, 300, 180)
	win.setWindowTitle("Eagle Eye")
	win.show()
	sys.exit(app.exec_())

def importBtn_clicked(self):
	win2 = QtWidgets.QWidget()
	win2.setGeometry(100,100,300,280)
	win2.setWindowTitle("Eagle Eye")
	win2.show()
	print ("import button was clicked")

def camBtn_clicked():
	print ("webcam button was clicked")

if __name__ == '__main__':
	window()
