# -*- coding: utf-8 -*-
from PyQt5.QtCore import QMetaObject, QCoreApplication


class Ui_DesktopWindow(object):
    def setupUi(self, DesktopWindow):
        if not DesktopWindow.objectName():
            DesktopWindow.setObjectName(u"DesktopWindow")
        DesktopWindow.resize(400, 300)

        self.retranslateUi(DesktopWindow)

        QMetaObject.connectSlotsByName(DesktopWindow)
    # setupUi

    def retranslateUi(self, DesktopWindow):
        DesktopWindow.setWindowTitle(QCoreApplication.translate("DesktopWindow", u"DesktopWindow", None))
    # retranslateUi

