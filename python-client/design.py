# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chat-client.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ChatClient(object):
    def setupUi(self, ChatClient):
        ChatClient.setObjectName("ChatClient")
        ChatClient.resize(791, 585)
        self.centralwidget = QtWidgets.QWidget(ChatClient)
        self.centralwidget.setObjectName("centralwidget")
        self.sendbutton = QtWidgets.QPushButton(self.centralwidget)
        self.sendbutton.setGeometry(QtCore.QRect(640, 440, 93, 31))
        self.sendbutton.setObjectName("sendbutton")
        self.messageview = QtWidgets.QTextBrowser(self.centralwidget)
        self.messageview.setGeometry(QtCore.QRect(20, 20, 751, 321))
        self.messageview.setObjectName("messageview")
        self.messageedit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.messageedit.setGeometry(QtCore.QRect(20, 370, 601, 171))
        self.messageedit.setObjectName("messageedit")
        ChatClient.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(ChatClient)
        self.statusbar.setObjectName("statusbar")
        ChatClient.setStatusBar(self.statusbar)

        self.retranslateUi(ChatClient)
        QtCore.QMetaObject.connectSlotsByName(ChatClient)

    def retranslateUi(self, ChatClient):
        _translate = QtCore.QCoreApplication.translate
        ChatClient.setWindowTitle(_translate("ChatClient", "MainWindow"))
        self.sendbutton.setText(_translate("ChatClient", "SEND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ChatClient = QtWidgets.QMainWindow()
    ui = Ui_ChatClient()
    ui.setupUi(ChatClient)
    ChatClient.show()
    sys.exit(app.exec_())
