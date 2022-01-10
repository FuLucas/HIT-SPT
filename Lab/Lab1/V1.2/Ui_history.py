from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_history(object):
    def setupUi(self, History):
        History.setObjectName("History")
        History.resize(400, 300)
        font_text = QtGui.QFont()
        font_text.setFamily("Terminal")
        font_text.setPointSize(20)
        self.centralwidget = QtWidgets.QWidget(History)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 380, 280))
        self.textBrowser.setFont(font_text)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAlignment(Qt.AlignRight)
        History.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  #设置窗体总显示在最上面
        self.retranslateUi(History)
        QtCore.QMetaObject.connectSlotsByName(History)

    def retranslateUi(self, History):
        _translate = QtCore.QCoreApplication.translate
        History.setWindowTitle(_translate("History", "History"))
        file = open('files/history.txt', 'r')
        data = file.readlines()
        file.close()
        str = ''.join(data)
        self.textBrowser.setText(str)

