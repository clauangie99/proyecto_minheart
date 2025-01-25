import requests # Librería para consumir datos de internet
import json # libreria que nos permite convertir el string al tradicional
import os
import sys
import jwt # Hay que descargarlo
import datetime # Reconocer si el token expiro o no
import asyncio
import httpx # Hay que descargarlo
import aiohttp # Hay que descargarlo
import aiofiles # Hay que descargarlo

from PySide6.QtWidgets import QApplication, QFileDialog

# Se declara una variable con el link que vamos a mandar la info.
url = "http://127.0.0.1:5000"

# Esta función elimina el token
def eliminar_token():
    with open("token.txt", "w") as file:
        # Dentro del archivo, se guardara el token
        # Va abrir el archivo y se va reescribir en 0 caracteres
        file.write("")


# Esta función determine la caducidad del token
def caducidad_token(expiracion):
    # Vamos a traducir la fecha
    fecha_expiracion = datetime.datetime.fromtimestamp(expiracion)

    return fecha_expiracion > datetime.datetime.now()
    # Si es mayor (True), significa que mi token sigue siendo válido
    # Si es menor (False), significa que mi token ya caduco


# Esta función decodifica el token
def decode_token(token):

    # Verificando si existe un token que decodifica
    if token:
        # Crear una variable
        # Decodificamos el playload del token
        payload = jwt.decode(token, options={"verify_signature": False}) # Este valor viene en la documentacion de pywt

        # Retornamos el payload decodificado
        return payload

    return None

# Funcion que carge el archivo txt y obtenga el token
def cargar_token():
    # Primero, comprobamos si el archivo "token.txt" sí existe. ("r" es modo de lectura)
    if os.path.exists("token.txt"):
        # El archivo existe

        # Abrimos el archivo y retornamos su contenido (el token)
        with open("token.txt", "r") as file:

            contenido = file.read()
            # Como si mi archivo donde se guarda el token esta vacio
            if len(contenido) == 0:
                return None

            return contenido

    else:
        # El archivo no existe y retornamos vacío
        return None


# Esta función crea un archivo en donde se almacena el token
async def crear_archivo_token(token):
    # Abrira un archivo. Si NO existe, lo va a crear. ("w" es modo de escritura)

    async with aiofiles.open("token.txt", "w") as file:
        # Dentro del archivo, se guardara el token
        await file.write(token)

# Esta función nos ayudará a crear usuarios y guardarlos en un DB
def registrar_user(nombre, apellido, telefono, correo, password):

    # Diccionario que contendra la info que se registrara en mi base de datos
    info_enviar = {
        "nombre": nombre + " " + apellido,
        "telefono": telefono,
        "correo": correo,
        "password": password

    }

    print(info_enviar)
    # Creamos una variable llamada "respuesta"
    # Nos permite enviar información, a la ruta especifica, y con la inf a enviar.
    respuesta = requests.post(url+"/registro", data=info_enviar)

    respuesta_string = respuesta.content.decode("utf-8")
    respuesta_diccionario = json.loads(respuesta_string)
    return respuesta_diccionario

async def login_user(correo, password):

    # Diccionario que mandara info a la base de datos
    info_recibir = {
        "correo": correo,
        "password": password

    }
    print(info_recibir)

    async with httpx.AsyncClient() as cliente:
        respuesta = await cliente.post(url+"/login", data=info_recibir)

    respuesta_string = respuesta.content.decode("utf-8")

    respuesta_diccionario = json.loads(respuesta_string)

    if "Token" in respuesta_diccionario:

        # Se crea el archivo "token.txt" y dentro se guarda el token generado
        await crear_archivo_token(respuesta_diccionario["Token"])

    return respuesta_diccionario

if __name__ == "__main__":
    # Creamos variable en donde cargamos el token que se genero
    token_actual = cargar_token()

    # Decodificamos la información del token que nos genero
    payload_token = decode_token(token_actual)

    valido = caducidad_token(payload_token["exp"])
    print(valido)
