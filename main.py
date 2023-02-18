# -*- coding: utf-8 -*-
import win32gui
from PyQt5.QtWidgets import QMainWindow, QApplication, QTextEdit, QVBoxLayout
import sys
from Pages.Desktop import Desktop
from UI.Qdesk import Ui_Qdesk
from common.SysCommon import set_Z_IndexOnDesktop


# 主界面
class MainForm(QMainWindow, Ui_Qdesk):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)
        # 初始化桌面
        self.desktop = Desktop()
        self.desktop.show()



# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    # MainWindow.show()
    set_Z_IndexOnDesktop()

    sys.exit(app.exec_())
