# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(841, 448)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setStyleSheet(u"\n"
"QTabWidget::pane {\n"
"		border-width: 0px;\n"
"border-radius:0px;\n"
"	     border-style: solid;\n"
"\n"
"}\n"
"QTabWidget :disabled{\n"
"	color:black;\n"
"}\n"
"\n"
"\n"
"QTabBar::tab {\n"
"border-style:outset;\n"
"	border-color: rgb(47, 47, 47);\n"
"width:60px;\n"
"height:25px;\n"
"	font: 75 13pt \"Tahoma\";\n"
"margin:1px;\n"
"\n"
"	border-width: 2px;\n"
"  	border-top-right-radius:10px;\n"
"   border-top-left-radius:10px;\n"
"border-bottom-width:0px;\n"
"\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected{\n"
"border-style:inset;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(139, 139, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:!selected {\n"
"    	margin-top: 1px;\n"
"		margin-right: 1px;\n"
"		background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(78,78, 78, 255), stop:1 rgba(71, 71, 71, 255));\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"	font: 75 11pt \"Tahoma\";\n"
"	color: rgb(0, 0, 0);\n"
"	"
                        "background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(139, 139, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
"	border-style: outset;\n"
"\n"
"	\n"
"	border-color: rgb(39, 39, 39);\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(139, 139, 139, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	border-width: 1px;\n"
"	border-radius: 12px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.615, y2:1, stop:0 rgba(221, 221, 221, 255), stop:1 rgba(111, 111, 111, 255));\n"
"}\n"
"QPushButton:pressed{\n"
"border-style:inset;\n"
"	background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(109, 109, 109, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"QPushButton:disabled{\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-right-color: qlineargradie"
                        "nt(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-bottom-color: rgb(58, 58, 58);\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"\n"
"QLineEdit {\n"
"	color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"	border-width: 1px; \n"
"border-radius: 8px;\n"
"	border-style: inset;\n"
"	background: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(187, 187, 187);\n"
"	selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLineEdit::disabled {\n"
"	color: rgb(129, 129, 129);\n"
"}\n"
"QLabel {\n"
"	border:none;\n"
"	background-color: transparent;\n"
"\n"
"}\n"
"QLabel::disabled\n"
"{\n"
"		color: rgb(0, 0, 0);\n"
"}\n"
"QMenuBar {\n"
"	font: 9pt \"Tahoma\";\n"
"}\n"
""
                        "QMenuBar::item {\n"
"	spacing: 3px;\n"
"	padding: 1px 4px;\n"
"	background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"	background:rgb(115, 115, 115);\n"
"	font: 9pt \"Tahoma\";\n"
"}\n"
"QMenu::item:selected {\n"
"	color:rgb(255,255,255);\n"
"	border-width:2px;\n"
"	border-style:solid;\n"
"	padding-left:18px;\n"
"	padding-right:8px;\n"
"	padding-top:2px;\n"
"	padding-bottom:3px;\n"
"	background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-bottom-color: rgb(58, 58, 58);\n"
""
                        "	border-bottom-width: 1px;\n"
"}\n"
"QMenu::item {\n"
"	background-color:rgb(78,78,78);\n"
"	padding-left:20px;\n"
"	padding-top:4px;\n"
"	padding-bottom:4px;\n"
"	padding-right:10px;\n"
"	font: 9pt \"Tahoma\";\n"
"}\n"
"\n"
"QCheckBox {\n"
"	padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	padding-left: 1px;\n"
"	padding-right: 1px;\n"
"	padding-bottom: 1px;\n"
"	padding-top: 1px;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QComboBox\n"
"{\n"
"	background-color: rgb(99, 99, 99);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"	border-radius:4px;\n"
"	border-style:solid;\n"
"	border-width:1px;\n"
"	border-color: rgb(87, 97, 106);\n"
"	background-color: rgb(255, 255, 255);\n"
"\n"
"}\n"
"\n"
"QSlider{\n"
"	border-style: o"
                        "utset;\n"
"	border-left-color: rgb(130, 130, 130);\n"
"	border-top-color: rgb(136, 136, 136);\n"
"	border-right-color: rgb(107, 107, 107);\n"
"	border-bottom-color: rgb(98, 98, 98);\n"
"border-width:1px;\n"
"	padding: 6px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0.864, stop:0 rgba(150, 150, 150, 255), stop:1 rgba(71, 71, 71, 255));\n"
"	border-radius: 14px;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"	border-style: outset;\n"
"	border-color: rgb(0, 0, 0);\n"
"	border-width: 0px;\n"
"    margin:2px 2px;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"     	background-color: rgb(255, 141, 0);\n"
"    margin: 6px 2px;\n"
"}\n"
"QSlider::sub-page:horizontal:disabled {\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"QSlider::add-page:horizontal {\n"
"	background-color: rgb(98, 98, 98);\n"
"	border-width: 0px;\n"
"\n"
"    margin: 8px 2px;\n"
"}\n"
"QSlider::handle {\n"
"	border-style: outset;\n"
"	border-left-color: rgb(170, 170, 170);\n"
"	border-top-color: rgb(170, 170, 170);\n"
"	borde"
                        "r-right-color: rgb(50, 50, 50);\n"
"	border-bottom-color: rgb(50, 50, 50);\n"
"    \n"
"	background-color: rgb(255, 141, 0);\n"
"	border-width: 1px;\n"
"	border-radius: 11px;\n"
"   width: 35px;\n"
"    margin: -6px -6px;\n"
"\n"
"    }\n"
"\n"
"QSlider::disabled {\n"
"	border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"	border-bottom-color: rgb(58, 58, 58);\n"
"	border-bottom-width: 1px;\n"
"	color: rgb(0, 0, 0);\n"
"	background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"\n"
"QSlider::handle:disabled{\n"
"	background-color: rgb(59, 48,"
                        " 48);\n"
"}\n"
"\n"
"QFrame, QSpinBox\n"
"{\n"
"border-style:outset;\n"
"	border-color: rgb(40, 40, 40);\n"
"	border-width: 3px;\n"
"\n"
"}\n"
"\n"
"\n"
"\n"
"QSpinBox {\n"
"    padding-right: -4px; /* make room for the arrows */\n"
"border-radius:11px;\n"
"}\n"
"\n"
"QSpinBox::up-button {\n"
"\n"
"    width: 15px; /* 16 + 2*1px border-width = 15px padding + 3px parent border */\n"
"	border-image: url(:/Images/Images/up.png);\n"
"    border-width: 1px;\n"
"    border-bottom-width: 0;\n"
"    padding: 1px; \n"
"}\n"
"\n"
"\n"
"QSpinBox::down-button {\n"
"\n"
"\n"
"    width: 15px;\n"
"	\n"
"	border-image: url(:/Images/Images/Down.png);\n"
"    border-width: 1px;\n"
"    border-top-width: 0;\n"
"    padding: 1px; \n"
"}\n"
"\n"
"QSpinBox::up-button:hover, ::down-button:hover{\n"
"	border-width: 0;\n"
"}\n"
"QSpinBox::up-button:pressed, ::down-button:pressed{\n"
"	border-width: 2;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 11px;\n"
"	font: 700 8pt \"Tahoma\";\n"
"}\n"
"\n"
"\n"
"QComboBox::drop-down {\n"
""
                        "width : 11px;\n"
"height:11px;\n"
"	border-image: url(:/Images/Images/Down.png);\n"
"border-width:5px;\n"
"margin:2px -2px;\n"
"}\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"\n"
"#frame QFrame\n"
"{\n"
"border-radius:19px;\n"
"}\n"
"\n"
"#toolBox QLabel, #Developer QLabel\n"
"{\n"
"	border-radius:17px;\n"
"	border-style:outset;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(90, 90, 90, 		255), stop:1 rgba(44, 44, 44, 255));\n"
"}\n"
"\n"
"QObject #speedwidget, #RPMwidget, #TempWidget, #FuelWidget\n"
"{\n"
"	background-color: transparent;\n"
"}\n"
"QTabWidget ::tab\n"
"{\n"
"	background-color: rgb(162, 162, 162);\n"
"\n"
"}")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(2, 2, 2, 2)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tab.setMinimumSize(QSize(0, 0))
        self.tab.setMaximumSize(QSize(16777215, 16777215))
        self.tab.setStyleSheet(u"QFrame\n"
"{\n"
"border-radius:13px;\n"
"}")
        self.gridLayout_3 = QGridLayout(self.tab)
        self.gridLayout_3.setSpacing(2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(2, 2, 2, 2)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 1, 3, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.frame_3 = QFrame(self.tab)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setMinimumSize(QSize(130, 0))
        self.frame_3.setMaximumSize(QSize(130, 292))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.btnrun = QPushButton(self.frame_3)
        self.btnrun.setObjectName(u"btnrun")
        sizePolicy1.setHeightForWidth(self.btnrun.sizePolicy().hasHeightForWidth())
        self.btnrun.setSizePolicy(sizePolicy1)
        self.btnrun.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnrun)

        self.btnstop = QPushButton(self.frame_3)
        self.btnstop.setObjectName(u"btnstop")
        sizePolicy1.setHeightForWidth(self.btnstop.sizePolicy().hasHeightForWidth())
        self.btnstop.setSizePolicy(sizePolicy1)
        self.btnstop.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnstop)

        self.btnload = QPushButton(self.frame_3)
        self.btnload.setObjectName(u"btnload")
        sizePolicy1.setHeightForWidth(self.btnload.sizePolicy().hasHeightForWidth())
        self.btnload.setSizePolicy(sizePolicy1)
        self.btnload.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnload)

        self.btnsave = QPushButton(self.frame_3)
        self.btnsave.setObjectName(u"btnsave")
        sizePolicy1.setHeightForWidth(self.btnsave.sizePolicy().hasHeightForWidth())
        self.btnsave.setSizePolicy(sizePolicy1)
        self.btnsave.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnsave)

        self.btnclose = QPushButton(self.frame_3)
        self.btnclose.setObjectName(u"btnclose")
        sizePolicy1.setHeightForWidth(self.btnclose.sizePolicy().hasHeightForWidth())
        self.btnclose.setSizePolicy(sizePolicy1)
        self.btnclose.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.btnclose)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy1.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy1)
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        sizePolicy1.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy1)
        self.pushButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.pushButton_7)


        self.gridLayout_3.addWidget(self.frame_3, 1, 2, 1, 1)

        self.frame_2 = QFrame(self.tab)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMaximumSize(QSize(819, 86))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_2)
        self.gridLayout_5.setSpacing(2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(2, 2, 2, 2)
        self.frame_52 = QFrame(self.frame_2)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setStyleSheet(u"QLabel\n"
"{\n"
"border:none;\n"
"}\n"
"QFrame\n"
"{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_57 = QHBoxLayout(self.frame_52)
        self.horizontalLayout_57.setSpacing(2)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(2, 2, 2, 2)
        self.label_57 = QLabel(self.frame_52)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"border:none;")

        self.horizontalLayout_57.addWidget(self.label_57)

        self.lineEdit_57 = QLineEdit(self.frame_52)
        self.lineEdit_57.setObjectName(u"lineEdit_57")

        self.horizontalLayout_57.addWidget(self.lineEdit_57)


        self.gridLayout_5.addWidget(self.frame_52, 2, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"border:none;\n"
"font: 700 12pt \"Tahoma\";")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_5.addWidget(self.label_2, 0, 0, 1, 1)

        self.frame_51 = QFrame(self.frame_2)
        self.frame_51.setObjectName(u"frame_51")
        sizePolicy1.setHeightForWidth(self.frame_51.sizePolicy().hasHeightForWidth())
        self.frame_51.setSizePolicy(sizePolicy1)
        self.frame_51.setStyleSheet(u"QLabel\n"
"{\n"
"border:none;\n"
"}\n"
"QFrame\n"
"{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_56 = QHBoxLayout(self.frame_51)
        self.horizontalLayout_56.setSpacing(2)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(2, 2, 2, 2)
        self.label_56 = QLabel(self.frame_51)
        self.label_56.setObjectName(u"label_56")
        sizePolicy1.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy1)
        self.label_56.setStyleSheet(u"border:none;")

        self.horizontalLayout_56.addWidget(self.label_56)

        self.WorkingDirectory = QLineEdit(self.frame_51)
        self.WorkingDirectory.setObjectName(u"WorkingDirectory")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.WorkingDirectory.sizePolicy().hasHeightForWidth())
        self.WorkingDirectory.setSizePolicy(sizePolicy2)

        self.horizontalLayout_56.addWidget(self.WorkingDirectory)

        self.btnbrowse = QPushButton(self.frame_51)
        self.btnbrowse.setObjectName(u"btnbrowse")
        self.btnbrowse.setStyleSheet(u"border-radius:10px;")

        self.horizontalLayout_56.addWidget(self.btnbrowse)

        self.horizontalLayout_56.setStretch(0, 1)
        self.horizontalLayout_56.setStretch(1, 10)
        self.horizontalLayout_56.setStretch(2, 2)

        self.gridLayout_5.addWidget(self.frame_51, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.frame_2, 2, 1, 1, 2)

        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMaximumSize(QSize(687, 292))
        self.frame.setStyleSheet(u"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 9, 9)
        self.frame_29 = QFrame(self.frame)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_32 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_32.setSpacing(4)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_29)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_32.addWidget(self.label_32)

        self.lineEdit_32 = QLineEdit(self.frame_29)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.lineEdit_32)

        self.horizontalLayout_32.setStretch(0, 3)
        self.horizontalLayout_32.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_29, 1, 1, 1, 1)

        self.frame_42 = QFrame(self.frame)
        self.frame_42.setObjectName(u"frame_42")
        self.frame_42.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_46 = QHBoxLayout(self.frame_42)
        self.horizontalLayout_46.setSpacing(4)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.frame_42)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_46.addWidget(self.label_46)

        self.lineEdit_46 = QLineEdit(self.frame_42)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.lineEdit_46)

        self.horizontalLayout_46.setStretch(0, 3)
        self.horizontalLayout_46.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_42, 5, 2, 1, 1)

        self.frame_35 = QFrame(self.frame)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_39 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_39.setSpacing(4)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.frame_35)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_39.addWidget(self.label_39)

        self.lineEdit_39 = QLineEdit(self.frame_35)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.lineEdit_39)

        self.horizontalLayout_39.setStretch(0, 3)
        self.horizontalLayout_39.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_35, 6, 1, 1, 1)

        self.frame_47 = QFrame(self.frame)
        self.frame_47.setObjectName(u"frame_47")
        self.frame_47.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_51 = QHBoxLayout(self.frame_47)
        self.horizontalLayout_51.setSpacing(4)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.frame_47)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_51.addWidget(self.label_51)

        self.lineEdit_51 = QLineEdit(self.frame_47)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.lineEdit_51)

        self.horizontalLayout_51.setStretch(0, 3)
        self.horizontalLayout_51.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_47, 1, 2, 1, 1)

        self.frame_31 = QFrame(self.frame)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_35 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_35.setSpacing(4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_31)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_35.addWidget(self.label_35)

        self.lineEdit_35 = QLineEdit(self.frame_31)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.lineEdit_35)

        self.horizontalLayout_35.setStretch(0, 3)
        self.horizontalLayout_35.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_31, 3, 0, 1, 1)

        self.frame_45 = QFrame(self.frame)
        self.frame_45.setObjectName(u"frame_45")
        self.frame_45.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_49 = QHBoxLayout(self.frame_45)
        self.horizontalLayout_49.setSpacing(4)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.frame_45)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_49.addWidget(self.label_49)

        self.lineEdit_49 = QLineEdit(self.frame_45)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.lineEdit_49)

        self.horizontalLayout_49.setStretch(0, 3)
        self.horizontalLayout_49.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_45, 7, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 10, 1, 1, 1)

        self.frame_30 = QFrame(self.frame)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_33 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_33.setSpacing(4)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.frame_30)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_33.addWidget(self.label_33)

        self.lineEdit_33 = QLineEdit(self.frame_30)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.lineEdit_33)

        self.horizontalLayout_33.setStretch(0, 3)
        self.horizontalLayout_33.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_30, 2, 1, 1, 1)

        self.frame_33 = QFrame(self.frame)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_37 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_37.setSpacing(4)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.frame_33)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_37.addWidget(self.label_37)

        self.lineEdit_37 = QLineEdit(self.frame_33)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.lineEdit_37)

        self.horizontalLayout_37.setStretch(0, 3)
        self.horizontalLayout_37.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_33, 4, 1, 1, 1)

        self.frame_26 = QFrame(self.frame)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_29 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_29.setSpacing(4)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_26)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_29.addWidget(self.label_29)

        self.lineEdit_29 = QLineEdit(self.frame_26)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.lineEdit_29)

        self.horizontalLayout_29.setStretch(0, 3)
        self.horizontalLayout_29.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_26, 1, 0, 1, 1)

        self.frame_46 = QFrame(self.frame)
        self.frame_46.setObjectName(u"frame_46")
        self.frame_46.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_50 = QHBoxLayout(self.frame_46)
        self.horizontalLayout_50.setSpacing(4)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_46)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_50)

        self.lineEdit_50 = QLineEdit(self.frame_46)
        self.lineEdit_50.setObjectName(u"lineEdit_50")
        self.lineEdit_50.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.lineEdit_50)

        self.horizontalLayout_50.setStretch(0, 3)
        self.horizontalLayout_50.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_46, 8, 1, 1, 1)

        self.frame_50 = QFrame(self.frame)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_54 = QHBoxLayout(self.frame_50)
        self.horizontalLayout_54.setSpacing(4)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.frame_50)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_54.addWidget(self.label_54)

        self.lineEdit_54 = QLineEdit(self.frame_50)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.lineEdit_54)

        self.horizontalLayout_54.setStretch(0, 3)
        self.horizontalLayout_54.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_50, 9, 0, 1, 1)

        self.frame_27 = QFrame(self.frame)
        self.frame_27.setObjectName(u"frame_27")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_27.sizePolicy().hasHeightForWidth())
        self.frame_27.setSizePolicy(sizePolicy3)
        self.frame_27.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_30 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_30.setSpacing(4)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_30 = QLabel(self.frame_27)
        self.label_30.setObjectName(u"label_30")
        sizePolicy3.setHeightForWidth(self.label_30.sizePolicy().hasHeightForWidth())
        self.label_30.setSizePolicy(sizePolicy3)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_30.addWidget(self.label_30)

        self.lineEdit_30 = QLineEdit(self.frame_27)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.lineEdit_30)

        self.horizontalLayout_30.setStretch(0, 3)
        self.horizontalLayout_30.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_27, 2, 0, 1, 1)

        self.frame_48 = QFrame(self.frame)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_52 = QHBoxLayout(self.frame_48)
        self.horizontalLayout_52.setSpacing(4)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_52 = QLabel(self.frame_48)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_52.addWidget(self.label_52)

        self.lineEdit_52 = QLineEdit(self.frame_48)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.lineEdit_52)

        self.horizontalLayout_52.setStretch(0, 3)
        self.horizontalLayout_52.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_48, 7, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Tahoma")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;\n"
"font: 700 18pt \"Tahoma\";")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)

        self.frame_40 = QFrame(self.frame)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_44 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_44.setSpacing(4)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.frame_40)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.label_44)

        self.lineEdit_44 = QLineEdit(self.frame_40)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.lineEdit_44)

        self.horizontalLayout_44.setStretch(0, 3)
        self.horizontalLayout_44.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_40, 8, 0, 1, 1)

        self.frame_49 = QFrame(self.frame)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_53 = QHBoxLayout(self.frame_49)
        self.horizontalLayout_53.setSpacing(4)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.frame_49)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_53)

        self.lineEdit_53 = QLineEdit(self.frame_49)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        self.lineEdit_53.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.lineEdit_53)

        self.horizontalLayout_53.setStretch(0, 3)
        self.horizontalLayout_53.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_49, 8, 2, 1, 1)

        self.frame_39 = QFrame(self.frame)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_43 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_43.setSpacing(4)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_39)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_43.addWidget(self.label_43)

        self.lineEdit_43 = QLineEdit(self.frame_39)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.lineEdit_43)

        self.horizontalLayout_43.setStretch(0, 3)
        self.horizontalLayout_43.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_39, 7, 0, 1, 1)

        self.checkBox_2 = QCheckBox(self.frame)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setLayoutDirection(Qt.RightToLeft)
        self.checkBox_2.setStyleSheet(u"background-color: transparent;")

        self.gridLayout.addWidget(self.checkBox_2, 9, 2, 1, 1)

        self.frame_34 = QFrame(self.frame)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_38 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_38.setSpacing(4)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_38 = QLabel(self.frame_34)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.label_38)

        self.lineEdit_38 = QLineEdit(self.frame_34)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.lineEdit_38)

        self.horizontalLayout_38.setStretch(0, 3)
        self.horizontalLayout_38.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_34, 5, 1, 1, 1)

        self.frame_44 = QFrame(self.frame)
        self.frame_44.setObjectName(u"frame_44")
        self.frame_44.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_48 = QHBoxLayout(self.frame_44)
        self.horizontalLayout_48.setSpacing(4)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.frame_44)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_48.addWidget(self.label_48)

        self.lineEdit_48 = QLineEdit(self.frame_44)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.lineEdit_48)

        self.horizontalLayout_48.setStretch(0, 3)
        self.horizontalLayout_48.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_44, 4, 2, 1, 1)

        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_31 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_31.setSpacing(4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.frame_28)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_31.addWidget(self.label_31)

        self.lineEdit_31 = QLineEdit(self.frame_28)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.lineEdit_31)

        self.horizontalLayout_31.setStretch(0, 3)
        self.horizontalLayout_31.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_28, 3, 1, 1, 1)

        self.frame_36 = QFrame(self.frame)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_40 = QHBoxLayout(self.frame_36)
        self.horizontalLayout_40.setSpacing(4)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_36)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_40.addWidget(self.label_40)

        self.lineEdit_40 = QLineEdit(self.frame_36)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.lineEdit_40)

        self.horizontalLayout_40.setStretch(0, 3)
        self.horizontalLayout_40.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_36, 5, 0, 1, 1)

        self.frame_32 = QFrame(self.frame)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_36 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_36.setSpacing(4)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.frame_32)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_36.addWidget(self.label_36)

        self.lineEdit_36 = QLineEdit(self.frame_32)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.lineEdit_36)

        self.horizontalLayout_36.setStretch(0, 3)
        self.horizontalLayout_36.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_32, 6, 0, 1, 1)

        self.frame_38 = QFrame(self.frame)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_42 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_42.setSpacing(4)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.label_42 = QLabel(self.frame_38)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_42.addWidget(self.label_42)

        self.lineEdit_42 = QLineEdit(self.frame_38)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.lineEdit_42)

        self.horizontalLayout_42.setStretch(0, 3)
        self.horizontalLayout_42.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_38, 3, 2, 1, 1)

        self.btnavarage = QCheckBox(self.frame)
        self.btnavarage.setObjectName(u"btnavarage")
        self.btnavarage.setLayoutDirection(Qt.RightToLeft)
        self.btnavarage.setStyleSheet(u"background-color: transparent;")

        self.gridLayout.addWidget(self.btnavarage, 9, 1, 1, 1)

        self.frame_43 = QFrame(self.frame)
        self.frame_43.setObjectName(u"frame_43")
        self.frame_43.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_47 = QHBoxLayout(self.frame_43)
        self.horizontalLayout_47.setSpacing(4)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_47 = QLabel(self.frame_43)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_47.addWidget(self.label_47)

        self.lineEdit_47 = QLineEdit(self.frame_43)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.lineEdit_47)

        self.horizontalLayout_47.setStretch(0, 3)
        self.horizontalLayout_47.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_43, 6, 2, 1, 1)

        self.frame_41 = QFrame(self.frame)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_45 = QHBoxLayout(self.frame_41)
        self.horizontalLayout_45.setSpacing(4)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.frame_41)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_45.addWidget(self.label_45)

        self.lineEdit_45 = QLineEdit(self.frame_41)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.lineEdit_45)

        self.horizontalLayout_45.setStretch(0, 3)
        self.horizontalLayout_45.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_41, 2, 2, 1, 1)

        self.frame_37 = QFrame(self.frame)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setStyleSheet(u"QFrame{\n"
"	border-width:0px;\n"
"	background-color: transparent;\n"
"}")
        self.horizontalLayout_41 = QHBoxLayout(self.frame_37)
        self.horizontalLayout_41.setSpacing(4)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.frame_37)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_41.addWidget(self.label_41)

        self.lineEdit_41 = QLineEdit(self.frame_37)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.lineEdit_41)

        self.horizontalLayout_41.setStretch(0, 3)
        self.horizontalLayout_41.setStretch(1, 1)

        self.gridLayout.addWidget(self.frame_37, 4, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setColumnStretch(0, 1)

        self.gridLayout_3.addWidget(self.frame, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.gridLayout_3.setRowStretch(1, 4)
        self.gridLayout_3.setRowStretch(2, 1)
        self.gridLayout_3.setColumnStretch(1, 4)
        self.gridLayout_3.setColumnStretch(2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tab_2.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setSpacing(2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.tab_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.graphWidget_2 = PlotWidget(self.frame_5)
        self.graphWidget_2.setObjectName(u"graphWidget_2")

        self.gridLayout_7.addWidget(self.graphWidget_2, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_5, 1, 0, 1, 1)

        self.frame_6 = QFrame(self.tab_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_6)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.graphWidget_3 = PlotWidget(self.frame_6)
        self.graphWidget_3.setObjectName(u"graphWidget_3")

        self.gridLayout_8.addWidget(self.graphWidget_3, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.tab_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_4)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.graphWidget = PlotWidget(self.frame_4)
        self.graphWidget.setObjectName(u"graphWidget")

        self.gridLayout_6.addWidget(self.graphWidget, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_4, 0, 0, 1, 2)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 841, 17))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.currentChanged.connect(self.btnstop.click)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btnrun.setText(QCoreApplication.translate("MainWindow", u"Run", None))
        self.btnstop.setText(QCoreApplication.translate("MainWindow", u"Stop", None))
        self.btnload.setText(QCoreApplication.translate("MainWindow", u"Load", None))
        self.btnsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btnclose.setText(QCoreApplication.translate("MainWindow", u"Close", None))
        self.pushButton_6.setText("")
        self.pushButton_7.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Experiment name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u" Output location", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Working directory", None))
        self.btnbrowse.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"B1 frequency (Hz)", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Polarizing current (A)", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Polarizing duration (ms)", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"MRI", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Real_Time Denoising", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btnavarage.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuHelp.setTitle(QCoreApplication.translate("MainWindow", u"Help", None))
    # retranslateUi

