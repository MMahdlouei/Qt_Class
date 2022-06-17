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
        MainWindow.resize(658, 99)
        MainWindow.setMinimumSize(QSize(658, 99))
        MainWindow.setMaximumSize(QSize(658, 99))
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.linebrowse = QLineEdit(self.splitter)
        self.linebrowse.setObjectName(u"linebrowse")
        self.linebrowse.setMinimumSize(QSize(420, 0))
        self.linebrowse.setMaximumSize(QSize(16777215, 23))
        self.splitter.addWidget(self.linebrowse)
        self.btnbrowse = QPushButton(self.splitter)
        self.btnbrowse.setObjectName(u"btnbrowse")
        self.btnbrowse.setMaximumSize(QSize(75, 23))
        self.splitter.addWidget(self.btnbrowse)

        self.verticalLayout.addWidget(self.splitter)

        self.splitter_2 = QSplitter(self.centralwidget)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.linesave = QLineEdit(self.splitter_2)
        self.linesave.setObjectName(u"linesave")
        self.linesave.setMinimumSize(QSize(420, 0))
        self.linesave.setMaximumSize(QSize(16777215, 23))
        self.splitter_2.addWidget(self.linesave)
        self.btnsave = QPushButton(self.splitter_2)
        self.btnsave.setObjectName(u"btnsave")
        self.btnsave.setMaximumSize(QSize(75, 23))
        self.splitter_2.addWidget(self.btnsave)

        self.verticalLayout.addWidget(self.splitter_2)

        self.btnconvert = QPushButton(self.centralwidget)
        self.btnconvert.setObjectName(u"btnconvert")

        self.verticalLayout.addWidget(self.btnconvert)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Converter", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btnbrowse.setText(QCoreApplication.translate("MainWindow", u"Browseeeeeeee", None))
        self.btnsave.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.btnconvert.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
    # retranslateUi

