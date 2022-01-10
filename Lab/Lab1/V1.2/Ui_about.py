from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Ui_about(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(400, 300)
        font_text = QtGui.QFont()
        font_text.setFamily("Terminal")
        font_text.setPointSize(20)
        self.centralwidget = QtWidgets.QWidget(About)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 380, 280))
        self.textBrowser.setFont(font_text)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAlignment(Qt.AlignRight)
        About.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  #设置窗体总显示在最上面
        self.retranslateUi(About)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        _translate = QtCore.QCoreApplication.translate
        About.setWindowTitle(_translate("About", "About"))
        file = open('files/about.txt', 'r')
        data = file.readlines()
        s = ''.join(data)
        self.textBrowser.setText(s)
