from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from cupCalc import *

#This is the view controller for the cupcake calculater

class CalcWindow(QMainWindow): 

	def __init__(self): 
		super(CalcWindow, self).__init__()
		
		#set model 
		self.model = CupcakeModel()
		
		#set a generic central widget
		widget = QWidget()
		self.setCentralWidget(widget) 
		
		#set the size of the window
		self.setFixedWidth(600) 
		self.setFixedHeight(600)
		
		#create a exit 
		menu = self.menuBar().addMenu("&Menu")
		quitAct = QAction("E&xit", self, shortcut=QKeySequence.Quit, triggered=self.close)
		menu.addAction(quitAct)		
		
		#set title 
		self.setWindowTitle("Cupcake Calculator")
		
		#set text
		self.label_1 = QLabel('Input Stuff', self)
		self.label_1.move(20, 20)
	
		#create a textbox
		self.textbox_1 = QLineEdit(self)
		self.textbox_1.move(20, 50)
		self.textbox_1.resize(280,40)
		
		#create a button to calculate
		self.calc_button = QPushButton('Calculate', self)
		self.calc_button.move(20,100)
		
		#call the new reset
		self.start()
		
	def start(self):
	
		print("Starting!")
		
		self.model.start()
		
	
	
	
	
	
	
	
	
	
	
	
	
	
		

