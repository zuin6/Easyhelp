# -*- coding: utf-8 -*-
from PyQt5.QtWidgets import QApplication \
    , QWidget \
    , QVBoxLayout \
    , QTableWidget \
    , QTableWidgetItem
import sys


class MainForm(QWidget):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        # 初始化桌面
        layout = QVBoxLayout(self)
        table = QTableWidget()
        # 列的总数量
        row = 12
        # 行的总数量
        col = 12
        # 设置行和列数量
        table.setRowCount(row)
        table.setColumnCount(col)
        for i in range(0, col):
            for j in range(0, row):
                table.setItem(i, j, QTableWidgetItem("Test"))
        layout.addWidget(table)


# 主程序
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = MainForm()
    MainWindow.resize(800, 800)
    MainWindow.show()

    sys.exit(app.exec_())
