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
        MainWindow.resize(1377, 768)
        MainWindow.setStyleSheet(u"background-color: rgb(94, 103, 103);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(94, 103, 103);")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 1191, 771))
        self.label.setPixmap(QPixmap(u":/Images/Images/main0.png"))
        self.label.setScaledContents(True)
        self.btnl1 = QPushButton(self.centralwidget)
        self.btnl1.setObjectName(u"btnl1")
        self.btnl1.setGeometry(QRect(0, 290, 91, 91))
        self.btnl1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnl1.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/lsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnl1.setFlat(True)
        self.btnl2 = QPushButton(self.centralwidget)
        self.btnl2.setObjectName(u"btnl2")
        self.btnl2.setGeometry(QRect(0, 430, 91, 91))
        self.btnl2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnl2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/lsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnl3 = QPushButton(self.centralwidget)
        self.btnl3.setObjectName(u"btnl3")
        self.btnl3.setGeometry(QRect(0, 570, 91, 91))
        self.btnl3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnl3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/lsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnl4 = QPushButton(self.centralwidget)
        self.btnl4.setObjectName(u"btnl4")
        self.btnl4.setGeometry(QRect(0, 680, 91, 91))
        self.btnl4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnl4.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/lsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnl4.setFlat(True)
        self.btnr3 = QPushButton(self.centralwidget)
        self.btnr3.setObjectName(u"btnr3")
        self.btnr3.setGeometry(QRect(1280, 570, 91, 91))
        self.btnr3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnr3.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/rsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnr2 = QPushButton(self.centralwidget)
        self.btnr2.setObjectName(u"btnr2")
        self.btnr2.setGeometry(QRect(1280, 430, 91, 91))
        self.btnr2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnr2.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/rsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnr1 = QPushButton(self.centralwidget)
        self.btnr1.setObjectName(u"btnr1")
        self.btnr1.setGeometry(QRect(1280, 290, 91, 91))
        self.btnr1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnr1.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/rsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btnr4 = QPushButton(self.centralwidget)
        self.btnr4.setObjectName(u"btnr4")
        self.btnr4.setGeometry(QRect(1280, 680, 91, 91))
        self.btnr4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnr4.setStyleSheet(u"QPushButton\n"
"{\n"
"	border-image: url(:/Images/Images/rsoftkey.png);\n"
"	background-color: rgb(92, 101, 101);\n"
"}\n"
"QPushButton::hover\n"
"{\n"
"	border:5px;\n"
"}\n"
"QPushButton::pressed\n"
"{\n"
"	border:-5px;\n"
"}")
        self.btncard = QPushButton(self.centralwidget)
        self.btncard.setObjectName(u"btncard")
        self.btncard.setGeometry(QRect(0, 0, 211, 290))
        self.btncard.setStyleSheet(u"border-image: url(:/Images/Images/InsertCard.png);")
        MainWindow.setCentralWidget(self.centralwidget)
        self.btnl1.raise_()
        self.btnl2.raise_()
        self.btnl3.raise_()
        self.btnl4.raise_()
        self.btnr3.raise_()
        self.btnr2.raise_()
        self.btnr4.raise_()
        self.btnr1.raise_()
        self.label.raise_()
        self.btncard.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.btnl1.setText("")
        self.btnl2.setText("")
        self.btnl3.setText("")
        self.btnl4.setText("")
        self.btnr3.setText("")
        self.btnr2.setText("")
        self.btnr1.setText("")
        self.btnr4.setText("")
        self.btncard.setText("")
    # retranslateUi

