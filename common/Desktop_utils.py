# 根据屏幕大小计算表格列数量
def getTableRowSize(windowWidth):
    iconWidth = 80
    row = windowWidth / iconWidth
    return row


# 根据屏幕大小计算表格行数量
def getTableColSize(windowHeight):
    iconHeight = 90
    col = windowHeight / iconHeight
    return col
