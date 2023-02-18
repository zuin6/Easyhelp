import os

import win32gui
from PyQt5.QtWidgets import QApplication
from win32comext.shell import shell, shellcon


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


# 获取句柄标题
def get_hWndtitle(hwnd):
    title = win32gui.GetWindowText(hwnd)
    return title


# 获取所有窗口句柄
def get_all_hWnds():
    hWnd_list = []
    win32gui.EnumWindows(lambda hWnd, param: param.append((hWnd, get_hWndtitle(hWnd))), hWnd_list)
    return hWnd_list


# 获取指定窗口的所有子窗口句柄
def get_son_hWnds(param, findName, type: int):
    list = []
    for hWnd in param:
        if hWnd[1] == findName:
            if type == 0:
                return hWnd
            if type == 1:
                win32gui.EnumChildWindows(hWnd[0], lambda hWnd, param: param.append(hWnd), list)
    return list


# 获取桌面句柄
def get_desktop_hWnd():
    hWnd_list = get_all_hWnds()
    # 窗口没有被拆分直接获取
    hWnds = get_son_hWnds(hWnd_list, "Program Manager", 1)
    for hWnd in hWnds:

        className = win32gui.GetClassName(hWnd)
        if className == "SysListView32" or className == "TXMiniSkin":
            return hWnd
    # 获取拆分后的桌面句柄
    hWnd = win32gui.FindWindowEx(0, 0, "WorkerW", None)
    # 清空数组
    hWnds.clear()
    while len(hWnds) == 0:
        win32gui.EnumChildWindows(hWnd, lambda hWnd, param: param.append(hWnd), hWnds)
        hWnd = win32gui.FindWindowEx(0, hWnd, "WorkerW", None)
    for hWnd in hWnds:
        className = win32gui.GetClassName(hWnd)
        if className == "SysListView32" or className == "TXMiniSkin":
            return hWnd


# 获取helpDesktop窗口
def get_helpDesktop_hWnd():
    for hWnd in get_all_hWnds():
        if hWnd[1] == "DesktopWindow":
            return hWnd[0]


# 将桌面设置为父窗口
def set_Z_IndexOnDesktop():
    pmhWnd = get_desktop_hWnd()
    helpDesktop_hWnd = get_helpDesktop_hWnd()
    # print("桌面句柄")
    # print("16进制", hex(pmhWnd))
    # print("窗口句柄")
    # print("16进制", hex(helpDesktop_hWnd))
    win32gui.SetParent(helpDesktop_hWnd, pmhWnd)


def 移动桌面助手窗口():
    hWnd = win32gui.FindWindowEx(0, 0, "WorkerW", None)
    hWnds = []
    while len(hWnds) == 0:
        win32gui.EnumChildWindows(hWnd, lambda hWnd, param: param.append(hWnd), hWnds)
        hWnd = win32gui.FindWindowEx(0, hWnd, "WorkerW", None)
    for hWnd in hWnds:
        className = win32gui.GetClassName(hWnd)
        if className == "TXMiniSkin":
            win32gui.MoveWindow(hWnd, 50, 50, 1200, 1200, True)


def main():
    # print(get_desktopFilesPath(get_desktopFiles()))
    # get_desktopFiles()
    # files = get_desktopFiles()
    # deskPath = get_desktopPath()
    index = 1

    # for name in files:
    #     path = os.path.join(deskPath, name)
    #     print(path)
    #     index = index + 1
    # print(index)
    # for filepath in filenames:
    # fileInfo = Qt.QFileInfo(os.path.join(dirpath, filepath))
    # print(fileInfo)


main()
