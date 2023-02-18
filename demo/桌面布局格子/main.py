import sys

from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect, QSize
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QLabel, QGroupBox, QGridLayout, QSizePolicy

from common.SysCommon import get_ScreenAvailableSize


class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 去边框
        # self.setStyleSheet("background:red;")
        gridLayout = QGridLayout(self)
        gridLayout.setGeometry(QRect(0, 0, 0, 0))
        gridLayout.setHorizontalSpacing(5)
        gridLayout.setVerticalSpacing(10)
        gridLayout.setContentsMargins(2, 10, 2, 20)
        gridLayout.setObjectName(u"gridLayout")

        for x in range(0, 24):
            for y in range(0, 12):
                groupBox = QGroupBox()
                groupBox.setObjectName("box" + str(y)+"&"+str(x))
                groupBox.setStyleSheet("background:pink;")
                groupBox.setContentsMargins(0, 0, 0, 0)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                groupBox.setSizePolicy(sizePolicy)
                gridLayout.addWidget(groupBox, y, x)

# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.setGeometry(get_ScreenAvailableSize())
    MainWindow.show()
    sys.exit(app.exec_())
