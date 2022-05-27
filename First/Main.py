import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2 import QtWidgets
from PySide2.QtCore import QFile
from MainWindow import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.press)


    def press(self):
        self.label.setText(self.ui.label.text() + " new text ")

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())