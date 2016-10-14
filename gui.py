"""
 Course: CST 205 @ CSU Monterey Bay
 Author: Babak Chehraz
 Abstract: This program simply displays a GUI that allows the user to either select a path
 to a video file or use their webcam instead. Then, it will launch tracking.py, the opencv
 project itself.
"""
import os, sys, tracking
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
		print ("import button was clicked")
		d = QtWidgets.QFileDialog(self)
		d.setFileMode(QtWidgets.QFileDialog.AnyFile)
		d.selectNameFilter("AVI video files only! (*.*)")
		filename = "g"	
		if d.exec_():
			filename = d.selectedFiles()
		print (filename)
		tracking.play(True, filename, 1)
		

	def camBtn_clicked(self):
		print ("webcam button was clicked")
		tracking.play(False, 0, 0)

if __name__ == '__main__':
	window()
