from PyQt5.QtCore import QRect, Qt as Qtcore, QPoint
from PyQt5.QtGui import QPainter, QColor, QPixmap, QMouseEvent
from PyQt5.QtWidgets import QWidget, QLabel, QGroupBox, QVBoxLayout


# 代码作者:https://github.com/la-vie-est-belle
# 参考作者：https://www.zhihu.com/people/la-vie-est-belle
class ChooseBox(QWidget):
    def __init__(self, parent=None):
        super(ChooseBox, self).__init__(parent)
        self.setGeometry(0, 0, parent.width(), parent.height())
        # self.setWindowFlags(Qtcore.FramelessWindowHint | Qtcore.Tool)
        self.rect = None

    def paintEvent(self, event):  # 重写事件
        # 初始化绘图工具
        q = QPainter(self)
        # 在窗体绘制
        if self.rect:
            q.fillRect(*self.rect, QColor(80, 106, 207, 30))

    # 鼠标按下
    def mousePressEvent(self, event):
        self.rect = (event.x(), event.y(), 0, 0)
        self.update()

    # 鼠标松开
    def mouseReleaseEvent(self, event):
        self.rect = (0, 0, 0, 0)
        self.update()

    def mouseMoveEvent(self, event):
        start_x, start_y = self.rect[0:2]
        self.rect = (start_x, start_y, event.x() - start_x, event.y() - start_y)
        self.update()
