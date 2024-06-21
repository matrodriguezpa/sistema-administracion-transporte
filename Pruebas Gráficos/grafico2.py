from PyQt5 import QtWidgets
from Ejemplo import Ui_MainWindow  # importa nuestro archivo generado
import sys
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
app = QtWidgets.QApplication([])
application = mywindow()
application.show()
sys.exit(app.exec())
