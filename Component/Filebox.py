# -*- coding: utf-8 -*-
from PyQt5 import Qt, QtGui, QtCore
from PyQt5.QtCore import QSize, QRect,Qt as Qtcore
from PyQt5.QtWidgets import QWidget \
    , QSizePolicy \
    , QPushButton \
    , QGroupBox \
    , QVBoxLayout \
    , QTextEdit

sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
sizePolicy.setHorizontalStretch(0)
sizePolicy.setVerticalStretch(0)


class FileBox(QWidget):
    def __init__(self, filePath):
        super(FileBox, self).__init__()
        self.fileName = "fileName"
        self.fileIcon = "fileIcon"
        self.filePath = filePath

        # 获取文件图片和名称
        fileInfo = Qt.QFileInfo(self.filePath)
        fileIcon = Qt.QFileIconProvider()
        self.fileIcon = QtGui.QIcon(fileIcon.icon(fileInfo))
        self.fileName = QtCore.QFileInfo(self.filePath).fileName()

        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        # 容器
        box = QGroupBox(self)
        # box.setStyleSheet("border:none;")
        box.setSizePolicy(sizePolicy)
        boxQvLayout = QVBoxLayout(box)
        boxQvLayout.setSpacing(0)
        boxQvLayout.setContentsMargins(0, 0, 0, 0)
        # 设置box比例
        boxQvLayout.setStretch(0, 7)
        boxQvLayout.setStretch(1, 1)
        # 添加上半部分
        topSection = self.topSectionInit()
        boxQvLayout.addWidget(topSection)
        # 添加下半部分
        bottomInit = self.bottomSectionInit()
        boxQvLayout.addWidget(bottomInit)

        # # 设置box比例
        boxQvLayout.setStretch(0, 6)
        boxQvLayout.setStretch(1, 4)
        self.verticalLayout.addWidget(box)

    # 上半部分
    def topSectionInit(self):
        topSection = QGroupBox(self)
        topSection.setStyleSheet("border:none;")
        topSection.setSizePolicy(sizePolicy)
        upQvLayout = QVBoxLayout(topSection)
        upQvLayout.setContentsMargins(0, 0, 0, 0)
        iconButton = QPushButton()
        iconButton.setSizePolicy(sizePolicy)
        iconButton.setIconSize(QSize(18,18))
        iconButton.setIcon(self.fileIcon)
        upQvLayout.addWidget(iconButton)
        return topSection

    # 下半部分
    def bottomSectionInit(self):
        downSection = QGroupBox(self)
        downSection.setSizePolicy(sizePolicy)
        downQvLayout = QVBoxLayout(downSection)
        # downQvLayout.setContentsMargins(0, 0, 0, 0)
        # 文件名称
        fileEdit = QTextEdit(downSection)
        fileEdit.setSizePolicy(sizePolicy)
        fileEdit.setVerticalScrollBarPolicy(Qtcore.ScrollBarAlwaysOff)
        fileEdit.setLineWrapMode(QTextEdit.FixedColumnWidth)
        fileEdit.setLineWrapColumnOrWidth(6)
        fileEdit.setMarkdown(self.fileName)
        fileEdit.setStyleSheet("border:none;"
                               "color:white;"
                               "font-wight:1000;"
                               "text-shadow: -1px 20px 0 #000, 1px 1px 0 #000,1px -1px 0 #000,-1px -1px 0 #000;"
                               "background:rgb(0,0,0,0);"
                               # "qproperty-alignment:AlignCenter;"
                               "font-size:12px;")
        return downSection
