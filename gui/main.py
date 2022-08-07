
import sys
from PyQt5 import QtWidgets
from win import Ui_MainWindow
from PyQt5.QtWidgets import QMessageBox
from script.encrypt import Encrypt
from script.decrypt import Decrypt


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        self.ui.encode_btn.clicked.connect(self.encode_message)

        self.ui.encode_btn_2.clicked.connect(self.decode_message)
       

    def encode_message(self):
        self.enc_key = self.ui.pass_in.text()

        self.msg = self.ui.message.toPlainText()
        
        if self.enc_key == '' or self.msg == '':
            QMessageBox.information(self,'Notice','Please password field and the message field must be empty')
        
        else:
            msg = Encrypt(self.enc_key,self.msg)

            self.ui.encrypted_message.setText(msg)

            self.ui.status.setText('Encryption successful')
            print(self.msg)


    def decode_message(self):
        self.dec_key = self.ui.pass_in_2.text()

        self.enc_msg = self.ui.message_enc.toPlainText()

        if self.dec_key == '' or self.enc_msg == '':
            
            QMessageBox.information(self,'Notice','Please password field and the message field must be empty')
        else:
            dec_msg = Decrypt(self.dec_key,self.enc_msg)
            self.ui.decrypted_message.setText(dec_msg)
            self.ui.status_2.setText('Decryption successful')
            print(self.enc_msg)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())