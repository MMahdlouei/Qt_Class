# This Python file uses the following encoding: utf-8
import sys
import os

from PySide2.QtWidgets import QApplication, QMainWindow
import pyqtgraph as pg

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
        self.plot([1,2,3,4,5,6,7,8,9,10], [30,32,34,32,33,31,29,32,35,45])

    def plot(self, hour, temperature):
        self.ui.graphWidget.plot(hour, temperature)
        self.ui.graphWidget_2.plot(hour, temperature)
        self.ui.graphWidget_3.plot(hour, temperature)
        
    def Run(self):
        self.ui.tabWidget.setCurrentIndex(self.ui.tabWidget.indexOf(self.ui.tab_2))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
