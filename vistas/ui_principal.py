# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_principalkNcFlA.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1280, 720)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1280, 720))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u"recursos/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
#if QT_CONFIG(statustip)
        MainWindow.setStatusTip(u"")
#endif // QT_CONFIG(statustip)
        MainWindow.setStyleSheet(u"")
        MainWindow.setDockOptions(QMainWindow.DockOption.AllowTabbedDocks|QMainWindow.DockOption.AnimatedDocks)
        self.actionSalir = QAction(MainWindow)
        self.actionSalir.setObjectName(u"actionSalir")
        self.actionSalir.setShortcutContext(Qt.ShortcutContext.WindowShortcut)
        self.actionExportar_tabla = QAction(MainWindow)
        self.actionExportar_tabla.setObjectName(u"actionExportar_tabla")
        self.actionMateriasVista = QAction(MainWindow)
        self.actionMateriasVista.setObjectName(u"actionMateriasVista")
        self.actionCursos = QAction(MainWindow)
        self.actionCursos.setObjectName(u"actionCursos")
        self.actionDepartamentos = QAction(MainWindow)
        self.actionDepartamentos.setObjectName(u"actionDepartamentos")
        self.actionEspecialidades = QAction(MainWindow)
        self.actionEspecialidades.setObjectName(u"actionEspecialidades")
        self.actionOptativas = QAction(MainWindow)
        self.actionOptativas.setObjectName(u"actionOptativas")
        self.actionTiposAsignatura = QAction(MainWindow)
        self.actionTiposAsignatura.setObjectName(u"actionTiposAsignatura")
        self.actionTurnos = QAction(MainWindow)
        self.actionTurnos.setObjectName(u"actionTurnos")
        self.actionHorasDepartamentos = QAction(MainWindow)
        self.actionHorasDepartamentos.setObjectName(u"actionHorasDepartamentos")
        self.actionMaterias = QAction(MainWindow)
        self.actionMaterias.setObjectName(u"actionMaterias")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet(u"background-color: #5080ff;")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 1281, 701))
        self.divPrincipal = QHBoxLayout(self.horizontalLayoutWidget)
        self.divPrincipal.setObjectName(u"divPrincipal")
        self.divPrincipal.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.divPrincipal.setContentsMargins(10, 10, 10, 10)
        self.menuLateral = QVBoxLayout()
        self.menuLateral.setObjectName(u"menuLateral")
        self.logo = QLabel(self.horizontalLayoutWidget)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u"recursos/logo.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.logo.setWordWrap(False)

        self.menuLateral.addWidget(self.logo)

        self.groupBoxAcciones = QGroupBox(self.horizontalLayoutWidget)
        self.groupBoxAcciones.setObjectName(u"groupBoxAcciones")
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setBold(True)
        self.groupBoxAcciones.setFont(font)
        self.groupBoxAcciones.setStyleSheet(u"font-size: 15px;\n"
"background-color: #7aa8eb;\n"
"border-radius: 20px;")
        self.groupBoxAcciones.setFlat(False)
        self.groupBoxAcciones.setCheckable(False)
        self.layoutWidget = QWidget(self.groupBoxAcciones)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(40, 20, 171, 291))
        self.layourAcciones = QVBoxLayout(self.layoutWidget)
        self.layourAcciones.setObjectName(u"layourAcciones")
        self.layourAcciones.setContentsMargins(0, 0, 0, 0)
        self.botonAniadirCampo = QPushButton(self.layoutWidget)
        self.botonAniadirCampo.setObjectName(u"botonAniadirCampo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botonAniadirCampo.sizePolicy().hasHeightForWidth())
        self.botonAniadirCampo.setSizePolicy(sizePolicy1)
        self.botonAniadirCampo.setFont(font)
        self.botonAniadirCampo.setStyleSheet(u"#botonAniadirCampo {\n"
"	background-color: #8c6aff;\n"
"	border-radius: 20px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"#botonAniadirCampo:hover {\n"
"	background-color: #7aa8eb;\n"
"	border: 2px solid #8c6aff;\n"
"}")

        self.layourAcciones.addWidget(self.botonAniadirCampo)

        self.botonELiminarCampo = QPushButton(self.layoutWidget)
        self.botonELiminarCampo.setObjectName(u"botonELiminarCampo")
        self.botonELiminarCampo.setFont(font)
        self.botonELiminarCampo.setStyleSheet(u"#botonELiminarCampo {\n"
"	background-color: #8c6aff;\n"
"	border-radius: 20px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"#botonELiminarCampo:hover {\n"
"	background-color: #7aa8eb;\n"
"	border: 2px solid #8c6aff;\n"
"}")

        self.layourAcciones.addWidget(self.botonELiminarCampo)

        self.botonGuardar = QPushButton(self.layoutWidget)
        self.botonGuardar.setObjectName(u"botonGuardar")
        self.botonGuardar.setFont(font)
        self.botonGuardar.setStyleSheet(u"#botonGuardar {\n"
"	background-color: #8c6aff;\n"
"	border-radius: 20px;\n"
"	height: 40px;\n"
"}\n"
"\n"
"#botonGuardar:hover {\n"
"	background-color: #7aa8eb;\n"
"	border: 2px solid #8c6aff;\n"
"}")

        self.layourAcciones.addWidget(self.botonGuardar)


        self.menuLateral.addWidget(self.groupBoxAcciones)

        self.menuLateral.setStretch(0, 2)
        self.menuLateral.setStretch(1, 4)

        self.divPrincipal.addLayout(self.menuLateral)

        self.visorTabla = QVBoxLayout()
        self.visorTabla.setObjectName(u"visorTabla")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.nombreTabla = QLabel(self.horizontalLayoutWidget)
        self.nombreTabla.setObjectName(u"nombreTabla")
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(19)
        font1.setBold(True)
        self.nombreTabla.setFont(font1)
        self.nombreTabla.setTextFormat(Qt.TextFormat.RichText)
        self.nombreTabla.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.nombreTabla)

        self.entryBuscar = QLineEdit(self.horizontalLayoutWidget)
        self.entryBuscar.setObjectName(u"entryBuscar")
        font2 = QFont()
        font2.setFamilies([u"Consolas"])
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.entryBuscar.setFont(font2)
        self.entryBuscar.setStyleSheet(u"#entryBuscar {\n"
"	background-color: white;\n"
"	border-radius: 20px;\n"
"	font-size: 15px;\n"
"	height: 40px;\n"
"}")

        self.horizontalLayout_2.addWidget(self.entryBuscar)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.horizontalLayout_2.setStretch(0, 6)
        self.horizontalLayout_2.setStretch(1, 4)
        self.horizontalLayout_2.setStretch(2, 1)

        self.visorTabla.addLayout(self.horizontalLayout_2)

        self.vistaTabla = QTableWidget(self.horizontalLayoutWidget)
        self.vistaTabla.setObjectName(u"vistaTabla")
        self.vistaTabla.setStyleSheet(u"QTableView {\n"
"	height: 40px;\n"
"	background-color: rgb(255, 255, 255);\n"
"    border-radius: 20px; /* Ajusta el valor para redondear m\u00e1s o menos los bordes */\n"
"    border: 1px solid #ccc; /* Un borde sutil para definir la tabla */\n"
"	padding: 5px;\n"
"}\n"
"\n"
"QTableView::viewport {\n"
"	height: 40px;\n"
"	border-radius: 20px;\n"
"    background-color: #6B8E23;\n"
"}\n"
"\n"
"QTableView::corner {\n"
"    background-color: #6B8E23; /* Color de la esquina superior izquierda */\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QTableView::horizontalHeader {\n"
"    background-color: #6B8E23; /* Color de la esquina superior izquierda */\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QTableView::verticalHeader {\n"
"    background-color: #6B8E23; /* Color de la esquina superior izquierda */\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    padding: 5px; /* Espacio dentro de cada celda */\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QTableView::row:nth-child(odd) {"
                        "\n"
"    background-color: #8FBC8F; /* Verde medio (MediumSeaGreen) para filas impares */\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QTableView::row:nth-child(even) {\n"
"    background-color: #98FB98; /* Verde claro (PaleGreen) para filas pares */\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"    background-color: #6B8E23; /* Verde oscuro (OliveDrab) para la cabecera */\n"
"    color: white;\n"
"    padding: 5px;\n"
"    border: none;\n"
"	border-radius: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:first {\n"
"	border-radius: 20px;\n"
"    border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QHeaderView::section:horizontal:last {\n"
"    border-top-right-radius: 20px;\n"
"}")

        self.visorTabla.addWidget(self.vistaTabla)

        self.visorTabla.setStretch(0, 1)
        self.visorTabla.setStretch(1, 8)

        self.divPrincipal.addLayout(self.visorTabla)

        self.divPrincipal.setStretch(0, 1)
        self.divPrincipal.setStretch(1, 4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1280, 22))
        self.menuOpciones = QMenu(self.menubar)
        self.menuOpciones.setObjectName(u"menuOpciones")
        self.menuTablas = QMenu(self.menubar)
        self.menuTablas.setObjectName(u"menuTablas")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuOpciones.menuAction())
        self.menubar.addAction(self.menuTablas.menuAction())
        self.menuOpciones.addAction(self.actionExportar_tabla)
        self.menuOpciones.addSeparator()
        self.menuOpciones.addAction(self.actionSalir)
        self.menuTablas.addAction(self.actionCursos)
        self.menuTablas.addAction(self.actionDepartamentos)
        self.menuTablas.addAction(self.actionEspecialidades)
        self.menuTablas.addAction(self.actionHorasDepartamentos)
        self.menuTablas.addAction(self.actionMaterias)
        self.menuTablas.addAction(self.actionMateriasVista)
        self.menuTablas.addAction(self.actionOptativas)
        self.menuTablas.addAction(self.actionTiposAsignatura)
        self.menuTablas.addAction(self.actionTurnos)

        self.retranslateUi(MainWindow)
        self.actionSalir.triggered["bool"].connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"App", None))
        self.actionSalir.setText(QCoreApplication.translate("MainWindow", u"Salir", None))
        self.actionExportar_tabla.setText(QCoreApplication.translate("MainWindow", u"Exportar tabla (.csv)", None))
        self.actionMateriasVista.setText(QCoreApplication.translate("MainWindow", u"Materias (vista)", None))
        self.actionCursos.setText(QCoreApplication.translate("MainWindow", u"Cursos", None))
        self.actionDepartamentos.setText(QCoreApplication.translate("MainWindow", u"Departamentos", None))
        self.actionEspecialidades.setText(QCoreApplication.translate("MainWindow", u"Especialidades", None))
        self.actionOptativas.setText(QCoreApplication.translate("MainWindow", u"Optativas", None))
        self.actionTiposAsignatura.setText(QCoreApplication.translate("MainWindow", u"Tipos de asignatura", None))
        self.actionTurnos.setText(QCoreApplication.translate("MainWindow", u"Turnos", None))
        self.actionHorasDepartamentos.setText(QCoreApplication.translate("MainWindow", u"Horas departementos (vista)", None))
        self.actionMaterias.setText(QCoreApplication.translate("MainWindow", u"Materias", None))
        self.logo.setText("")
        self.groupBoxAcciones.setTitle(QCoreApplication.translate("MainWindow", u"Acciones", None))
        self.botonAniadirCampo.setText(QCoreApplication.translate("MainWindow", u"A\u00f1adir fila", None))
        self.botonELiminarCampo.setText(QCoreApplication.translate("MainWindow", u"Eliminar fila", None))
        self.botonGuardar.setText(QCoreApplication.translate("MainWindow", u"Guardar tabla (BBDD)", None))
        self.nombreTabla.setText(QCoreApplication.translate("MainWindow", u"Nombre de la tabla", None))
#if QT_CONFIG(statustip)
        self.entryBuscar.setStatusTip("")
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.entryBuscar.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.entryBuscar.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.entryBuscar.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.entryBuscar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Filtrar por nombre", None))
        self.menuOpciones.setTitle(QCoreApplication.translate("MainWindow", u"Opciones", None))
        self.menuTablas.setTitle(QCoreApplication.translate("MainWindow", u"Tablas", None))
    # retranslateUi

