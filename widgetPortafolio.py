# This Python file uses the following encoding: utf-8
from PySide6.QtWidgets import QWidget, QSizePolicy, QComboBox, QLabel, QVBoxLayout
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


from ui_widgetPortafolio import Ui_Form


class widgetProyecto(QWidget):
    def __init__(self, titulo = "", precio=0.0, descripcion="", imagen=None, parent=None):
        super().__init__(parent)

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.imagen = imagen


        # Configuración de tamaño y política
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.setMinimumHeight(250)  # Ajusta este valor según el tamaño que necesites
        self.setMaximumHeight(250)  # Mantener altura fija

        # Asegurarse de que el precio sea un número (float)
        precio = float(precio)

        # Se establecen los valores a los widgets
        self.ui.widget_titulo.setText(titulo)
        self.ui.widget_precio.setText(f"${precio:.2f}")
        self.ui.widget_descripcion.setText(str(descripcion))
        self.ui.widget_imagen.setFixedSize(200, 200)  # Ajusta el tamaño de la imagen

        if self.imagen:
            print(f"Intentando cargar la imagen desde: {self.imagen}")
            pixmap = QPixmap(self.imagen)
            if pixmap.isNull():
                print("Error al cargar la imagen. La ruta podría ser incorrecta.")
            else:
                print("Imagen cargada correctamente.")
                self.ui.widget_imagen.setPixmap(pixmap.scaled(
                    self.ui.widget_imagen.width(),
                    self.ui.widget_imagen.height(),
                    Qt.AspectRatioMode.KeepAspectRatio
                ))
        else:
            self.ui.widget_imagen.setText("Sin Imagen")

        # Conectar el QComboBox
        self.ui.comboBox.currentIndexChanged.connect(self.on_selection_changed)


    def on_selection_changed(self):
        selected_item = self.combo_box.currentText()



# if __name__ == "__main__":
#     pass
