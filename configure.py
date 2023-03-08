# -*- coding: utf-8 -*-
from common.Desktop_utils import get_desktopFiles


class desktopVal:
    # 选择的文件
    global DESKTOP_CHOOSE_FILES
    # 桌面所有文件名称
    global DESKTOP_FILES
    DESKTOP_FILES = get_desktopFiles()
    DESKTOP_CHOOSE_FILES = []


# def SET_DESKTOP_CHOOSE_FILES(key, value):
#     DESKTOP_CHOOSE_FILES[key] = value


# def GET_DESKTOP_CHOOSE_FILES(key=None, defValue=None):
#     if key is not None:
#         try:
#             return DESKTOP_CHOOSE_FILES[key]
#         except KeyError:
#             return defValue
#     else:
#         return DESKTOP_CHOOSE_FILES
