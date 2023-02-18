import sys

from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel


class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        layout = QVBoxLayout(self)
        layout.addWidget(QLabel("这是一个空白窗口"))


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.resize(800, 800)
    # MainWindow.show()

    sys.exit(app.exec_())
