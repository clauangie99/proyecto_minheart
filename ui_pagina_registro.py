# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina_registro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_pagina_registro(object):
    def setupUi(self, pagina_registro):
        if not pagina_registro.objectName():
            pagina_registro.setObjectName(u"pagina_registro")
        pagina_registro.resize(800, 600)
        self.logo_app = QLabel(pagina_registro)
        self.logo_app.setObjectName(u"logo_app")
        self.logo_app.setGeometry(QRect(20, 20, 261, 61))
        self.label = QLabel(pagina_registro)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(310, 110, 151, 41))
        self.label.setStyleSheet(u"font: 35pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.boton_login = QPushButton(pagina_registro)
        self.boton_login.setObjectName(u"boton_login")
        self.boton_login.setGeometry(QRect(260, 530, 281, 41))
        font = QFont()
        font.setBold(True)
        font.setKerning(True)
        self.boton_login.setFont(font)
        self.boton_login.setStyleSheet(u"border-radius: 15px;  /* Bordes redondeados */\n"
"border: 2px solid;  /* Borde del bot\u00f3n */\n"
"padding: 10px 20px;  /* Espaciado interno */\n"
"font-size: 16px;  /* Tama\u00f1o de la fuente */\n"
"")
        self.password_1 = QLineEdit(pagina_registro)
        self.password_1.setObjectName(u"password_1")
        self.password_1.setGeometry(QRect(460, 280, 250, 21))
        self.password_1.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.password_1.setReadOnly(False)
        self.label_2 = QLabel(pagina_registro)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(460, 250, 121, 21))
        self.label_2.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.boton_registro = QPushButton(pagina_registro)
        self.boton_registro.setObjectName(u"boton_registro")
        self.boton_registro.setGeometry(QRect(260, 440, 281, 41))
        font1 = QFont()
        font1.setBold(True)
        self.boton_registro.setFont(font1)
        self.boton_registro.setStyleSheet(u"border-radius: 15px;  /* Bordes redondeados */\n"
"border: 2px solid;  /* Borde del bot\u00f3n */\n"
"padding: 10px 20px;  /* Espaciado interno */\n"
"font-size: 16px;  /* Tama\u00f1o de la fuente */\n"
"")
        self.label_3 = QLabel(pagina_registro)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(460, 180, 191, 21))
        self.label_3.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.correo = QLineEdit(pagina_registro)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(460, 210, 250, 21))
        self.correo.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.label_4 = QLabel(pagina_registro)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 500, 211, 20))
        self.label_4.setStyleSheet(u"font: 15pt \"Lucida Grande\";\n"
"color: rgb(235, 247, 78);\n"
"")
        self.label_5 = QLabel(pagina_registro)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(460, 320, 231, 21))
        self.label_5.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.password_2 = QLineEdit(pagina_registro)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setGeometry(QRect(460, 350, 250, 21))
        self.password_2.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.password_2.setReadOnly(False)
        self.label_6 = QLabel(pagina_registro)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 180, 181, 31))
        self.label_6.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.nombre = QLineEdit(pagina_registro)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(60, 210, 250, 21))
        self.nombre.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.apellido = QLineEdit(pagina_registro)
        self.apellido.setObjectName(u"apellido")
        self.apellido.setGeometry(QRect(60, 280, 250, 21))
        self.apellido.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.label_7 = QLabel(pagina_registro)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 250, 181, 31))
        self.label_7.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(pagina_registro)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 320, 181, 31))
        self.label_8.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.telefono = QLineEdit(pagina_registro)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setGeometry(QRect(60, 350, 250, 21))
        self.telefono.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.label_9 = QLabel(pagina_registro)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(260, 410, 271, 20))
        self.label_9.setStyleSheet(u"font: \"Lucida Grande\";\n"
"color: rgb(255, 0, 0);")

        self.retranslateUi(pagina_registro)

        QMetaObject.connectSlotsByName(pagina_registro)
    # setupUi

    def retranslateUi(self, pagina_registro):
        pagina_registro.setWindowTitle(QCoreApplication.translate("pagina_registro", u"Form", None))
        self.logo_app.setText("")
        self.label.setText(QCoreApplication.translate("pagina_registro", u"Registro", None))
        self.boton_login.setText(QCoreApplication.translate("pagina_registro", u"Iniciar Sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("pagina_registro", u"Contrase\u00f1a:", None))
        self.boton_registro.setText(QCoreApplication.translate("pagina_registro", u"Registrarse", None))
        self.label_3.setText(QCoreApplication.translate("pagina_registro", u"Correo electr\u00f3nico:", None))
        self.label_4.setText(QCoreApplication.translate("pagina_registro", u"\u00bfYa cuentas con una cuenta?", None))
        self.label_5.setText(QCoreApplication.translate("pagina_registro", u"Confirmar contrase\u00f1a:", None))
        self.label_6.setText(QCoreApplication.translate("pagina_registro", u"Nombre(s):", None))
        self.label_7.setText(QCoreApplication.translate("pagina_registro", u"Apellidos:", None))
        self.label_8.setText(QCoreApplication.translate("pagina_registro", u"Tel\u00e9fono:", None))
        self.label_9.setText("")
    # retranslateUi

