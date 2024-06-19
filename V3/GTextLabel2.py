from PyQt5 import QtWidgets, QtGui,QtCore
from TextLabel import Ui_MainWindow
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('Verdana', 50))
        self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200)) # cambio de la geometría del label
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
