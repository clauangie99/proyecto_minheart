# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(395, 270)
        self.botonesDialog = QDialogButtonBox(Dialog)
        self.botonesDialog.setObjectName(u"botonesDialog")
        self.botonesDialog.setGeometry(QRect(210, 210, 161, 32))
        self.botonesDialog.setOrientation(Qt.Orientation.Horizontal)
        self.botonesDialog.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 101, 16))
        self.titulo = QLineEdit(Dialog)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setGeometry(QRect(20, 60, 231, 21))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 110, 101, 16))
        self.descripcion = QTextEdit(Dialog)
        self.descripcion.setObjectName(u"descripcion")
        self.descripcion.setGeometry(QRect(20, 140, 171, 101))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(270, 30, 101, 16))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(210, 110, 101, 16))
        self.archivos = QPushButton(Dialog)
        self.archivos.setObjectName(u"archivos")
        self.archivos.setGeometry(QRect(210, 130, 141, 32))
        self.imagen_label = QLabel(Dialog)
        self.imagen_label.setObjectName(u"imagen_label")
        self.imagen_label.setGeometry(QRect(210, 170, 161, 21))
        self.precio = QLineEdit(Dialog)
        self.precio.setObjectName(u"precio")
        self.precio.setGeometry(QRect(270, 60, 113, 21))

        self.retranslateUi(Dialog)
        self.botonesDialog.accepted.connect(Dialog.accept)
        self.botonesDialog.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Titulo:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Descripci\u00f3n:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Precio:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Im\u00e1gen o video:", None))
        self.archivos.setText(QCoreApplication.translate("Dialog", u"Seleccionar archivo", None))
        self.imagen_label.setText("")
    # retranslateUi

