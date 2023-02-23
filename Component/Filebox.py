# -*- coding: utf-8 -*-
import configure
from PyQt5 import Qt, QtGui, QtCore
from PyQt5.QtCore import QSize, QRect, Qt as Qtcore, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QWidget \
    , QSizePolicy \
    , QPushButton \
    , QGroupBox \
    , QVBoxLayout \
    , QTextEdit, QLabel


# 重置盒子为默认样式
def clearBoxStyle(box):
    box.setStyleSheet("background-color:transparent;")


# 选中文件后添加样式
def chooseBoxStyle(box):
    box.setStyleSheet("#" + box.seatName + "{background-color:rgba(192,192,192,0.3);"
                                           "border:1px solid rgba(255,255,255,0.3);}")


# 文件名修改
def openFileNameEdit(box):
    box.isEdit = True
    textEdit = box.findChild(QTextEdit)
    # 显示编辑框
    textEdit.setHidden(False)
    # 隐藏Qlabel
    label = box.findChild(QLabel)
    label.setHidden(True)


# 关闭修改文本框
def closeFileNameEdit(box):
    textEdit = box.findChild(QTextEdit)
    # 显示编辑框
    textEdit.setHidden(True)
    # 隐藏Qlabel
    label = box.findChild(QLabel)
    label.setHidden(False)
    box.isEdit = False


# 选中的文件
chooseFiles = configure.DESKTOP_CHOOSE_FILES


# 文件盒子
class GroupBoxQ(QGroupBox):

    def __init__(self):
        super(GroupBoxQ, self).__init__()
        self.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        # self.setStyleSheet("background-color:transparent;"
        #                    "border:2px pink solid;")


# 桌面文件
class FileBox(QWidget):
    def __init__(self, filePath, seatName):
        super(FileBox, self).__init__()
        self.fileName = "fileName"
        self.fileIcon = "fileIcon"
        self.filePath = filePath
        self.seatName = seatName
        self.isEdit = False  # 是否编辑

        # 获取文件图片和名称
        fileInfo = Qt.QFileInfo(self.filePath)
        fileIcon = Qt.QFileIconProvider()
        self.fileIcon = QtGui.QIcon(fileIcon.icon(fileInfo))
        self.fileName = QtCore.QFileInfo(self.filePath).fileName()
        self.setObjectName(seatName)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        # 容器
        box = GroupBoxQ()
        box.setObjectName(seatName)
        boxQvLayout = QVBoxLayout(box)
        boxQvLayout.setSpacing(0)
        boxQvLayout.setContentsMargins(2, 2, 2, 2)
        # 添加上半部分
        topSection = self.topSectionInit()
        boxQvLayout.addWidget(topSection)
        # 添加下半部分
        bottomInit = self.bottomSectionInit()
        boxQvLayout.addWidget(bottomInit)

        # 设置box比例
        # boxQvLayout.setStretch(0, 6)
        # boxQvLayout.setStretch(1, 4)
        self.verticalLayout.addWidget(box)
        # 连接桌面信号，处理
        # box.connect(self.editFileName)

    # 鼠标悬浮
    def enterEvent(self, e):
        if self.objectName() not in chooseFiles:
            self.setStyleSheet("#" + self.seatName + "{background-color:rgba(255,255,255,0.1);"
                                                     "border-radius:4px;"
                                                     "border:1px solid rgba(255,255,255,0.3);}")

    # 鼠标离开
    def leaveEvent(self, e):
        if self.objectName() not in chooseFiles:
            clearBoxStyle(self)

    def mousePressEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            # if not self.hasFocus():
            #     self.setFocus()
            #     print(222)
            # else:
            #     print(111)
            #     return
            # 没有选中，直接添加
            if len(chooseFiles) == 0:
                # 添加文件至选择列表
                chooseFiles.append(self.seatName)
                chooseBoxStyle(self)
                return
            # 已选中单击不操作
            if self.objectName() in chooseFiles:
                return
            else:  # 除新选择文件外，去掉所有文件样式
                desktopWindow = self.parent().parent()
                boxs = desktopWindow.findChildren(FileBox)
                for box in boxs:
                    clearBoxStyle(box)
                # 清楚选择列表
                chooseFiles.clear()
                # 添加文件至选择列表
                chooseFiles.append(self.seatName)
                chooseBoxStyle(self)

        elif e.buttons() == QtCore.Qt.RightButton:  # 右键按下
            print("单击鼠标右键")  # 响应测试语句
        elif e.buttons() == QtCore.Qt.MidButton:  # 中键按下
            print("单击鼠标中键")  # 响应测试语句

    def keyPressEvent(self, e):
        if e.key() == Qtcore.Key_F2:  # 判断是否按下了F2键
            box = self.focusWidget()
            if len(chooseFiles) != 0:
                if box.isEdit is False:
                    openFileNameEdit(box)

    def focusOutEvent(self, e):
        box = self.focusWidget()
        closeFileNameEdit(box)

    def editFileName(result=None):
        print(result)

    # 上半部分
    def topSectionInit(self):
        topSection = QGroupBox(self)
        upQvLayout = QVBoxLayout(topSection)
        upQvLayout.setContentsMargins(0, 0, 0, 0)
        iconButton = QPushButton()
        iconButton.setSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        iconButton.setIconSize(QSize(18, 18))
        iconButton.setIcon(self.fileIcon)
        iconButton.setStyleSheet("background-color:transparent;")
        # iconButton.setGeometry(QRect(topSection.size().width()/6, 0, 38, 38))
        upQvLayout.addWidget(iconButton)
        return topSection

    # 下半部分
    def bottomSectionInit(self):
        downSection = QGroupBox(self)
        downQvLayout = QVBoxLayout(downSection)
        downQvLayout.setContentsMargins(0, 0, 0, 0)
        # 文件名称Label
        fileText = QLabel(downSection)
        fileText.setText(self.fileName)
        fileText.setStyleSheet("color:rgb(248,246,231);"
                               "font-wight:1000;"
                               "font-size:12px;"
                               "text-align:center;"
                               # "background:red;"
                               "")
        fileText.setAlignment(Qtcore.AlignCenter)
        size = downSection.size()
        fileText.setGeometry(0, 0, size.width(), size.height())
        # 文件名称编辑框
        fileEdit = QTextEdit(downSection)
        fileEdit.setHidden(True)
        # fileEdit.lineWrapMode(Qt.FixedPixelWidth)
        fileEdit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        fileEdit.setVerticalScrollBarPolicy(Qtcore.ScrollBarAlwaysOff)
        fileEdit.setMarkdown(self.fileName)
        # fileEdit.setStyleSheet(
        #     "background-color:transparent;"
        # )
        return downSection
