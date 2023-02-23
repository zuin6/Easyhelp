import math
import os

from PyQt5.QtCore import Qt as Qtcore, QRect, pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QPalette, QBrush, QImage, QImageReader
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy, QVBoxLayout, QLabel

import configure
from UI.DesktopWindow import Ui_DesktopWindow
from Component.Filebox import FileBox
from common.Desktop_utils import get_DesktopWallPaperPath
from common.Desktop_utils import get_desktopFiles, get_ScreenAvailableSize, get_desktopFilesPath

# 选中的文件
chooseFiles = configure.DESKTOP_CHOOSE_FILES


class Desktop(QGroupBox, Ui_DesktopWindow):
    # 定义一个信号
    editBoxSignal = pyqtSignal(object)

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        # 设置窗体透明
        self.setWindowFlags(Qtcore.FramelessWindowHint | Qtcore.Tool)  # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setGeometry(get_ScreenAvailableSize())
        self.setStyleSheet("border:none;")
        self.initDesktop()

    # 初始化桌面
    def initDesktop(self):
        self.loadDesktopFiles()
        self.loadBackgroundImage()

    # 桌面背景设置
    def loadBackgroundImage(self):
        pal = QPalette()
        img = QImageReader(get_DesktopWallPaperPath())
        img.setScaledSize(QSize(self.width(), 1080))
        img = img.read()
        pal.setBrush(QPalette.Window, QBrush(img))
        self.setPalette(pal)

    # 加载桌面图标
    def loadDesktopFiles(self):
        # 行、列总数量
        row = 12
        col = 24
        # 桌面布局初始化
        # 获取桌面所有文件名称
        desktopFiles = get_desktopFiles()
        filesPath = get_desktopFilesPath(desktopFiles)
        # 获取桌面所有文件数量
        fileCount = len(desktopFiles)
        # 计算需要几列可以输出桌面所有文件
        needRow = math.ceil(fileCount / row)
        # # 最后一列有几个文件
        lastColFileCount = fileCount % row
        gridLayout = QGridLayout(self)
        gridLayout.setGeometry(QRect(0, 0, 0, 0))
        gridLayout.setHorizontalSpacing(2)
        gridLayout.setVerticalSpacing(8)
        gridLayout.setContentsMargins(2, 6, 2, 14)
        # 定义文件索引
        index = 0
        for X in range(0, col):
            for Y in range(0, row):
                # 位置
                seat = str(Y) + "T" + str(X)
                # 图标容器
                groupBox = QGroupBox()
                groupBox.setStyleSheet("border:none;")
                groupBox.setObjectName(seat)
                sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                groupBox.setSizePolicy(sizePolicy)
                # 添加图标
                if filesPath[index] != 0:
                    groupboxLayout = QVBoxLayout(groupBox)
                    groupboxLayout.setContentsMargins(0, 0, 0, 0)
                    groupboxLayout.setSpacing(0)
                    groupboxLayout.addWidget(FileBox(filesPath[index], seat))
                gridLayout.addWidget(groupBox, Y, X)
                # 文件索引
                index = index + 1

    # 文件盒子选择
    def chooseBox(self):
        for child in self.children():
            if child.objectName() == chooseFiles[0]:
                return child
