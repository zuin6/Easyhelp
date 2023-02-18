import math
import os

from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy, QVBoxLayout, QLabel
from UI.DesktopWindow import Ui_DesktopWindow
from Component.Filebox import FileBox
from common.SysCommon import get_desktopFiles, get_ScreenAvailableSize, get_desktopFilesPath


class Desktop(QGroupBox, Ui_DesktopWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        # 设置窗体透明
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setGeometry(get_ScreenAvailableSize())
        self.setStyleSheet("border:none;")
        # 行、列总数量
        row = col = 12
        # 桌面布局初始化
        # 表格组件

        # 获取桌面所有文件名称
        desktopFiles = get_desktopFiles()
        filesPath = get_desktopFilesPath(desktopFiles)
        # 获取桌面所有文件数量
        fileCount = len(desktopFiles)
        # 计算需要几列可以输出桌面所有文件
        needRow = math.ceil(fileCount / col)
        # # 最后一列有几个文件
        lastColFileCount = fileCount % col
        print(fileCount)

        gridLayout = QGridLayout(self)
        gridLayout.setGeometry(QRect(0, 0, 0, 0))
        gridLayout.setHorizontalSpacing(2)
        gridLayout.setVerticalSpacing(10)
        gridLayout.setContentsMargins(2, 5, 2, 20)
        gridLayout.setObjectName(u"gridLayout")
        # 定义文件索引
        index = 0
        for X in range(0, 24):
            for Y in range(0, 12):
                # 图标容器
                groupBox = QGroupBox()
                groupBox.setObjectName("box" + str(Y) + "&" + str(X))

                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                groupBox.setSizePolicy(sizePolicy)
                # 添加图标
                if filesPath[index] != 0:
                    groupboxLayout = QVBoxLayout(groupBox)
                    groupBox.setStyleSheet("border:none;background:pink;")
                    groupboxLayout.setContentsMargins(0, 0, 0, 0)
                    groupboxLayout.setSpacing(0)
                    groupboxLayout.addWidget(FileBox(filesPath[index]))
                gridLayout.addWidget(groupBox, Y, X)
                # 文件索引
                index = index + 1