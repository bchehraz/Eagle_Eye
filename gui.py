import os,sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtGui

def window():
	app = QApplication(sys.argv)
	win = QtGui.QWidget()

	logo = QtGui.QLabel(win)
	logo.setGeometry(10, 10, 400, 400)
	logo.setPixmap(QtGui.QPixmap(os.getcwd() + "/res/Eagle_i.png"))

	heading = QtGui.QLabel(win)
	heading.setText("Welcome to Eagle Eye")
	heading.move(75,0);

	importBtn = QPushButton(win)
	importBtn.setText("Import Video")
	importBtn.move(20,50)
	importBtn.clicked.connect(importBtn_clicked)
	
	camBtn = QPushButton(win)
	camBtn.setText("Use Webcam")
	camBtn.move(180,50)
	camBtn.clicked.connect(camBtn_clicked)

	label = QtGui.QLabel(win)
	label.setText("OR")
	label.move(140,50)

	win.setGeometry(100,100,300,100)
	win.setWindowTitle("Eagle Eye")
	win.show()
	sys.exit(app.exec_())

def importBtn_clicked():
	#lineEdit.setText(QFileDialog.getOpenFileName())
	self.fileDialog = QtGui.QFileDialog(self)
	self.fileDialog.show()
	print "import button was clicked"

def camBtn_clicked():
	print "webcam button was clicked"

if __name__ == '__main__':
	window()

