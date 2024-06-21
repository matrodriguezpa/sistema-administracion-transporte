from PyQt5 import QtWidgets, QtGui
from TextLabel import Ui_MainWindow
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) 
        self.ui.label.setFont(QtGui.QFont('SansSerif', 14)) # Cambia el tipo de letra y su tamaño
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
