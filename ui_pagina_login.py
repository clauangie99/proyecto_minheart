# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pagina_login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_pagina_login(object):
    def setupUi(self, pagina_login):
        if not pagina_login.objectName():
            pagina_login.setObjectName(u"pagina_login")
        pagina_login.resize(800, 600)
        self.centralwidget = QWidget(pagina_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.titulo = QLabel(self.centralwidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(270, 100, 271, 40))
        self.titulo.setStyleSheet(u"font: 35pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.logo_app = QLabel(self.centralwidget)
        self.logo_app.setObjectName(u"logo_app")
        self.logo_app.setGeometry(QRect(20, 20, 261, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(270, 155, 191, 21))
        self.label.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(270, 250, 121, 16))
        self.label_2.setStyleSheet(u"font: 20pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);")
        self.correo = QLineEdit(self.centralwidget)
        self.correo.setObjectName(u"correo")
        self.correo.setGeometry(QRect(270, 190, 250, 21))
        self.correo.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.password = QLineEdit(self.centralwidget)
        self.password.setObjectName(u"password")
        self.password.setEnabled(True)
        self.password.setGeometry(QRect(270, 280, 250, 21))
        self.password.setStyleSheet(u"border-radius: 5px;  /* Bordes redondeados */")
        self.password.setReadOnly(False)
        self.boton_login = QPushButton(self.centralwidget)
        self.boton_login.setObjectName(u"boton_login")
        self.boton_login.setGeometry(QRect(260, 370, 281, 41))
        font = QFont()
        font.setBold(True)
        font.setKerning(True)
        self.boton_login.setFont(font)
        self.boton_login.setStyleSheet(u"border-radius: 15px;  /* Bordes redondeados */\n"
"border: 2px solid;  /* Borde del bot\u00f3n */\n"
"padding: 10px 20px;  /* Espaciado interno */\n"
"font-size: 16px;  /* Tama\u00f1o de la fuente */\n"
"")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(280, 440, 251, 20))
        self.label_3.setStyleSheet(u"font: 15pt \"Lucida Grande\";\n"
"color: rgb(235, 247, 78);\n"
"")
        self.boton_registro = QPushButton(self.centralwidget)
        self.boton_registro.setObjectName(u"boton_registro")
        self.boton_registro.setGeometry(QRect(260, 470, 281, 41))
        font1 = QFont()
        font1.setBold(True)
        self.boton_registro.setFont(font1)
        self.boton_registro.setStyleSheet(u"border-radius: 15px;  /* Bordes redondeados */\n"
"border: 2px solid;  /* Borde del bot\u00f3n */\n"
"padding: 10px 20px;  /* Espaciado interno */\n"
"font-size: 16px;  /* Tama\u00f1o de la fuente */\n"
"")
        self.cargando = QLabel(self.centralwidget)
        self.cargando.setObjectName(u"cargando")
        self.cargando.setGeometry(QRect(277, 330, 241, 20))
        self.error = QLabel(self.centralwidget)
        self.error.setObjectName(u"error")
        self.error.setGeometry(QRect(280, 320, 231, 20))
        self.error.setStyleSheet(u"color: rgb(255, 0, 8);")
        pagina_login.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(pagina_login)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        pagina_login.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pagina_login)
        self.statusbar.setObjectName(u"statusbar")
        pagina_login.setStatusBar(self.statusbar)

        self.retranslateUi(pagina_login)

        QMetaObject.connectSlotsByName(pagina_login)
    # setupUi

    def retranslateUi(self, pagina_login):
        pagina_login.setWindowTitle(QCoreApplication.translate("pagina_login", u"MainWindow", None))
        self.titulo.setText(QCoreApplication.translate("pagina_login", u"Inicio de Sesi\u00f3n", None))
        self.logo_app.setText("")
        self.label.setText(QCoreApplication.translate("pagina_login", u"Correo electr\u00f3nico:", None))
        self.label_2.setText(QCoreApplication.translate("pagina_login", u"Contrase\u00f1a:", None))
        self.boton_login.setText(QCoreApplication.translate("pagina_login", u"Iniciar Sesi\u00f3n", None))
        self.label_3.setText(QCoreApplication.translate("pagina_login", u"\u00bfA\u00fan no cuentas con una cuenta?", None))
        self.boton_registro.setText(QCoreApplication.translate("pagina_login", u"Registrate Ahora", None))
        self.cargando.setText("")
        self.error.setText("")
    # retranslateUi

