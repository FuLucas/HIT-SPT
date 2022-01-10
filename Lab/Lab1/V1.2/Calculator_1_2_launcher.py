import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog

import Calculator_1_2
import Ui_about
import Ui_history


# 由于历史需从文件更新，每次触发再实例化
def loadHistory():
    child_history = QDialog()
    history_ui = Ui_history.Ui_history()
    history_ui.setupUi(child_history)
    child_history.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 实例化主窗口
    main = QMainWindow()
    main_ui = Calculator_1_2.Calculator_1_2()
    main_ui.setupUi(main)
    # 实例化关于窗口
    child_about = QDialog()
    child_about_ui = Ui_about.Ui_about()
    child_about_ui.setupUi(child_about)

    # 按钮绑定事件
    btn_about = main_ui.action_about
    btn_about.triggered.connect(child_about.show)
    btn_history = main_ui.action_history
    btn_history.triggered.connect(loadHistory)

    # 显示
    main.show()

    sys.exit(app.exec_())
