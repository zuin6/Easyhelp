# -*- coding: utf-8 -*-
import os

import configure
from PyQt5 import Qt, QtGui, QtCore
from PyQt5.QtCore import QSize, QRect, Qt as Qtcore, pyqtSlot, pyqtSignal, QRegExp
from PyQt5.QtWidgets import QWidget \
    , QSizePolicy \
    , QPushButton \
    , QGroupBox \
    , QVBoxLayout \
    , QPlainTextEdit, QLabel, QPlainTextEdit, QApplication

# 重置盒子为默认样式
from common.Desktop_utils import fileReName, get_desktopFiles


def clearChooseBox(boxWidget):
    boxWidget.setStyleSheet("background-color:transparent;")
    # 是否编辑状态
    if boxWidget.isEdit:
        closeFileNameEdit(boxWidget)


# 设置焦点
def addFocus(widget):
    if widget.hasFocus():
        return
    else:
        widget.setFocus()


# 选中文件后添加样式
def chooseBoxStyle(boxWidget):
    boxWidget.setStyleSheet("#" + boxWidget.seatName + "{background-color:rgba(0,0,200,0.2);"
                                                       "border:1px solid rgba(255,255,255,0.3);}")


# 文件名修改
def openFileNameEdit(boxWidget):
    boxWidget.isEdit = True
    textEdit = boxWidget.findChild(QPlainTextEdit)
    # 显示编辑框
    textEdit.setHidden(False)
    textEdit.textCursor()

    # 隐藏Qlabel
    label = boxWidget.findChild(QLabel)
    label.setHidden(True)


# 关闭修改文本框
def closeFileNameEdit(boxWidget):
    if boxWidget.inherits("FileBox"):
        if boxWidget.isEdit:
            textEdit = boxWidget.findChild(QPlainTextEdit)
            # 显示编辑框
            textEdit.setHidden(True)
            # 隐藏Qlabel
            label = boxWidget.findChild(QLabel)
            label.setHidden(False)
            boxWidget.isEdit = False
            # 改名
            name = textEdit.toPlainText()
            newFilePath = fileReName(boxWidget.filePath, name)
            configure.DESKTOP_FILES = get_desktopFiles()
            # 更新FileBox的数据
            if os.path.exists(newFilePath):
                # 获取文件图片和名称
                fileInfo = Qt.QFileInfo(newFilePath)
                fileIcon = Qt.QFileIconProvider()
                boxWidget.filePath = newFilePath
                boxWidget.fileIcon = QtGui.QIcon(fileIcon.icon(fileInfo))
                boxWidget.fileName = QtCore.QFileInfo(newFilePath).fileName()
                label.setText(name)
                icon = boxWidget.findChild(QPushButton)
                icon.setIcon(boxWidget.fileIcon)
                return
            textEdit.setPlainText(newFilePath)


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
        self.fileName = "Name"
        self.fileIcon = "Icon"
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
        # 连接文本修改控件
        textEdit = box.findChild(QPlainTextEdit, None)
        # textEdit.textChanged.connect(lambda: self.fileNameChange(QPlainTextEdit, 20))

    # 文件名修改
    def fileNameChange(self, textEdit, max_length):
        pass

    # 鼠标悬浮
    def enterEvent(self, e):
        if self.objectName() not in chooseFiles:
            self.setStyleSheet("#" + self.seatName + "{background-color:rgba(0,0,200,0.1);"
                                                     "border:1px solid rgba(255,255,255,0.3);}")

    # 鼠标离开
    def leaveEvent(self, e):
        if self.objectName() not in chooseFiles:
            clearChooseBox(self)

    def mousePressEvent(self, e):
        # 左键按下
        if e.buttons() == QtCore.Qt.LeftButton:
            # 设置焦点
            addFocus(self)
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
                boxWidgets = desktopWindow.findChildren(FileBox)
                for widget in boxWidgets:
                    clearChooseBox(widget)
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
        # 判断是否按下了F2键
        if e.key() == Qtcore.Key_F2:
            # 当前焦点控件
            currentWidget = self.focusWidget()
            # 有选中文件并且焦点控件是FileBox
            if len(chooseFiles) != 0:
                if currentWidget.isEdit is False:
                    openFileNameEdit(currentWidget)
        # 判断是否按下了回车键
        if e.key() == Qtcore.Key_Return:
            print(e)

    # 盒子失去焦点事件
    def focusOutEvent(self, e):
        boxWidget = self.focusWidget()
        closeFileNameEdit(boxWidget)

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
        fileEdit = QPlainTextEdit(downSection)
        fileEdit.setHidden(True)
        # fileEdit.lineWrapMode(Qt.FixedPixelWidth)
        fileEdit.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        fileEdit.setVerticalScrollBarPolicy(Qtcore.ScrollBarAlwaysOff)
        fileEdit.setPlainText(self.fileName)
        return downSection
