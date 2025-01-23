# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_pagina_registro import Ui_pagina_registro
from imagenes import Imagenes
from router import routerManager
from metodos import registrar_user

class pagina_registro(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        # 1. Hace referencia al UI de nuestra página
        # Le indica de donde va a sacar el apartado gráfico
        self.ui = Ui_pagina_registro()

        # De ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)

        # Objeto de la clase routerManager
        self.router_manager = routerManager()

        # Vamos a que ejecute la funcion "insertar_imagen"
        imagen_logo = Imagenes.insertar_imagen("imagenes/logo_lb.png", self.ui.logo_app)

        # Vamos a que se ejecute la funcion "imagen_fondo"
        Imagenes.imagen_fondo(self, "imagenes/fondo_tres.png")

        # Boton de registro para validar datos
        self.ui.boton_registro.clicked.connect(self.validar_datos)

        # Boton para mandar a login
        self.ui.boton_login.clicked.connect(self.mandar_login)

    # Función que verifica que ningun dato falte y/o este mal
    def validar_datos(self):
        # Creando variables con nuestros objetos para sacar el texto ingresado en ellos
        nombre = self.ui.nombre.text() # Texto de Nombre
        apellido = self.ui.apellido.text() # Texto de Apellido
        telefono = self.ui.telefono.text() # Texto de telefono
        correo = self.ui.correo.text() # Texto del correo
        password_1 = self.ui.password_1.text() # Texto del primer password
        password_2 = self.ui.password_2.text() # Texto del segundo password

        # PASOS DE VALIDACIÓN
        # 1.- Asegurarnos que ningún parámetro este vacío
        # 1.1.- Si alguno viene vacío, tenemso que generar un error
        # Con que 1 no cumpla con la condición, entre el mensaje de error
        if len(nombre) <= 0 or len(apellido) <= 0 or len(telefono) <= 0 or len(password_1) <= 0:
            print("Error: Datos faltantes")
            self.ui.error.setText("Error: Datos faltantes")

        # 2. - El correo que ingrese el usuario se válido
        # 2.2.- Si no es válido, generamos un error
        elif "@" not in correo and "." not in correo:
            print("Error: Correo no válido")
            self.ui.error.setText("Error: Correo no válido")

        # 3.- Que ambas contraseñas coincidan
        # 3.3.- Si alguna de las contraseñas no coinciden que generar un error
        elif password_1 != password_2:
            print("Error: Contraseñas no coinciden")
            self.ui.error.setText("Error: Contraseñas no coinciden")

        else:
            print("Todos los datos son correctos")
            resultado = registrar_user(nombre, apellido, telefono, correo, password_1)

            # Si se cumple, significa que tenemos un usuario previamente registrado
            if "Error" in resultado:
                self.ui.error.setText("El usuario ya está registrado")

            else:
                # Si toda su información es válida, se guarda en DB y se redirige a login para iniciar sesión
                # Lo manda a la ventana de Iniciar Sesión
                self.mandar_login()

    # Función de mandar al usuario a Login
    def mandar_login(self):
        self.router_manager.acceder_login(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = pagina_registro()
    widget.show()
    sys.exit(app.exec())
