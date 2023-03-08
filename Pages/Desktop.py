from PyQt5 import QtCore
from PyQt5.QtCore import Qt as Qtcore, QRect, QSize, QTimer, Qt
from PyQt5.QtGui import QPixmap, QImageReader, QPainter, QPen, QColor, QCursor
from PyQt5.QtWidgets import QGroupBox, QGridLayout, QSizePolicy, QVBoxLayout, QLabel, QApplication, QAction, qApp, QMenu
import configure
from Component.ChooseBox import ChooseBox
from UI.DesktopWindow import Ui_DesktopWindow
from Component.FileBox import FileBox
from common.Desktop_utils import get_DesktopWallPaperPath
from common.Desktop_utils import get_desktopFilesPath

# 选中的文件
chooseFiles = configure.DESKTOP_CHOOSE_FILES


class Desktop(QGroupBox, Ui_DesktopWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        # 当前背景图片
        self.currentBackImgPath = get_DesktopWallPaperPath()
        # 背景索引
        self.imgIndex = 0
        # 宽、高
        self.windowSize = QApplication.desktop()
        # 隐藏桌面
        self.hideWindow = False
        # 是否双击桌面
        self.doubleClick = False
        # 设置窗体透明
        self.setWindowFlags(Qtcore.FramelessWindowHint | Qtcore.Tool)  # 去边框
        # self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        self.setGeometry(0, 0, self.windowSize.width(), self.windowSize.height())
        self.windowBox = QGroupBox(self)
        self.windowBox.setGeometry(0, 0, self.windowSize.width(), self.windowSize.height())
        self.setStyleSheet("border:none;")
        self.initDesktop()
        self.rect = None
        self.setContextMenuPolicy(Qt.CustomContextMenu)

        # 初始化桌面
    def initDesktop(self):
        self.loadDesktopFiles()
        self.loadBackgroundImage()
        # ChooseBox(self)

    # 桌面背景设置
    def loadBackgroundImage(self):
        # 图片读取
        img = QImageReader(self.currentBackImgPath)
        # 设置缩放
        img.setScaledSize(QSize(1920, 1080))
        img = img.read()
        # 背景
        currentLabel = QLabel(self)
        currentLabel.setGeometry(0, 0, self.windowSize.width(), self.windowSize.height())
        currentLabel.setPixmap(QPixmap(img))
        currentLabel.lower()
        # 注册表监听
        imgTimer = QTimer(self)
        imgTimer.timeout.connect(lambda: self.listenImagePath(currentLabel))
        imgTimer.start(500)

    # 背景检测定时器
    def listenImagePath(self, currentLabel):
        path = get_DesktopWallPaperPath()
        if self.currentBackImgPath != path:
            self.changeBackgroundImage(currentLabel, path)

    # 同步系统背景
    def changeBackgroundImage(self, label, path):
        img = QImageReader(path)
        img.setScaledSize(QSize(1920, 1080))
        img = img.read()
        label.setPixmap(QPixmap(img))
        self.currentBackImgPath = path

    # 加载桌面图标
    def loadDesktopFiles(self):
        # 行、列总数量
        row = 12
        col = 24
        # 桌面布局初始化
        # 获取桌面所有文件名称
        desktopFiles = configure.DESKTOP_FILES
        filesPath = get_desktopFilesPath(desktopFiles)
        gridLayout = QGridLayout(self.windowBox)
        gridLayout.setGeometry(QRect(0, 0, 0, 0))
        gridLayout.setHorizontalSpacing(4)
        gridLayout.setVerticalSpacing(8)
        gridLayout.setContentsMargins(2, 6, 2, 50)
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

    # 鼠标单击按下
    def mousePressEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            self.rect = (e.x(), e.y(), 0, 0)
        elif e.buttons() == QtCore.Qt.RightButton:  # 右键按下
            print("单击鼠标右键")  # 响应测试语句
            menu = QMenu(self)
            menu.addAction(u"查看(V)")
            menu.addAction(u"排序方式(O)")
            menu.addAction(u"刷新(E)")
            menu.addSeparator()
            menu.addAction(u"粘贴")
            menu.addAction(u"粘贴快捷方式")
            menu.addAction(u"撤销")
            menu.addAction(u"新建")
            menu.addSeparator()
            menu.addAction(u"NVIDIA 控制面板")
            menu.addSeparator()
            menu.addAction(u"新建")
            menu.addSeparator()
            menu.addAction(u"显示设置")
            menu.addAction(u"个性化")
            # 右键弹出
            menu.popup(QCursor.pos())
        elif e.buttons() == QtCore.Qt.MidButton:  # 中键按下
            print("单击鼠标中键")  # 响应测试语句


    # 双击松开
    def mouseDoubleClickEvent(self, e):
        if e.buttons() == QtCore.Qt.LeftButton:
            if not self.hideWindow:
                self.hideWindow = True
                self.windowBox.setHidden(self.hideWindow)
            else:
                self.hideWindow = False
                self.windowBox.setHidden(self.hideWindow)

