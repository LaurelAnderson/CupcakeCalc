from PyQt5.QtWidgets import QApplication
from CalcWindow import *

#Main app window for the cupcake calculater, setting up the Qt applicaiton 

app = QApplication([])
window = CalcWindow()
window.show()
app.exec_()
