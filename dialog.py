# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QDoubleValidator

from ui_dialog import Ui_Dialog

class ventanaEmergente(QDialog):

    # Objeto de tipo signal que llega a la ventana original en forma de lista
    datos_enviar = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        # Variable para almacenar la ruta de la imagen seleccionada
        self.archivo_imagen = None

        # Conectar los botones
        self.ui.archivos.clicked.connect(self.seleccionar_imagen)

        # Configurar el validador para el campo de precio
        validador_precio = QDoubleValidator(0.0, 9999999999.99, 2, self)
        validador_precio.setNotation(QDoubleValidator.StandardNotation)
        self.ui.precio.setValidator(validador_precio)

        # Conectar los botones del QDialogButtonBox
        self.ui.botonesDialog.accepted.connect(self.enviar_datos)
        self.ui.botonesDialog.rejected.connect(self.cancelar)


    # Método para función de seleccionar imagen
    def seleccionar_imagen(self):
        # Abrir el diálogo para seleccionar una imagen
        buscar_archivo, _ = QFileDialog.getOpenFileName(
            self,
            "Seleccionar Imagen", #Título de la ventana
            "", #Directorio inicial
            "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)" # Filtro de archivos
        )

        if buscar_archivo:
            self.archivo_imagen = buscar_archivo
            # Mostrar la ruta en el QLabel
            self.ui.imagen_label.setText(f"Imagen selecionada: {buscar_archivo}")


    # Método que servira para interceptar la información y enviarla a la pagina inicial
    def enviar_datos(self):
        titulo = self.ui.titulo.text()
        descripcion = self.ui.descripcion.toPlainText()
        precio = self.ui.precio.text()

        # Crear lista con los datos
        datos = [titulo, float(precio), descripcion, self.archivo_imagen]

        # Emitir el signal con los datos
        self.datos_enviar.emit(datos)

        # Cerrar la ventana
        self.accept()

    def cancelar(self):
        # Cerrar la ventana sin hacer nada
        self.reject()


# if __name__ == "__main__":
#     pass
