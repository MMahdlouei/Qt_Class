import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtWidgets
from PySide2.QtCore import QFile
from MainWindow import Ui_MainWindow
import math



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.btn0.clicked.connect(lambda:self.pressed("0"))
        self.btn1.clicked.connect(lambda:self.pressed("1"))
        self.btn2.clicked.connect(lambda:self.pressed("2"))
        self.btn3.clicked.connect(lambda:self.pressed("3"))
        self.btn4.clicked.connect(lambda:self.pressed("4"))
        self.btn5.clicked.connect(lambda:self.pressed("5"))
        self.btn6.clicked.connect(lambda:self.pressed("6"))
        self.btn7.clicked.connect(lambda:self.pressed("7"))
        self.btn8.clicked.connect(lambda:self.pressed("8"))
        self.btn9.clicked.connect(lambda:self.pressed("9"))
        self.btnminus.clicked.connect(lambda:self.pressed("-"))
        self.btnplus.clicked.connect(lambda:self.pressed("+"))
        self.btnmulti.clicked.connect(lambda:self.pressed("*"))
        self.btndevide.clicked.connect(lambda:self.pressed("/"))
        self.btnequal.clicked.connect(lambda:self.pressed("="))


    def pressed(self, text):
        temp = self.lbl.text()
        if temp == "0" :
            self.lbl.setText("")
        
            
        elif text == "-" or text == "+" or text == "/" or text == "*":
            if temp[-1] == "+" or temp[-1] == "-" or temp[-1] == "*" or temp[-1] == "/":
                self.lbl.setText(temp[:-1])
                
        if text == "=":
            self.lbl.setText(str(eval(self.lbl.text())))
        else:    
            self.lbl.setText(self.lbl.text() + text)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())