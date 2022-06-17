from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide2 import QtWidgets
from MainWindow import Ui_MainWindow



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.btnbrowse.clicked.connect(self.Browse)
        self.btnsave.clicked.connect(self.Save)
        self.btnconvert.clicked.connect(self.Convert)

    def Browse(self):
        uifile = QFileDialog.getOpenFileName(self, "Select Your UI File", "", "UI Files (*.ui) ;; All Files(*.*)")
        self.linebrowse.setText(uifile[0])

    def Save(self):
        pyfile = QFileDialog.getSaveFileName(self, "Save Your Python File", "MainWindow", "Python Files (*.py) ;; All Files(*.*)")
        self.linesave.setText(pyfile[0])

    def Convert(self):
        import os
        mycommand = "pyside2-uic " + self.linebrowse.text() + " -o " + self.linesave.text()
        #print(mycommand)
        os.system(mycommand)
        if os.path.isfile(self.linesave.text()):
            message = QMessageBox(self)
            message.setText("Convert Is Succesfull!")
            message.setWindowTitle("Succed!")
            message.buttonClicked.connect(app.quit)
            message.exec_()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())