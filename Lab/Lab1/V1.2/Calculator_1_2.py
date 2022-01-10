import sys
import math
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

import Sound


class Calculator_1_2(QWidget):
    def setupUi(self, Calculator_1_2):
        super().__init__()
        self.sound = Sound.Sound(self)
        self.sound_stat = self.sound.sound_init()  # 语音初始化状态
        Calculator_1_2.setObjectName("Calculator_1_2")
        Calculator_1_2.setFixedSize(480, 558)  # 固定窗口大小

        font_text = QtGui.QFont()
        font_text.setFamily("Terminal")
        font_text.setPointSize(20)
        font_btn = QtGui.QFont()
        font_btn.setFamily("Times New Roman")
        font_btn.setPointSize(15)

        self.current = ''  # 内部算式
        self.centralwidget = QtWidgets.QWidget(Calculator_1_2)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(30, 30, 411, 100))
        self.textBrowser.setFont(font_text)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setAlignment(Qt.AlignRight)
        self.pushButton_C = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_C.setGeometry(QtCore.QRect(110, 210, 70, 50))
        self.pushButton_C.setFont(font_btn)
        self.pushButton_C.setObjectName("pushButton_C")
        self.pushButton_C.clicked.connect(self.press_btn)
        self.pushButton_Del = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Del.setGeometry(QtCore.QRect(200, 210, 70, 50))
        self.pushButton_Del.setFont(font_btn)
        self.pushButton_Del.setObjectName("pushButton_Del")
        self.pushButton_Del.clicked.connect(self.press_btn)
        self.pushButton_Sqrt = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sqrt.setGeometry(QtCore.QRect(290, 210, 70, 50))
        self.pushButton_Sqrt.setFont(font_btn)
        self.pushButton_Sqrt.setObjectName("pushButton_Sqrt")
        self.pushButton_Sqrt.clicked.connect(self.press_btn)
        self.pushButton_Div = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Div.setGeometry(QtCore.QRect(380, 210, 70, 50))
        self.pushButton_Div.setFont(font_btn)
        self.pushButton_Div.setObjectName("pushButton_Div")
        self.pushButton_Div.clicked.connect(self.press_btn)
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(110, 270, 70, 50))
        self.pushButton_7.setFont(font_btn)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.clicked.connect(self.press_btn)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(200, 270, 70, 50))
        self.pushButton_8.setFont(font_btn)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.clicked.connect(self.press_btn)
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(290, 270, 70, 50))
        self.pushButton_9.setFont(font_btn)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.clicked.connect(self.press_btn)
        self.pushButton_Times = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Times.setGeometry(QtCore.QRect(380, 270, 70, 50))
        self.pushButton_Times.setFont(font_btn)
        self.pushButton_Times.setObjectName("pushButton_Times")
        self.pushButton_Times.clicked.connect(self.press_btn)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(110, 330, 70, 50))
        self.pushButton_4.setFont(font_btn)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.press_btn)
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(200, 330, 70, 50))
        self.pushButton_5.setFont(font_btn)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.clicked.connect(self.press_btn)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 330, 70, 50))
        self.pushButton_6.setFont(font_btn)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.clicked.connect(self.press_btn)
        self.pushButton_Minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Minus.setGeometry(QtCore.QRect(380, 330, 70, 50))
        self.pushButton_Minus.setFont(font_btn)
        self.pushButton_Minus.setObjectName("pushButton_Minus")
        self.pushButton_Minus.clicked.connect(self.press_btn)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(110, 390, 70, 50))
        self.pushButton_1.setFont(font_btn)
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_1.clicked.connect(self.press_btn)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 390, 70, 50))
        self.pushButton_2.setFont(font_btn)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.press_btn)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(290, 390, 70, 50))
        self.pushButton_3.setFont(font_btn)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.press_btn)
        self.pushButton_Plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Plus.setGeometry(QtCore.QRect(380, 390, 70, 50))
        self.pushButton_Plus.setFont(font_btn)
        self.pushButton_Plus.setObjectName("pushButton_Plus")
        self.pushButton_Plus.clicked.connect(self.press_btn)
        self.pushButton_Sign = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Sign.setGeometry(QtCore.QRect(110, 450, 70, 50))
        self.pushButton_Sign.setFont(font_btn)
        self.pushButton_Sign.setObjectName("pushButton_Sign")
        self.pushButton_Sign.clicked.connect(self.press_btn)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(200, 450, 70, 50))
        self.pushButton_0.setFont(font_btn)
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_0.clicked.connect(self.press_btn)
        self.pushButton_Dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Dot.setGeometry(QtCore.QRect(290, 450, 70, 50))
        self.pushButton_Dot.setFont(font_btn)
        self.pushButton_Dot.setObjectName("pushButton_Dot")
        self.pushButton_Dot.clicked.connect(self.press_btn)
        self.pushButton_Eq = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Eq.setGeometry(QtCore.QRect(380, 450, 70, 50))
        self.pushButton_Eq.setFont(font_btn)
        self.pushButton_Eq.setObjectName("pushButton_Eq")
        self.pushButton_Eq.clicked.connect(self.press_btn)
        self.pushButton_Cos = QPushButton(self.centralwidget)
        self.pushButton_Cos.setObjectName(u"pushButton_Cos")
        self.pushButton_Cos.setGeometry(QRect(20, 270, 70, 50))
        self.pushButton_Cos.setFont(font_btn)
        self.pushButton_Cos.clicked.connect(self.press_btn)
        self.pushButton_lg = QPushButton(self.centralwidget)
        self.pushButton_lg.setObjectName(u"pushButton_lg")
        self.pushButton_lg.setGeometry(QRect(20, 390, 70, 50))
        self.pushButton_lg.setFont(font_btn)
        self.pushButton_lg.clicked.connect(self.press_btn)
        self.pushButton_Sin = QPushButton(self.centralwidget)
        self.pushButton_Sin.setObjectName(u"pushButton_Sin")
        self.pushButton_Sin.setGeometry(QRect(20, 210, 70, 50))
        self.pushButton_Sin.setFont(font_btn)
        self.pushButton_Sin.clicked.connect(self.press_btn)
        self.pushButton_Ln = QPushButton(self.centralwidget)
        self.pushButton_Ln.setObjectName(u"pushButton_Ln")
        self.pushButton_Ln.setGeometry(QRect(20, 450, 70, 50))
        self.pushButton_Ln.setFont(font_btn)
        self.pushButton_Ln.clicked.connect(self.press_btn)
        self.pushButton_Pow = QPushButton(self.centralwidget)
        self.pushButton_Pow.setObjectName(u"pushButton_Pow")
        self.pushButton_Pow.setGeometry(QRect(20, 330, 70, 50))
        self.pushButton_Pow.setFont(font_btn)
        self.pushButton_Pow.clicked.connect(self.press_btn)
        self.pushButton_Fac = QPushButton(self.centralwidget)
        self.pushButton_Fac.setObjectName(u"pushButton_Fac")
        self.pushButton_Fac.setGeometry(QRect(20, 150, 70, 50))
        self.pushButton_Fac.setFont(font_btn)
        self.pushButton_Fac.clicked.connect(self.press_btn)
        self.pushButton_Pi = QPushButton(self.centralwidget)
        self.pushButton_Pi.setObjectName(u"pushButton_Pi")
        self.pushButton_Pi.setGeometry(QRect(290, 150, 70, 50))
        self.pushButton_Pi.setFont(font_btn)
        self.pushButton_Pi.clicked.connect(self.press_btn)
        self.pushButton_LeftPar = QPushButton(self.centralwidget)
        self.pushButton_LeftPar.setObjectName(u"pushButton_LeftPar")
        self.pushButton_LeftPar.setGeometry(QRect(200, 150, 70, 50))
        self.pushButton_LeftPar.setFont(font_btn)
        self.pushButton_LeftPar.clicked.connect(self.press_btn)
        self.pushButton_Abs = QPushButton(self.centralwidget)
        self.pushButton_Abs.setObjectName(u"pushButton_Abs")
        self.pushButton_Abs.setGeometry(QRect(380, 150, 70, 50))
        self.pushButton_Abs.setFont(font_btn)
        self.pushButton_Abs.clicked.connect(self.press_btn)
        self.pushButton_RightPar = QPushButton(self.centralwidget)
        self.pushButton_RightPar.setObjectName(u"pushButton_RightPar")
        self.pushButton_RightPar.setGeometry(QRect(110, 150, 70, 50))
        self.pushButton_RightPar.setFont(font_btn)
        self.pushButton_RightPar.clicked.connect(self.press_btn)

        self.action_about = QAction(Calculator_1_2)
        self.action_about.setObjectName(u"action_about")
        self.action_about.setShortcut("Ctrl+N")
        icon_about = QtGui.QIcon()
        icon_about.addPixmap(QtGui.QPixmap("images/about.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_about.setIcon(icon_about)

        self.action_history = QAction(Calculator_1_2)
        self.action_history.setObjectName(u"action_history")
        self.action_history.setShortcut("Ctrl+T")
        icon_history = QtGui.QIcon()
        icon_history.addPixmap(QtGui.QPixmap("images/history.png"),
                               QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_history.setIcon(icon_history)

        self.action_sound = QAction(Calculator_1_2)
        self.action_sound.setObjectName(u"action_sound")
        self.action_sound.setShortcut("Ctrl+S")
        icon_sound = QtGui.QIcon()
        icon_sound.addPixmap(QtGui.QPixmap("images/play.png"),
                             QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.action_sound.setIcon(icon_sound)
        btn_sound = self.action_sound
        btn_sound.triggered.connect(self.sound.make_voice)

        Calculator_1_2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Calculator_1_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        Calculator_1_2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Calculator_1_2)
        self.statusbar.setObjectName("statusbar")
        Calculator_1_2.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu.addAction(self.action_sound)
        self.menu_2.addAction(self.action_about)
        self.menu_2.addAction(self.action_history)

        self.retranslateUi(Calculator_1_2)
        QtCore.QMetaObject.connectSlotsByName(Calculator_1_2)

    def retranslateUi(self, Calculator_1_2):
        _translate = QtCore.QCoreApplication.translate
        Calculator_1_2.setWindowTitle(
            _translate("Calculator_1_2", "Calculator V1.2"))
        self.textBrowser.setText('0')
        self.pushButton_C.setText(_translate("Calculator_1_2", "C"))
        self.pushButton_Del.setText(_translate("Calculator_1_2", "←"))
        self.pushButton_Sqrt.setText(_translate("Calculator_1_2", "√"))
        self.pushButton_Div.setText(_translate("Calculator_1_2", "÷"))
        self.pushButton_7.setText(_translate("Calculator_1_2", "7"))
        self.pushButton_8.setText(_translate("Calculator_1_2", "8"))
        self.pushButton_9.setText(_translate("Calculator_1_2", "9"))
        self.pushButton_Times.setText(_translate("Calculator_1_2", "×"))
        self.pushButton_4.setText(_translate("Calculator_1_2", "4"))
        self.pushButton_5.setText(_translate("Calculator_1_2", "5"))
        self.pushButton_6.setText(_translate("Calculator_1_2", "6"))
        self.pushButton_Minus.setText(_translate("Calculator_1_2", "-"))
        self.pushButton_1.setText(_translate("Calculator_1_2", "1"))
        self.pushButton_2.setText(_translate("Calculator_1_2", "2"))
        self.pushButton_3.setText(_translate("Calculator_1_2", "3"))
        self.pushButton_Plus.setText(_translate("Calculator_1_2", "+"))
        self.pushButton_Sign.setText(_translate("Calculator_1_2", "+/-"))
        self.pushButton_0.setText(_translate("Calculator_1_2", "0"))
        self.pushButton_Dot.setText(_translate("Calculator_1_2", "."))
        self.pushButton_Eq.setText(_translate("Calculator_1_2", "="))
        self.pushButton_Cos.setText(_translate("Calculator_1_2", "cos"))
        self.pushButton_lg.setText(_translate("Calculator_1_2", "1/lg"))
        self.pushButton_Sin.setText(_translate("Calculator_1_2", "sin"))
        self.pushButton_Ln.setText(_translate("Calculator_1_2", "ln"))
        self.pushButton_Pow.setText(_translate("Calculator_1_2", "^"))
        self.pushButton_Fac.setText(_translate("Calculator_1_2", "n!"))
        self.pushButton_Pi.setText(_translate("Calculator_1_2", "pi"))
        self.pushButton_LeftPar.setText(_translate("Calculator_1_2", ")"))
        self.pushButton_Abs.setText(_translate("Calculator_1_2", "|x|"))
        self.pushButton_RightPar.setText(_translate("Calculator_1_2", "("))
        self.menu.setTitle(_translate("Calculator_1_2", "计算"))
        self.action_sound.setText(_translate("Calculator_1_2", "朗读当前内容"))
        self.menu_2.setTitle(_translate("Calculator_1_2", "其它"))
        self.action_about.setText(_translate("Calculator_1_2", "关于"))
        self.action_history.setText(_translate("Calculator_1_2", "历史"))

    def press_btn(self):
        button_text = self.sender()
        if self.sound_stat == "Error":
            QMessageBox.about(self, '语音引擎初始化失败', '未找到系统内置英文语音引擎！')
            self.sound_stat = "Ok"
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
            temp_str = self.current
            try:
                i = 0
                if '×' in self.current:
                    self.current = self.current.replace('×', '*')
                if '÷' in self.current:
                    self.current = self.current.replace('÷', "/")
                if 'sin' in self.current:
                    self.current = self.current.replace('sin', 'math.sin')
                if 'cos' in self.current:
                    self.current = self.current.replace('cos', 'math.cos')
                if '^' in self.current:
                    self.current = self.current.replace('^', '**')
                if 'pi' in self.current:
                    self.current = self.current.replace('pi', 'math.pi')
                if 'ln' in self.current:
                    self.current = self.current.replace('ln', 'math.log')
                if '1/lg' in self.current:
                    self.current = self.current.replace('1/lg(', 'math.log(10,')

                while '!' in self.current:
                    i = self.current.find('!')
                    self.current = self.current[:i] + self.current[i + 1:]
                    findPlace = False
                    RightPar_num = 0
                    while findPlace == False and i >= 0:
                        i -= 1
                        if self.current[i] == ')':
                            RightPar_num += 1
                        if self.current[i] == '(' and RightPar_num > 0:
                            RightPar_num -= 1
                            if RightPar_num == 0:
                                findPlace = True
                    if i == 0:
                        self.current = 'math.factorial' + self.current
                    else:
                        self.current = self.current[:
                                                    i] + 'math.factorial' + self.current[
                                                        i:]
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
                # 将计算历史（包括错误）插入第一行
                f = open('files/history.txt', 'r+')
                content = f.read()
                f.seek(0, 0)
                f.write(temp_str + '=' + self.current + '\n' + content)
                f.flush()
                f.close()
            except Exception as e:
                QMessageBox.about(self, '表达式语法错误', '错误信息：' + str(e))

        elif button_text.text() == 'sin' or button_text.text(
        ) == 'cos' or button_text.text() == 'ln' or button_text.text() == '1/lg':
            self.current += button_text.text() + '('
            self.textBrowser.setText(self.current)
        elif button_text.text() == 'n!':
            self.current += '!'
            self.textBrowser.setText(self.current)
        elif button_text.text() == '|x|':
            self.current += 'abs('
            self.textBrowser.setText(self.current)
        else:
            self.current += button_text.text()
            self.textBrowser.setText(self.current)
