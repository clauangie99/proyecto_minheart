# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_pagina_login import Ui_pagina_login
from imagenes import Imagenes
from router import routerManager

from metodos import login_user
from metodos import cargar_token
from metodos import decode_token

import time
import asyncio
from qasync import asyncSlot

class pagina_login(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 1. Hace referencia al UI de nuestra página
        # Le indica de donde va a sacar el apartado gráfico
        self.ui = Ui_pagina_login()
        # De ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)

        # Nuevo objeto con el atributo routerManager
        self.router_manager = routerManager()

        # Vamos a que ejecute la funcion "insertar_imagen"
        imagen_logo = Imagenes.insertar_imagen("imagenes/logo_lb.png", self.ui.logo_app)

        # Vamos a que se ejecute la funcion "imagen_fondo"
        Imagenes.imagen_fondo(self, "imagenes/fondo_uno.png")

        # Conectamos los botones
        # Boton para registrarte
        self.ui.boton_registro.clicked.connect(self.mandar_registro)

        # Iniciamos sesión con el usuario
        self.ui.boton_login.clicked.connect(self.manejar_inicio_asincrono)

    # Método envia al usuario a la ventana "pagina_registro"
    def mandar_registro(self):
        # Esta linea de código nos ayuda a enviar al usuario a la nueva_ventana (registro)
        # El parametro de ventana_anterior tiene "self" porque hace referencia al objeto
        self.router_manager.acceder_registro(ventana_anterior=self)

    @asyncSlot()
    async def manejar_inicio_asincrono(self):
        await self.iniciar_sesion()

    # Inicia sesión y manda al usuario a la pagina de inicio
    async def iniciar_sesion(self):

## await
        self.ui.error.setText("")
        correo = self.ui.correo.text()
        password = self.ui.password.text()

        self.ui.cargando.setText("Cargando...")
        respuesta = await login_user(correo, password)
        self.ui.cargando.setText("")

        respuesta = await login_user(correo, password)
        print(respuesta)

        # Variable para cargar token del inicio de sesion
        mi_token = cargar_token()
        print(f"El token es: {mi_token}")

        # Va codificar el token guardado en la variable 'mi_token'
        datos_token = decode_token(mi_token)
        print(respuesta)

        # Se inicia sesión y se va cargar el objeto 'sub', donde viene el nombre del usuario
        if "Token" in respuesta:
            self.router_manager.acceder_inicio(self, datos_token["sub"])

        else:
            self.ui.error.setText("El correo o contraseña no coinciden.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = pagina_login()
    widget.show()
    sys.exit(app.exec())
