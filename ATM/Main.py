from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import Qt, QPixmap
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from MainWindow import Ui_MainWindow

class State():
    Main = 0
    InsertCard = 1

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.state = State.Main
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.btncard.hide()
        self.MyButtons = QButtonGroup(self, exclusive = False)
        self.MyButtons.addButton(self.btnl1, 1)
        self.MyButtons.addButton(self.btnl2, 2)
        self.MyButtons.addButton(self.btnl3, 3)
        self.MyButtons.addButton(self.btnl4, 4)
        self.MyButtons.addButton(self.btnr1, 5)
        self.MyButtons.addButton(self.btnr2, 6)
        self.MyButtons.addButton(self.btnr3, 7)
        self.MyButtons.addButton(self.btnr4, 8)
        self.MyButtons.buttonClicked.connect(self.press)

    def update(self, i):
                self.btncard.setGeometry(QRect(i, i, 211, 290)) 
                
    def press(self, mybtn):
        
        btn = self.MyButtons.id(mybtn)
        if(self.state == State.Main):
            self.label.setPixmap(QPixmap(u":/Images/Images/main1.png"))
            self.btncard.show()
            self.newtimer = QTimer()
            self.newtimer.start(100)
            self.newtimer.timeout.connect(self.update)
               
            self.state = State.InsertCard
        elif self.state == 3:
            if(btn == 5):
                self.label.setPixmap(QPixmap(u":/Images/Images/main6.png"))
                self.state = 6
            elif (btn == 1):
                self.label.setPixmap(QPixmap(u":/Images/Images/main13.png"))
                self.state = 13
        elif (self.state == 1):
            pass
        elif(self.state == 2):
            pass
        elif(self.state == 6):
            self.label.setPixmap(QPixmap(u":/Images/Images/main8.png"))
            self.state = 8
            timer = QTimer()
            timer.timeout.connect(lambda:self.label.setPixmap(QPixmap(u":/Images/Images/main10.png")))
            timer.start(3000)
            self.state= 10
            
        print(self.state) 


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())