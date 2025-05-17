# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_errorlBcjBT.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(320, 110)
        Form.setMinimumSize(QSize(320, 110))
        Form.setMaximumSize(QSize(320, 110))
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DialogWarning))
        Form.setWindowIcon(icon)
        self.horizontalLayoutWidget = QWidget(Form)
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
        self.icono.setPixmap(QPixmap(u"../../recursos/dialog_warning.png"))
        self.icono.setScaledContents(False)
        self.icono.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.icono)

        self.textoError = QLabel(self.horizontalLayoutWidget)
        self.textoError.setObjectName(u"textoError")

        self.horizontalLayout.addWidget(self.textoError)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Error", None))
        self.icono.setText("")
        self.textoError.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

