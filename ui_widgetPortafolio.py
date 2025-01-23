# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'widgetPortafolio.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(630, 227)
        self.widget_titulo = QLabel(Form)
        self.widget_titulo.setObjectName(u"widget_titulo")
        self.widget_titulo.setGeometry(QRect(300, 30, 321, 31))
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.widget_titulo.setFont(font)
        self.widget_titulo.setStyleSheet(u"font: 20pt \"Academy Engraved LET\";")
        self.widget_titulo.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.widget_descripcion = QLabel(Form)
        self.widget_descripcion.setObjectName(u"widget_descripcion")
        self.widget_descripcion.setGeometry(QRect(240, 140, 361, 71))
        font1 = QFont()
        font1.setItalic(True)
        self.widget_descripcion.setFont(font1)
        self.widget_descripcion.setAutoFillBackground(False)
        self.widget_descripcion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.widget_precio = QLabel(Form)
        self.widget_precio.setObjectName(u"widget_precio")
        self.widget_precio.setGeometry(QRect(300, 70, 91, 16))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(370, 70, 61, 16))
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.widget_imagen = QLabel(Form)
        self.widget_imagen.setObjectName(u"widget_imagen")
        self.widget_imagen.setGeometry(QRect(20, 10, 181, 201))
        self.comboBox = QComboBox(Form)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(442, 65, 131, 32))
        self.comboBox.setEditable(True)
        self.widget_descripcion_2 = QLabel(Form)
        self.widget_descripcion_2.setObjectName(u"widget_descripcion_2")
        self.widget_descripcion_2.setGeometry(QRect(240, 110, 361, 16))
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setItalic(False)
        self.widget_descripcion_2.setFont(font3)
        self.widget_descripcion_2.setAutoFillBackground(False)
        self.widget_descripcion_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(240, 70, 51, 16))
        self.label_5.setFont(font2)
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(240, 35, 51, 16))
        self.label_6.setFont(font2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.widget_titulo.setText(QCoreApplication.translate("Form", u"Titulo", None))
        self.widget_descripcion.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n", None))
        self.widget_precio.setText(QCoreApplication.translate("Form", u"Precio", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Estado:", None))
        self.widget_imagen.setText(QCoreApplication.translate("Form", u"Im\u00e1gen", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"En Venta", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"Vendido", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Form", u"En Exhibici\u00f3n", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("Form", u"Selecci\u00f3n", None))
        self.widget_descripcion_2.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Precio:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"T\u00edtulo:", None))
    # retranslateUi

