from PySide2.QtWidgets import QApplication
from PySide2 import QtWidgets
from MainWindow import Ui_MainWindow
import serial
import serial.tools.list_ports


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.Message = bytearray(32) #defining a variable with 32 bytes of data, if u want to change bits u need to use shift and | and & operators
        self.Message[0] = 0xFF
        self.Message[1] = self.CreateByte(1, 0, 1, 0, 1, 0, 0, 1)#set 8 bits in one byte
        self.DisEnable(False)
        self.btnConnect.clicked.connect(self.ConnectSerial)
        self.btnDisconnect.clicked.connect(self.DisconnectSerial)
        self.lineEdit.setInputMask("0x-HH");
        #self.btnSend.clicked.connect(lambda : self.ser.write(self.Message)) u can use this instead of defining function
        self.btnSend.clicked.connect(self.SendSerial)
        Ports = serial.tools.list_ports.comports() # make a list from available COM ports. u should print this to see whole list
        for this in Ports:
            #com = str(this)
            #self.comboBox.addItem(com[com.find('COM'):com.find('COM')+5])
            self.comboBox.addItem(str(this))
    
    def ConnectSerial(self):
        com = self.comboBox.currentText()
        com = com[com.find('COM'):com.find('COM')+4]#select only COM# from whole text, u need to put com# in next line
        self.ser = serial.Serial(
            port = com,#u can pu any com u want here for example "COM4" or "COM3". it need to be string
            baudrate = 115200,
            parity = serial.PARITY_NONE,
            stopbits = serial.STOPBITS_ONE,
            bytesize = serial.EIGHTBITS,
            timeout = 100)
        if self.ser.isOpen():# returns true if port was open
            self.DisEnable(True)
        
    def DisconnectSerial(self):
        self.ser.close()
        if not self.ser.isOpen():
            self.DisEnable(False)

    def DisEnable(self, mode):#this function will change buttons and combobox state with opening and closing com port 
        if mode:
            self.btnConnect.setDisabled(mode)
            self.comboBox.setDisabled(mode)
            self.btnSend.setEnabled(mode)
            self.btnDisconnect.setEnabled(mode)
        else:
            self.btnConnect.setEnabled(~mode)
            self.comboBox.setEnabled(~mode)
            self.btnSend.setDisabled(~mode)
            self.btnDisconnect.setDisabled(~mode)

    def SendSerial(self):
        self.ser.write(self.Message) #u should update your message content before send

    def CreateByte(self, bit0, bit1, bit2, bit3, bit4, bit5, bit6, bit7):#just a sample funtion for creating byte from bits
        return  bit0 | bit1<<1 | bit2<<2  | bit3 << 3 | bit4 << 4 | bit5 << 5 | bit6 << 6 | bit7 << 7        



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())