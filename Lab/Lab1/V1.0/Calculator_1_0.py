import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Calculator_1_0(QWidget):
    def setupUi(self, Calculator_1_0):
        super().__init__()
        Calculator_1_0.setObjectName("Calculator_1_0")
        Calculator_1_0.setFixedSize(360, 500)  # 固定窗口大小
        font_text = QtGui.QFont()
        font_text.setFamily("Terminal")
        font_text.setPointSize(20)
        font_btn = QtGui.QFont()
        font_btn.setFamily("Times New Roman")
        font_btn.setPointSize(15)
        self.current = ''  # 内部算式
        self.centralwidget = QtWidgets.QWidget(Calculator_1_0)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 300, 100))
        self.textBrowser.setFont(font_text)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAlignment(Qt.AlignRight)
        self.pushButton_C = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_C.setGeometry(QtCore.QRect(10, 150, 70, 50))
        self.pushButton_C.setFont(font_btn)
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_C.clicked.connect(self.press_btn)
        self.pushButton_Del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Del.setGeometry(QtCore.QRect(100, 150, 70, 50))
        self.pushButton_Del.setFont(font_btn)
        self.pushButton_Del.setObjectName("pushButton_Del")
        self.pushButton_Del.clicked.connect(self.press_btn)
        self.pushButton_Sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sqrt.setGeometry(QtCore.QRect(190, 150, 70, 50))
        self.pushButton_Sqrt.setFont(font_btn)
        self.pushButton_Sqrt.setObjectName("pushButton_Sqrt")
        self.pushButton_Sqrt.clicked.connect(self.press_btn)
        self.pushButton_Div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Div.setGeometry(QtCore.QRect(280, 150, 70, 50))
        self.pushButton_Div.setFont(font_btn)
        self.pushButton_Div.setObjectName("pushButton_Div")
        self.pushButton_Div.clicked.connect(self.press_btn)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 210, 70, 50))
        self.pushButton_7.setFont(font_btn)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.press_btn)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 210, 70, 50))
        self.pushButton_8.setFont(font_btn)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.press_btn)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(190, 210, 70, 50))
        self.pushButton_9.setFont(font_btn)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.press_btn)
        self.pushButton_Times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Times.setGeometry(QtCore.QRect(280, 210, 70, 50))
        self.pushButton_Times.setFont(font_btn)
        self.pushButton_Times.setObjectName("pushButton_Times")
        self.pushButton_Times.clicked.connect(self.press_btn)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 270, 70, 50))
        self.pushButton_4.setFont(font_btn)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.press_btn)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(100, 270, 70, 50))
        self.pushButton_5.setFont(font_btn)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.press_btn)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(190, 270, 70, 50))
        self.pushButton_6.setFont(font_btn)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.press_btn)
        self.pushButton_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Minus.setGeometry(QtCore.QRect(280, 270, 70, 50))
        self.pushButton_Minus.setFont(font_btn)
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        self.pushButton_Minus.clicked.connect(self.press_btn)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(10, 330, 70, 50))
        self.pushButton_1.setFont(font_btn)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.press_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 330, 70, 50))
        self.pushButton_2.setFont(font_btn)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.press_btn)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(190, 330, 70, 50))
        self.pushButton_3.setFont(font_btn)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.press_btn)
        self.pushButton_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plus.setGeometry(QtCore.QRect(280, 330, 70, 50))
        self.pushButton_Plus.setFont(font_btn)
        self.pushButton_Plus.setObjectName("pushButton_Plus")
        self.pushButton_Plus.clicked.connect(self.press_btn)
        self.pushButton_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign.setGeometry(QtCore.QRect(10, 390, 70, 50))
        self.pushButton_Sign.setFont(font_btn)
        self.pushButton_Sign.setObjectName("pushButton_Sign")
        self.pushButton_Sign.clicked.connect(self.press_btn)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(100, 390, 70, 50))
        self.pushButton_0.setFont(font_btn)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_0.clicked.connect(self.press_btn)
        self.pushButton_Dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dot.setGeometry(QtCore.QRect(190, 390, 70, 50))
        self.pushButton_Dot.setFont(font_btn)
        self.pushButton_Dot.setObjectName("pushButton_Dot")
        self.pushButton_Dot.clicked.connect(self.press_btn)
        self.pushButton_Eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Eq.setGeometry(QtCore.QRect(280, 390, 70, 50))
        self.pushButton_Eq.setFont(font_btn)
        self.pushButton_Eq.setObjectName("pushButton_Eq")
        self.pushButton_Eq.clicked.connect(self.press_btn)
        Calculator_1_0.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator_1_0)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        Calculator_1_0.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator_1_0)
        self.statusbar.setObjectName("statusbar")
        Calculator_1_0.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())
        self.retranslateUi(Calculator_1_0)
        QtCore.QMetaObject.connectSlotsByName(Calculator_1_0)

    def retranslateUi(self, Calculator_1_0):
        _translate = QtCore.QCoreApplication.translate
        Calculator_1_0.setWindowTitle(
            _translate("Calculator_1_0", "Calculator V1.0"))
        self.textBrowser.setText('0')
        self.pushButton_C.setText(_translate("Calculator_1_0", "C"))
        self.pushButton_Del.setText(_translate("Calculator_1_0", "←"))
        self.pushButton_Sqrt.setText(_translate("Calculator_1_0", "√"))
        self.pushButton_Div.setText(_translate("Calculator_1_0", "÷"))
        self.pushButton_7.setText(_translate("Calculator_1_0", "7"))
        self.pushButton_8.setText(_translate("Calculator_1_0", "8"))
        self.pushButton_9.setText(_translate("Calculator_1_0", "9"))
        self.pushButton_Times.setText(_translate("Calculator_1_0", "×"))
        self.pushButton_4.setText(_translate("Calculator_1_0", "4"))
        self.pushButton_5.setText(_translate("Calculator_1_0", "5"))
        self.pushButton_6.setText(_translate("Calculator_1_0", "6"))
        self.pushButton_Minus.setText(_translate("Calculator_1_0", "-"))
        self.pushButton_1.setText(_translate("Calculator_1_0", "1"))
        self.pushButton_2.setText(_translate("Calculator_1_0", "2"))
        self.pushButton_3.setText(_translate("Calculator_1_0", "3"))
        self.pushButton_Plus.setText(_translate("Calculator_1_0", "+"))
        self.pushButton_Sign.setText(_translate("Calculator_1_0", "+/-"))
        self.pushButton_0.setText(_translate("Calculator_1_0", "0"))
        self.pushButton_Dot.setText(_translate("Calculator_1_0", "."))
        self.pushButton_Eq.setText(_translate("Calculator_1_0", "="))
        self.menu.setTitle(_translate("Calculator_1_0", "计算"))

    def press_btn(self):
        button_text = self.sender()
        if button_text.text() == 'C':
            self.current = ''
            self.textBrowser.setText('0')
        elif button_text.text() == '←':
            self.current = self.current[:-1]
            if self.current == '':
                self.textBrowser.setText('0')
            else:
                self.textBrowser.setText(self.current)
        elif button_text.text() == '+/-':
            if self.current == '':
                return
            if self.current[0] == '-':
                self.current = self.current[1:]
            else:
                self.current = "-" + self.current
            self.textBrowser.setText(self.current)
        elif button_text.text() == '=':
            try:
                i = 0
                if '×' in self.current:
                    self.current = self.current.replace('×', '*')
                if '÷' in self.current:
                    self.current = self.current.replace('÷', "/")
                while '√' in self.current:
                    i = self.current.find('√')
                    j = i + 1
                    while j < len(self.current) and self.current[j].isdigit():
                        j += 1
                    self.current = self.current[:j] + ")" + self.current[j:]
                    self.current = self.current[:
                                                i] + "math.sqrt(" + self.current[
                                                    i + 1:]
                self.current = str(eval(self.current))
                self.textBrowser.setText(self.textBrowser.toPlainText() +
                                         "\n=" + self.current)
            except Exception as e:
                QMessageBox.about(self, '表达式语法错误', '错误信息：' + str(e))
        else:
            self.current += button_text.text()
            self.textBrowser.setText(self.current)
