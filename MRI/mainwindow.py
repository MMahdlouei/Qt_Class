# This Python file uses the following encoding: utf-8
import sys
import os

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
        self.ui.btnrun.clicked.connect(self.Run)
        self.flag=True
        self.j=0

        # circular buffer for storing serial data until it is
        # fetched by the GUI
        self.j=0
        self.sps = 0.0              # holds the average sample acquisition rate
        self.exitFlag = False
        self.exitMutex = threading.Lock()
        self.dataMutex = threading.Lock()
        # self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])
        
        
    def plott(self, hour,  temperature):

        while True:
            # see whether an exit was requested
            with self.exitMutex:
                if self.exitFlag:
                    break
            self.j=self.j+1
            hour=[1, 2, 3, 4]      
            temperature=[1, 2, 3, self.j+1]
   
            # self.ui.graphWidget.plot(hour, temperature)
            self.ui.graphWidget.plot(hour, temperature)
            # self.ui.graphWidget_2.plot(hour, temperature)
            # self.ui.graphWidget_3.plot(hour, temperature)

            if self.j>40:
                self.exit()
 



    def Run(self):
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.indexOf(self.ui.tab_2)) 
        hour=[1,2,3,4,5,6,7,8,9,10]     
        temperature=[30,32,34,32,33,31,29,32,35,45]

        exitMutex = self.exitMutex
        dataMutex = self.dataMutex
        count = 0
        sps = None
        # lastUpdate = time.time()
        self.thread = threading.Thread(target=self.plott, args=(hour,temperature,))
        self.thread.start()
       

    def exit(self):
        """ Instruct the serial thread to exit."""
        with self.exitMutex:
            self.exitFlag = True        
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
