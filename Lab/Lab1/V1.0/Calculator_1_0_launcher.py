import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import Calculator_1_0

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Calculator_1_0.Calculator_1_0()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
