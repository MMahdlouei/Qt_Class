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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(407, 109)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnConnect = QPushButton(self.centralwidget)
        self.btnConnect.setObjectName(u"btnConnect")
        self.btnConnect.setGeometry(QRect(300, 10, 92, 23))
        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(10, 10, 281, 22))
        self.comboBox.setStyleSheet(u"font: 75 12pt \"Comic Sans MS\";\n"
"color:rgb(0, 255, 8);")
        self.btnDisconnect = QPushButton(self.centralwidget)
        self.btnDisconnect.setObjectName(u"btnDisconnect")
        self.btnDisconnect.setGeometry(QRect(300, 40, 92, 23))
        self.btnSend = QPushButton(self.centralwidget)
        self.btnSend.setObjectName(u"btnSend")
        self.btnSend.setGeometry(QRect(10, 40, 92, 23))
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 70, 113, 31))
        self.lineEdit.setFocusPolicy(Qt.ClickFocus)
        self.lineEdit.setStyleSheet(u"font: 75 16pt \"Comic Sans MS\";\n"
"color:rgb(0, 255, 21);")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnConnect.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
        self.btnDisconnect.setText(QCoreApplication.translate("MainWindow", u"Disconnect", None))
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
    # retranslateUi

