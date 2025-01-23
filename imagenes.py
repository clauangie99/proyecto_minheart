# This Python file uses the following encoding: utf-8

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

# Creamos una clase que nos permitira manejar las imagenes
class Imagenes():
    @staticmethod
    # Creamos una función que nos permitira subir fotos y ajustarlas
    def insertar_imagen(imagen_a_subir, label):

        imagen = QPixmap(imagen_a_subir)

        # Adaptar el objeto del tamaño que establecimos para adaptar
        imagen_pixmap = imagen.scaled(
            label.width(),
            label.height(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
            )

        # Donde vamos a insertar ese QPixmap
        label.setPixmap(imagen_pixmap)

    @staticmethod
    # Creamos una función que nos permitira establecer una imagen como fondo en una ventana
    def imagen_fondo(ventana, imagen_a_subir):
        # ventana - Hace referencia a la ventana principal de la app

        ventana.setStyleSheet(f"""
        QMainWindow {{
            background-image: url({imagen_a_subir});
            background-repeat: no-repeat;
            background-position: center;
        }}
    """)



if __name__ == "__main__":
     pass
