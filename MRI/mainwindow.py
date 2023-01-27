# This Python file uses the following encoding: utf-8
from pickle import TRUE
import sys
import os

from PySide2.QtCore import QTimer
from random import randrange
from PySide2.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg
import threading

uiclass, baseclass = pg.Qt.loadUiType("form.ui")

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
os.system("pyside2-uic form.ui -o ui_form.py")
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.firsttime = True
        self.ui.btnrun.clicked.connect(self.Run)
        self.flag=True
        self.j=0
        self.timer = QTimer()
        self.timer.timeout.connect(self.plott)
        #self.ui.pushButton_2.clicked.connect(self.timer.stop)
        self.ui.tabWidget.currentChanged.connect(self.TabChanged)
   
        

        # circular buffer for storing serial data until it is
        # fetched by the GUI
        self.j=0
        self.sps = 0.0              # holds the average sample acquisition rate

        # self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        
    def TabChanged(self, index):
        if(index == self.ui.tabWidget.indexOf(self.ui.tab)):
            self.timer.stop()
            print("tab1")
        elif(index == self.ui.tabWidget.indexOf(self.ui.tab_2)):
            self.timer.start(20)
            print("tab2")

    def plott(self):
        
        if True:
            # see whether an exit was requested
            self.j=self.j+1
            hour=[1, 2, 3, 4]      
            temperature=[1, 2, 3, randrange(10)] 

            # self.ui.graphWidget.plot(hour, temperature)

            if(self.firsttime) :
                self.plotItem =self.ui.graphWidget.plot(hour, temperature)
                self.firsttime = False

            else:
                self.plotItem.setData(hour, temperature)
                print("amjikh")

            # self.ui.graphWidget_2.plot(hour, temperature)
            # self.ui.graphWidget_3.plot(hour, temperature)




    def Run(self):
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.indexOf(self.ui.tab_2)) 
        hour=[1,2,3,4,5,6,7,8,9,10]     
        temperature=[30,32,34,32,33,31,29,32,35,45]

  #      thread = threading.Thread(target=self.plott, args=(hour,temperature,))
 #       thread.start()
        #self.timer.start(20)
       

    def exit(self):
        """ Instruct the serial thread to exit."""
        with self.exitMutex:
            self.exitFlag = True        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
