# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QLabel, QMainWindow,
    QMenuBar, QPushButton, QScrollArea, QSizePolicy,
    QStatusBar, QTextEdit, QWidget)

class Ui_pagina_inicio(object):
    def setupUi(self, pagina_inicio):
        if not pagina_inicio.objectName():
            pagina_inicio.setObjectName(u"pagina_inicio")
        pagina_inicio.resize(800, 600)
        pagina_inicio.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        pagina_inicio.setAutoFillBackground(False)
        self.centralwidget = QWidget(pagina_inicio)
        self.centralwidget.setObjectName(u"centralwidget")
        self.logo_app = QLabel(self.centralwidget)
        self.logo_app.setObjectName(u"logo_app")
        self.logo_app.setGeometry(QRect(20, 20, 231, 41))
        self.label_nombre = QLabel(self.centralwidget)
        self.label_nombre.setObjectName(u"label_nombre")
        self.label_nombre.setGeometry(QRect(30, 100, 141, 31))
        self.label_nombre.setStyleSheet(u"font: 25pt \"Lucida Grande\";\n"
"font: 25pt \"Lucida Grande\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 290, 71, 16))
        self.label_2.setStyleSheet(u"font: 15pt \"Lucida Grande\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.nombre = QLabel(self.centralwidget)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setGeometry(QRect(30, 310, 141, 16))
        self.nuevo_proyecto = QPushButton(self.centralwidget)
        self.nuevo_proyecto.setObjectName(u"nuevo_proyecto")
        self.nuevo_proyecto.setGeometry(QRect(200, 100, 111, 32))
        self.nuevo_proyecto.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(730, 30, 51, 16))
        self.label_6.setStyleSheet(u"font: 18pt \"Lucida Grande\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.contenedor = QScrollArea(self.centralwidget)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setEnabled(True)
        self.contenedor.setGeometry(QRect(200, 140, 591, 391))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(10)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self.contenedor.sizePolicy().hasHeightForWidth())
        self.contenedor.setSizePolicy(sizePolicy)
        self.contenedor.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.contenedor.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.contenedor.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.contenedor.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 573, 373))
        self.contenedor.setWidget(self.scrollAreaWidgetContents)
        self.cerrar_sesion = QPushButton(self.centralwidget)
        self.cerrar_sesion.setObjectName(u"cerrar_sesion")
        self.cerrar_sesion.setGeometry(QRect(30, 510, 131, 21))
        self.cerrar_sesion.setStyleSheet(u"border-radius: 10px;  /* Bordes redondeados */\n"
"border: 1px solid;  /* Borde del bot\u00f3n */\n"
"font-size: 13px;  /* Tama\u00f1o de la fuente */\n"
"color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(-10, 80, 811, 511))
        self.label_8.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 340, 131, 16))
        self.label_3.setStyleSheet(u"font: 15pt \"Lucida Grande\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.descripcion = QTextEdit(self.centralwidget)
        self.descripcion.setObjectName(u"descripcion")
        self.descripcion.setGeometry(QRect(30, 360, 141, 131))
        self.descripcion.setOverwriteMode(False)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(320, 106, 241, 16))
        font = QFont()
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(153, 153, 153);")
        self.editar_foto = QPushButton(self.centralwidget)
        self.editar_foto.setObjectName(u"editar_foto")
        self.editar_foto.setGeometry(QRect(29, 250, 141, 32))
        self.editar_foto.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.foto_perfil = QLabel(self.centralwidget)
        self.foto_perfil.setObjectName(u"foto_perfil")
        self.foto_perfil.setGeometry(QRect(30, 140, 131, 101))
        self.foto_perfil.setFont(font)
        self.foto_perfil.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.foto_perfil.setAutoFillBackground(False)
        pagina_inicio.setCentralWidget(self.centralwidget)
        self.label_8.raise_()
        self.logo_app.raise_()
        self.label_nombre.raise_()
        self.nombre.raise_()
        self.nuevo_proyecto.raise_()
        self.contenedor.raise_()
        self.cerrar_sesion.raise_()
        self.label_6.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.descripcion.raise_()
        self.label.raise_()
        self.editar_foto.raise_()
        self.foto_perfil.raise_()
        self.menubar = QMenuBar(pagina_inicio)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        pagina_inicio.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(pagina_inicio)
        self.statusbar.setObjectName(u"statusbar")
        pagina_inicio.setStatusBar(self.statusbar)

        self.retranslateUi(pagina_inicio)

        QMetaObject.connectSlotsByName(pagina_inicio)
    # setupUi

    def retranslateUi(self, pagina_inicio):
        pagina_inicio.setWindowTitle(QCoreApplication.translate("pagina_inicio", u"pagina_inicio", None))
        self.logo_app.setText("")
        self.label_nombre.setText(QCoreApplication.translate("pagina_inicio", u"Bienvenido", None))
        self.label_2.setText(QCoreApplication.translate("pagina_inicio", u"Nombre:", None))
        self.nombre.setText(QCoreApplication.translate("pagina_inicio", u"TextLabel", None))
        self.nuevo_proyecto.setText(QCoreApplication.translate("pagina_inicio", u"Nuevo Proyecto", None))
        self.label_6.setText(QCoreApplication.translate("pagina_inicio", u"Perfil", None))
        self.cerrar_sesion.setText(QCoreApplication.translate("pagina_inicio", u"Cerrar Sesi\u00f3n", None))
        self.label_8.setText("")
        self.label_3.setText(QCoreApplication.translate("pagina_inicio", u"Descripci\u00f3n:", None))
        self.descripcion.setDocumentTitle(QCoreApplication.translate("pagina_inicio", u"Cuentanos de ti", None))
        self.descripcion.setMarkdown("")
        self.descripcion.setPlaceholderText(QCoreApplication.translate("pagina_inicio", u"Escribe aqu\u00ed...", None))
        self.label.setText(QCoreApplication.translate("pagina_inicio", u"Agrega un nuevo proyecto", None))
        self.editar_foto.setText(QCoreApplication.translate("pagina_inicio", u"Editar foto", None))
        self.foto_perfil.setText(QCoreApplication.translate("pagina_inicio", u"Sin foto de perfil", None))
    # retranslateUi

