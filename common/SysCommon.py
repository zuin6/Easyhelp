import os

import win32gui
from PyQt5.QtWidgets import QApplication
from win32comext.shell import shell, shellcon


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
    a = None
    while len(hWnds) == 0:
        win32gui.EnumChildWindows(hWnd, lambda hWnd, param: param.append(hWnd), hWnds)
        hWnd = win32gui.FindWindowEx(0, hWnd, "WorkerW", None)
    for hWnd in hWnds:
        className = win32gui.GetClassName(hWnd)
        if className == "TXMiniSkin":
        # if className == "_cls_desk_":
            win32gui.MoveWindow(hWnd, 100, 100, 1200, 1200, True)
            a = hWnd
    while True:
        win32gui.MoveWindow(a,400,400,1200,1200,True)

def main():
    移动桌面助手窗口()


# main()
