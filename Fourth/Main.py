from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import *
from MainWindow import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.btnonoff.clicked.connect(self.Pressed)
        self.btnexit.clicked.connect(app.quit)

    def Pressed(self):
        if self.btnonoff.isChecked():
            self.label.setPixmap(":/Images/Images/green.png")
            self.btnonoff.setIcon(QIcon(":/Images/Images/on.png"))
        else:
            self.label.setPixmap(":/Images/Images/red.png")
            self.btnonoff.setIcon(QIcon(":/Images/Images/off.png"))

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())