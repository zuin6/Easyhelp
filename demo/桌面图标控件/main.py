# -*- coding: utf-8 -*-
from PyQt5 import Qt, QtGui, QtCore
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSizePolicy \
    , QApplication \
    , QWidget \
    , QSizePolicy \
    , QPushButton \
    , QSpacerItem \
    , QGroupBox \
    , QVBoxLayout \
    , QLineEdit
import sys


class FileBox(QWidget):
    def __init__(self, filePath):
        super(FileBox, self).__init__()
        self.fileName = "阿是低价数科点击啊看了"
        self.fileIcon = "fileIcon"
        self.filePath = filePath
        # 获取文件图片和名称
        fileInfo = Qt.QFileInfo(self.filePath)
        fileIcon = Qt.QFileIconProvider()
        self.fileIcon = QtGui.QIcon(fileIcon.icon(fileInfo))
        self.fileName = QtCore.QFileInfo(self.filePath).fileName()
        self.verticalLayout = QVBoxLayout(self)
        # 容器
        box = QGroupBox(self)
        box.setStyleSheet("")
        box.backgroundRole()
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHeightForWidth(box.sizePolicy().hasHeightForWidth())
        box.setSizePolicy(sizePolicy)
        boxQvLayout = QVBoxLayout(box)
        boxQvLayout.setContentsMargins(0, 0, 0, 0)

        # 添加上半部分
        topSection = self.topSectionInit()
        boxQvLayout.addWidget(topSection)
        # 添加下半部分
        bottomInit = self.bottomSectionInit()
        boxQvLayout.addWidget(bottomInit)
        # 设置box比例
        boxQvLayout.setStretch(0, 7)
        boxQvLayout.setStretch(1, 1)
        self.verticalLayout.addWidget(box)
    # 上半部分
    def topSectionInit(self):
        topSection = QGroupBox(self)
        topSection.setStyleSheet("border:none;")
        # topSection.setMaximumHeight(80)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        topSection.setSizePolicy(sizePolicy)
        upQvLayout = QVBoxLayout(topSection)
        # 设置上半部分控件比例
        upQvLayout.setStretch(0, 1)
        upQvLayout.setStretch(1, 8)
        upQvLayout.setStretch(2, 1)
        upQvLayout.setContentsMargins(0, 10, 0, 10)
        # 左弹簧
        # spacerLeft = QSpacerItem(20, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # upQvLayout.addItem(spacerLeft)

        iconButton = QPushButton()
        iconButton.setIconSize(QSize(256,256))
        iconButton.setIcon(self.fileIcon)
        upQvLayout.addWidget(iconButton)
        # 右弹簧
        # spacerRight = QSpacerItem(20, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)
        # upQvLayout.addItem(spacerRight)
        return topSection

    # 下半部分
    def bottomSectionInit(self):
        # 下半部分
        downSection = QGroupBox(self)
        downSection.setStyleSheet("background:pink;border:none;")
        downQvLayout = QVBoxLayout(downSection)
        # 设置下半部分控件比例
        downQvLayout.setStretch(0, 1)
        # 文件名称
        fileEdit = QLineEdit(self.fileName)
        fileEdit.setStyleSheet("border:none;"
                               "color:white;"
                               "font-wight:1000;"
                               "background:rgb(0,0,0,0);"
                               "qproperty-alignment:AlignCenter;"
                               "font-size:12px;")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        downSection.setSizePolicy(sizePolicy)
        downQvLayout.addWidget(fileEdit)
        downQvLayout.setContentsMargins(0, 10, 0, 10)
        return downSection


class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        # 初始化桌面
        layout = QVBoxLayout(self)

        filebox = FileBox("G:\\Desktop\\腾讯QQ.lnk")
        layout.addWidget(filebox)
        filebox.show()
        # for i in range(0, 5):
        #     filebox = FileBox()
        #     layout.addWidget(filebox)


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.resize(700, 800)
    MainWindow.show()

    sys.exit(app.exec_())
