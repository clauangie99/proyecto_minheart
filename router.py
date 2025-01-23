# IMPORTANT: Este archivo nos ayudará a manejar las rutas

# This Python file uses the following encoding: utf-8
from PySide6.QtCore import QObject

# Para realizar cambio de ventana "a" a ventana "b"
class routerManager():
    def __init__(self):

        # La ventana_actual nos ayudara a determinar desde que ventana venimos(estamos actual)
        self.ventana_actual = None

    # Acceder a ventana_login (pagina_login)
    def acceder_login(self, ventana_anterior = None):
        # Desde el archivo, importamos la clase
        from pagina_login import pagina_login
        # Creamos objeto de la nueva_ventana que queremos mostrar
        self.ventana_actual = pagina_login()

        # En el objeto, aplicamos el método show para mostrar la ventana
        self.ventana_actual.show()

        # Cerramos la ventana anterior (de la que veniamos)
        #ventana_anterior.close()
        if ventana_anterior is not None:
            print(f"Cerrando ventana anterior: {ventana_anterior}")
            ventana_anterior.close()
        else:
            print("Advertencia: ventana_anterior es None. No se cerrará ninguna ventana.")



    # Acceder a ventana_registro (pagina_registro)
    def acceder_registro(self, ventana_anterior = None):
        # Desde el archivo, importamos la clase
        from pagina_registro import pagina_registro
        # Creamos objeto de la nueva_ventana que queremos mostrar
        self.ventana_actual = pagina_registro()

        # En el objeto, aplicamos el método show para mostrar la ventana
        self.ventana_actual.show()

        # Cerramos la ventana anterior (de la que veniamos)
        ventana_anterior.close()


    # Acceder a ventana pagina_inicio (main)
    def acceder_inicio(self, ventana_anterior = None, nombre_user = "", client_id=None):
        # Desde el archivo, importamos la clase
        from pagina_inicio import pagina_inicio
        # Creamos objeto de la nueva_ventana que queremos mostrar
        self.ventana_actual = pagina_inicio(nombre_user=nombre_user, client_id=client_id)

        # En el objeto, aplicamos el método show para mostrar la ventana
        self.ventana_actual.show()

        # Cerramos la ventana anterior (de la que veniamos)
        ventana_anterior.close()
