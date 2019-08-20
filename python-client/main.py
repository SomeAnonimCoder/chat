import sys
from websocket_client import Client
import design
from PyQt5 import QtWidgets
class ChatUI(design.Ui_ChatClient):
    MainWindow = None

    def showMessages(self, html):
        self.MainWindow.messageview.setHTML(html)

    def sendMessage(self):


    def _main(self):
        app = QtWidgets.QApplication(sys.argv)
        ChatClient = QtWidgets.QMainWindow()
        ui = ChatUI()
        self.MainWindow = ui
        ui.setupUi(ChatClient)
        ui.sendbutton.pressed.connect(self.sendMessage)
        ChatClient.show()
        sys.exit(app.exec_())

if __name__=="__main__":
    gui = ChatUI()
    gui._main()