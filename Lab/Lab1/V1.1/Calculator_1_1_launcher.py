import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import Calculator_1_1

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Calculator_1_1.Calculator_1_1()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
