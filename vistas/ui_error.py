# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_errorRQMxSq.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_errorVentana(object):
    def setupUi(self, errorVentana):
        if not errorVentana.objectName():
            errorVentana.setObjectName(u"errorVentana")
        errorVentana.resize(320, 110)
        errorVentana.setMinimumSize(QSize(320, 110))
        errorVentana.setMaximumSize(QSize(320, 110))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning))
        errorVentana.setWindowIcon(icon)
        errorVentana.setStyleSheet(u"#errorVentana {\n"
"	background-color: #5080ff;\n"
"}")
        self.horizontalLayoutWidget = QWidget(errorVentana)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(-1, -1, 321, 111))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icono = QLabel(self.horizontalLayoutWidget)
        self.icono.setObjectName(u"icono")
        self.icono.setMinimumSize(QSize(0, 0))
        self.icono.setBaseSize(QSize(0, 0))
        self.icono.setStyleSheet(u"#icono {\n"
"	height: 50px;\n"
"}")
        self.icono.setPixmap(QPixmap(u"recursos/dialog_warning.png"))
        self.icono.setScaledContents(False)
        self.icono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.icono)

        self.textoError = QLabel(self.horizontalLayoutWidget)
        self.textoError.setObjectName(u"textoError")
        self.textoError.setAutoFillBackground(False)
        self.textoError.setWordWrap(True)

        self.horizontalLayout.addWidget(self.textoError)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(errorVentana)

        QMetaObject.connectSlotsByName(errorVentana)
    # setupUi

    def retranslateUi(self, errorVentana):
        errorVentana.setWindowTitle(QCoreApplication.translate("errorVentana", u"Error", None))
        self.icono.setText("")
        self.textoError.setText(QCoreApplication.translate("errorVentana", u"Error desconocido. Intentelo de nuevo m\u00e1s tarde.", None))
    # retranslateUi

