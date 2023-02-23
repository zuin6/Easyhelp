# 根据屏幕大小计算表格列数量
import os

import win32api
import win32con
import win32gui
from PyQt5.QtWidgets import QApplication
from win32comext.shell import shell, shellcon

def getTableRowSize(windowWidth):
    iconWidth = 80
    row = windowWidth / iconWidth
    return row


# 根据屏幕大小计算表格行数量
def getTableColSize(windowHeight):
    iconHeight = 90
    col = windowHeight / iconHeight
    return col




# 获取桌面路径
def get_desktopPath():
    return shell.SHGetPathFromIDList(shell.SHGetSpecialFolderLocation(0, shellcon.CSIDL_DESKTOP)).decode('utf-8')


# 获取屏幕可用尺寸
def get_ScreenAvailableSize():
    return QApplication.desktop().availableGeometry()


# 获取桌面所有文件名称
def get_desktopFiles():
    names = os.listdir(get_desktopPath())
    # 如果有桌面配置文件去除
    if "desktop.ini" in names:
        names.remove("desktop.ini")
    return names


# 获取桌面所有文件路径
def get_desktopFilesPath(files):
    # 桌面路径
    path = get_desktopPath()
    pathList = [0 for i in range(24*12)]
    index = 0
    for file in files:
        pathList[index] = os.path.join(path, file)
        index = index + 1
    return pathList

# 获取桌面壁纸路径
def get_DesktopWallPaperPath():
    reg_flags = win32con.WRITE_OWNER | win32con.KEY_WOW64_64KEY | win32con.KEY_ALL_ACCESS
    key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, reg_flags)
    value, key_type = win32api.RegQueryValueEx(key, 'WallPaper')
    # 关闭键
    win32api.RegCloseKey(key)
    return value

# 设置桌面壁纸
def setWallpaper(path):
    # 打开注册表
    reg_key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER, "Control Panel\\Desktop", 0, win32con.KEY_SET_VALUE)

    # 2：拉伸  0：居中  6：适应  10：填充
    win32api.RegSetValueEx(reg_key, "WallpaperStyle", 0, win32con.REG_SZ, "2")

    # SPIF_SENDWININICHANGE:立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)

