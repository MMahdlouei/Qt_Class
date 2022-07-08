from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets, QtCore
from MainWindow import Ui_MainWindow
from Setting import Ui_Setting

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.actionExit.triggered.connect(app.quit)
        self.actionOptions.triggered.connect(self.ShowSettingWindow)
       
        self.SettingWindow = Setting()
        self.SettingWindow.btnOk.clicked.connect(self.CloseSettingWindow)
        self.SettingWindow.btnCancel.clicked.connect(self.CloseSettingWindow)
        self.SettingWindow.comboBox.currentTextChanged.connect(self.ChangeColorFromComboBox)
        self.SettingWindow.scrRed.valueChanged.connect(self.ChangeColor)
        self.SettingWindow.scrGreen.valueChanged.connect(self.ChangeColor)
        self.SettingWindow.scrBlue.valueChanged.connect(self.ChangeColor)
        
        
        #self.SettingWindow.show()

    def ChangeColorFromComboBox(self):
        self.setStyleSheet(u"background-color:  "+self.SettingWindow.comboBox.currentText()+";")
    
    def ShowSettingWindow(self):
       
       self.SettingWindow.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
       self.SettingWindow.show()

    
    def CloseSettingWindow(self):
        self.SettingWindow.close()
        color = self.SettingWindow.comboBox.currentText()
        bluecolor = self.SettingWindow.scrBlue.value()
        redcolor = self.SettingWindow.scrRed.value()
        greencolor = self.SettingWindow.scrGreen.value()
        #self.setStyleSheet(u"background-color: "+color+";")
        #self.setStyleSheet(u"background-color:  rgb({}, {}, {});".format(redcolor, greencolor, bluecolor))
    
    def ChangeColor(self):
        self.setStyleSheet(u"background-color:  rgb({}, {}, {});".format(self.SettingWindow.scrRed.value(), self.SettingWindow.scrGreen.value(), self.SettingWindow.scrBlue.value()))
        
    def closeEvent(self, event):
        sys.exit()

class Setting(QtWidgets.QMainWindow, Ui_Setting):
    def __init__(self):
        super(Setting, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())