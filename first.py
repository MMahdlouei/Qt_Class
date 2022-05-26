
from MainWindow import Ui_MainWindow
import sys
from PySide2.QtWidgets import QApplication, QMainWindow
from PySide2.QtCore import QFile


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())