# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_loginPpkhQP.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_loginVentana(object):
    def setupUi(self, loginVentana):
        if not loginVentana.objectName():
            loginVentana.setObjectName(u"loginVentana")
        loginVentana.resize(370, 270)
        loginVentana.setMinimumSize(QSize(370, 270))
        loginVentana.setMaximumSize(QSize(370, 270))
        icon = QIcon()
        icon.addFile(u"recursos/logo.png", QSize(), QIcon.Mode.Active, QIcon.State.On)
        loginVentana.setWindowIcon(icon)
        self.verticalLayoutWidget = QWidget(loginVentana)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(9, 8, 351, 251))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.titulo = QLabel(self.verticalLayoutWidget)
        self.titulo.setObjectName(u"titulo")
        self.titulo.setMaximumSize(QSize(370, 50))
        font = QFont()
        font.setFamilies([u"Star Jedi"])
        font.setPointSize(20)
        self.titulo.setFont(font)
        self.titulo.setFrameShape(QFrame.Shape.NoFrame)
        self.titulo.setLineWidth(1)
        self.titulo.setScaledContents(False)
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.titulo)

        self.usuarioLayout = QHBoxLayout()
        self.usuarioLayout.setObjectName(u"usuarioLayout")
        self.usuarioLayout.setContentsMargins(25, -1, 25, -1)
        self.textoUsuario = QLabel(self.verticalLayoutWidget)
        self.textoUsuario.setObjectName(u"textoUsuario")
        self.textoUsuario.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.usuarioLayout.addWidget(self.textoUsuario)

        self.inputUsuario = QLineEdit(self.verticalLayoutWidget)
        self.inputUsuario.setObjectName(u"inputUsuario")

        self.usuarioLayout.addWidget(self.inputUsuario)

        self.usuarioLayout.setStretch(0, 1)
        self.usuarioLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.usuarioLayout)

        self.passwordLayout = QHBoxLayout()
        self.passwordLayout.setObjectName(u"passwordLayout")
        self.passwordLayout.setContentsMargins(25, -1, 25, -1)
        self.textoPassword = QLabel(self.verticalLayoutWidget)
        self.textoPassword.setObjectName(u"textoPassword")
        self.textoPassword.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.passwordLayout.addWidget(self.textoPassword)

        self.inputPassword = QLineEdit(self.verticalLayoutWidget)
        self.inputPassword.setObjectName(u"inputPassword")

        self.passwordLayout.addWidget(self.inputPassword)

        self.passwordLayout.setStretch(0, 1)
        self.passwordLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.passwordLayout)

        self.direccionLayout = QHBoxLayout()
        self.direccionLayout.setObjectName(u"direccionLayout")
        self.direccionLayout.setContentsMargins(25, -1, 25, -1)
        self.textoDireccion = QLabel(self.verticalLayoutWidget)
        self.textoDireccion.setObjectName(u"textoDireccion")
        self.textoDireccion.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.direccionLayout.addWidget(self.textoDireccion)

        self.inputDireccion = QLineEdit(self.verticalLayoutWidget)
        self.inputDireccion.setObjectName(u"inputDireccion")

        self.direccionLayout.addWidget(self.inputDireccion)

        self.direccionLayout.setStretch(0, 1)
        self.direccionLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.direccionLayout)

        self.bbddLayout = QHBoxLayout()
        self.bbddLayout.setObjectName(u"bbddLayout")
        self.bbddLayout.setContentsMargins(25, -1, 25, -1)
        self.textoBBDD = QLabel(self.verticalLayoutWidget)
        self.textoBBDD.setObjectName(u"textoBBDD")
        self.textoBBDD.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bbddLayout.addWidget(self.textoBBDD)

        self.inputBBDD = QLineEdit(self.verticalLayoutWidget)
        self.inputBBDD.setObjectName(u"inputBBDD")

        self.bbddLayout.addWidget(self.inputBBDD)

        self.bbddLayout.setStretch(0, 1)
        self.bbddLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.bbddLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.botonConectar = QPushButton(self.verticalLayoutWidget)
        self.botonConectar.setObjectName(u"botonConectar")

        self.horizontalLayout.addWidget(self.botonConectar)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 3)
        self.horizontalLayout.setStretch(2, 3)

        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(loginVentana)

        QMetaObject.connectSlotsByName(loginVentana)
    # setupUi

    def retranslateUi(self, loginVentana):
        loginVentana.setWindowTitle(QCoreApplication.translate("loginVentana", u"Login", None))
        self.titulo.setText(QCoreApplication.translate("loginVentana", u"Login BBDD", None))
        self.textoUsuario.setText(QCoreApplication.translate("loginVentana", u"Usuario", None))
        self.inputUsuario.setText("")
        self.inputUsuario.setPlaceholderText(QCoreApplication.translate("loginVentana", u"Introduce el usuario de la BBDD", None))
        self.textoPassword.setText(QCoreApplication.translate("loginVentana", u"Contrase\u00f1a", None))
        self.inputPassword.setPlaceholderText(QCoreApplication.translate("loginVentana", u"Introduce la contrase\u00f1a", None))
        self.textoDireccion.setText(QCoreApplication.translate("loginVentana", u"Direcci\u00f3n BBDD", None))
        self.inputDireccion.setPlaceholderText(QCoreApplication.translate("loginVentana", u"Ej.: localhost:8080", None))
        self.textoBBDD.setText(QCoreApplication.translate("loginVentana", u"BBDD", None))
        self.inputBBDD.setPlaceholderText(QCoreApplication.translate("loginVentana", u"Introduce el nombre de la BBDD", None))
        self.botonConectar.setText(QCoreApplication.translate("loginVentana", u"Conectar", None))
    # retranslateUi

