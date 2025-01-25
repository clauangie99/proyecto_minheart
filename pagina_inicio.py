# This Python file uses the following encoding: utf-8
import sys
import jwt
import requests

from PySide6.QtWidgets import QApplication, QFileDialog, QMainWindow, QVBoxLayout, QSizePolicy, QMessageBox, QScrollArea, QWidget, QLabel
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_pagina_inicio
from imagenes import Imagenes
from router import routerManager

from metodos import cargar_token
from metodos import decode_token
from metodos import caducidad_token
from metodos import eliminar_token

from dialog import ventanaEmergente
from widgetPortafolio import widgetProyecto

from qasync import QEventLoop
import asyncio

# Se declara una variable con el link que vamos a mandar la info.
url = "http://127.0.0.1:5000"

class pagina_inicio(QMainWindow):
    def __init__(self, nombre_user= "", client_id=None, parent=None):
        super().__init__(parent)
        # 1. Hace referencia al UI de nuestra página
        # Le indica de donde va a sacar el apartado gráfico
        self.ui = Ui_pagina_inicio()
        # De ese apartado gráfico lo inicializamos
        self.ui.setupUi(self)

        self.nombre_user = nombre_user

        # Primero, verificar si se pasa el nombre_user
        if self.nombre_user:
            self.ui.nombre.setText(str(self.nombre_user))
        elif client_id:
            nombre_usuario = self.obtener_nombre_usuario(client_id)
            if nombre_usuario:
                self.nombre_user = nombre_usuario
                self.ui.nombre.setText(nombre_usuario)
            else:
                self.ui.nombre.setText("Usuario no encontrado")
        else:
            self.ui.nombre.setText("Usuario no especificado")

        # Editar foto de perfil
        #self.editar_perfil() # nuevo objeto con el atributo
        self.ui.editar_foto.clicked.connect(self.editar_perfil)

        # Cargar la foto de perfil al iniciar
        self.cargar_foto_perfil()

        # Nuevo objeto con el atributo routerManager
        self.router_manager = routerManager()

        # Nuevo objeto acceder al QTextEditor
        self.editor_descripcion = self.ui.descripcion
        self.editor_descripcion.textChanged.connect(self.texto_descripcion) #Conectar señales

        # Vamos a que ejecute la funcion "insertar_imagen" para insertar el logo
        imagen_logo = Imagenes.insertar_imagen("imagenes/logo_lb.png", self.ui.logo_app)
        Imagenes.imagen_fondo(self, "imagenes/fondo_dos.png") # Vamos a que se ejecute la funcion "imagen_fondo"

        # Boton que deseamos que se seleccione: cerrar_sesion
        # Se conecta para identificar si se hizo clic
        # Conectado a la función/método acceder_login a nuestro objeto router_manager
        # Llevara un parametro que cierra la ventana anterior
        self.ui.cerrar_sesion.clicked.connect(self.cerrar_sesion)

        # Boton que deseamos conectar para abrir la ventana emergente
        self.ui.nuevo_proyecto.clicked.connect(self.abrir_ventana)

        ## widgetProyecto()
        # widget personalizado de widgetPortafolio
        self.scroll_widget = QWidget()

        # Creamos el layout para los proyectos
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setAlignment(Qt.AlignTop)

        #Configurar el QScrollArea con mi widget
        self.ui.contenedor.setWidget(self.scroll_widget)
        self.ui.contenedor.setWidgetResizable(True)
        self.ui.contenedor.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.ui.contenedor.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Configurar el widget contenedor
        self.scroll_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)

        # Imprimir la altura calculada del layout para depuración
        print("Altura calculada del layout:", self.scroll_layout.sizeHint().height())
        for i in range(self.scroll_layout.count()):
            item = self.scroll_layout.itemAt(i)
            print(f"Widget {i}: sizeHint={item.widget().sizeHint().height()}")

############### MÉTODOS ###############

    # Método para editar la foto de perfil
    def editar_perfil(self):
        try:
            # Abrir un dialog para seleccionar la imagen
            buscar_archivo, _ = QFileDialog.getOpenFileName(
                self,
                "Seleccionar Imagen", #Título de la ventana
                "", #Directorio inicial
                "Imágenes (*.png *.jpg *.jpeg *.bmp *.gif)" # Filtro de archivos
            )

            if buscar_archivo:
                # Usar el nombre de usuario guardado en la clase
                if not self.nombre_user or self.nombre_user in ["Usuario no encontrado", "Usuario no especificado"]:
                    QMessageBox.warning(self, "Error", "No hay un usuario válido")
                    return

                with open(buscar_archivo, "rb") as file:
                    # Preparar los datos para la petición
                    files = {"foto": (os.path.basename(buscar_archivo), file, "image/jpeg")}
                    data = {"usuario": self.nombre_user}

                    response = requests.post(url+"/api/items/uploads", files=files, data=data)

                    if response.status_code == 200:
                        pixmap = QPixmap(buscar_archivo)
                        pixmap = pixmap.scaled(
                            self.ui.foto_perfil.width(),
                            self.ui.foto_perfil.height(),
                            Qt.KeepAspectRatio,
                            Qt.SmoothTransformation
                        )
                        # Actualizar el QLabel con la imagen seleccionada
                        self.ui.foto_perfil.setPixmap(pixmap)
                        self.ui.foto_perfil.setScaledContents(True)

                        # Mostrar mensaje de éxito
                        QMessageBox.information(self,"Exito", "Foto de perfil actualizada")

                    else:
                        # Mostrar mensaje de erro si algo falla
                        erro_msg = response.json().get("error", "error desconocido")
                        QMessageBox.warning(self, "Error", f"No se pudo actualizar la foto de perfil: {error_msg}")

        except Exception as e:
            QMessageBox.critical(self,
                                "Error",
                                f"Error al procesar la imagen: {str(e)}")


    # Agregar este método para cargar la foto de perfil al iniciar la aplicación
    def cargar_foto_perfil(self):
        try:
            if not self.nombre_user or self.nombre_user in ["Usuario no encontrado", "Usuario no especificado"]:
                print("No hay usuario válido para cargar la foto")
                return

            response = requests.get(f"{url}/api/items/downloads/{self.nombre_user}")

            if response.status_code == 200:
                # Crear un QPixmap desde los datos de la imagen
                pixmap = QPixmap()
                pixmap.loadFromData(response.content)

                # Escalar la imagen
                pixmap = pixmap.scaled(
                    self.ui.foto_perfil.width(),
                    self.ui.foto_perfil.height(),
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )

                # Establecer la imagen en el QLabel
                self.ui.foto_perfil.setPixmap(pixmap)
                self.ui.foto_perfil.setScaledContents(True)
            else:
                print(f"No se pudo cargar la foto de perfil. Código: {response.status_code} ")

        except Exception as e:
            print(f"Error al cargar la foto de perfil: {str(e)}")

    # Método para obtener el nombre de usuario a insertar en label
    def obtener_nombre_usuario(self, nombre):
        # Aquí haces la consulta a la base de datos para obtener el nombre del usuario
        try:
            conexion = conectar_db()
            with conexion.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT nombre FROM users WHERE nombre = %s", (nombre,))
                usuario = cursor.fetchone()
                if usuario:
                    return usuario["nombre"]
            return None
        except Exception as e:
            print(f"Error al obtener el nombre del usuario: {e}")
            return None


    # Método para modificar texto de descripcion
    def texto_descripcion(self):
        # Leer el texto actual del QTextEdit
        texto_actual = self.editor_descripcion.toPlainText()
        print("Texto modificado:", texto_actual)

    # Método para abrir la ventana emergente de dialog
    def abrir_ventana(self):
        # Crear atributo que sea un objeto de mi dialog
        self.ventana = ventanaEmergente(self)

        # Conectar el signal de la ventana emergente al método recibir_datos
        self.ventana.datos_enviar.connect(self.recibir_datos)

        # Mostramos la ventana y se ejecuta con exec (de execute)
        self.ventana.exec()

    # Método para recibir la información
    def recibir_datos(self, datos):
        # Crear un widget de proyecto con los datos recibidos
        titulo, precio, descripcion, imagen = datos
        try:
            # Asegurarse de que el precio sea un número (float)
            precio = float(precio)
        except ValueError:
            # Si el precio no es un número válido, podemos manejar el error
            print(f"Error al convertir el precio: {precio}")
            precio = 0.0  # Establecer un valor predeterminado o manejar el error

        print(f"Información recibida: {datos}")

        nuevo_proyecto = widgetProyecto(titulo, precio, str(descripcion), imagen)
        self.scroll_layout.addWidget(nuevo_proyecto)

        # Forzar actualización
        self.scroll_widget.updateGeometry()
        self.ui.contenedor.viewport().update()

        # Debug info
        print(f"Número de widgets en el layout: {self.scroll_layout.count()}")
        print(f"Altura del scroll widget: {self.scroll_widget.height()}")


    def cerrar_sesion(self):

        eliminar_token()
        # Esta linea de código nos ayuda a enviar al usuario a la nueva_ventana (login)
        # El parametro de ventana_anterior tiene "self" porque hace referencia al objeto
        self.router_manager.acceder_login(ventana_anterior=self)

# Determinar si el usuario está ejecutandose este archivo
if __name__ == "__main__":


    # Tenemos que determinar el estado de mi token
    token_actual = cargar_token()

    # Decodificando la información del token
    payload_token = decode_token(token_actual)

    if payload_token:
        valido = caducidad_token(payload_token["exp"])

    else:
        valido = None

    router_manager = routerManager()

    # Primero creamos una aplicación (el lienzo/canva)
    app = QApplication(sys.argv)

    loop = QEventLoop(app)

    # Crear el entorno asíncrono para nuestra app
    asyncio.set_event_loop(loop)

    # Creamos la vista de esa aplicación
    widget = pagina_inicio()

    # Mostramos la aplicación
    # widget.show()

    if valido:

        # Si el token es válido el administrador de rutas hace que
        # el usuario acceda a la página principal
        print("Se carga la pagina pagina_inicio")
        print(payload_token)

        nombre = payload_token["sub"]
        widget = pagina_inicio(nombre_user=nombre)
        router_manager.acceder_inicio(widget, nombre)
    else:
        # Si el token es inválido el administrador de rutas hace que el usuario
        # Acceda a la pagina login
        print("Se carga login")
        router_manager.acceder_login(widget)

    with loop:
        loop.run_forever()

    sys.exit(app.exec())

