# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import MyResources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(50,50, 50, 255), stop:1 rgba(225, 225, 225, 255));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnonoff = QPushButton(self.centralwidget)
        self.btnonoff.setObjectName(u"btnonoff")
        self.btnonoff.setGeometry(QRect(120, 220, 261, 91))
        self.btnonoff.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnonoff.setStyleSheet(u"QPushButton\n"
"{\n"
"	border:none;\n"
"	background:none;\n"
"	border-image: url(:/Images/Images/off.png);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"	border:-3px;\n"
"}\n"
"QPushButton:checked\n"
"{\n"
"	border-image: url(:/Images/Images/on.png);\n"
"}\n"
"QPushButton:pressed:!checked\n"
"{\n"
"	border:3px;\n"
"	border-image: url(:/Images/Images/on.png);\n"
"}\n"
"QPushButton:pressed:checked\n"
"{\n"
"	border:3px;\n"
"	border-image: url(:/Images/Images/off.png);\n"
"}\n"
"\n"
"\n"
"")
        self.btnonoff.setIconSize(QSize(230, 80))
        self.btnonoff.setCheckable(True)
        self.btnonoff.setFlat(True)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(450, 160, 231, 211))
        self.label.setStyleSheet(u"background:none;")
        self.label.setPixmap(QPixmap(u":/Images/Images/red.png"))
        self.label.setScaledContents(True)
        self.btnexit = QPushButton(self.centralwidget)
        self.btnexit.setObjectName(u"btnexit")
        self.btnexit.setGeometry(QRect(710, 12, 81, 61))
        self.btnexit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnexit.setStyleSheet(u"QPushButton\n"
"{\n"
"font: 75 16pt \"Comic Sans MS\";\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(150,150, 150, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:hover\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(200,200, 200, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(50,50, 50, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnonoff.setText("")
        self.label.setText("")
        self.btnexit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
    # retranslateUi

