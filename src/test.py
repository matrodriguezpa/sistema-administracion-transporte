import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        # Configuración inicial de la ventana
        self.setWindowTitle('Ejemplo Interactivo en PyQt5')
        self.setGeometry(100, 100, 300, 200)

        # Crear un botón
        self.button = QPushButton('Haz clic aquí', self)
        self.button.clicked.connect(self.on_button_click)  # Conectar la señal clicked al método on_button_click

        # Configurar el layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def on_button_click(self):
        # Cambiar el texto del botón cuando se hace clic
        self.button.setText('¡Has hecho clic!')
        # Opcional: Desactivar el botón después de hacer clic
        self.button.setEnabled(False)

# Configuración de la aplicación
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
