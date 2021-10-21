from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con, win32gui, win32ui
from win32api import GetSystemMetrics


a = 0

dc = win32gui.GetDC(0)
dcObj = win32ui.CreateDCFromHandle(dc)
hwnd = win32gui.WindowFromPoint((0,0))
monitor = (0, 0, GetSystemMetrics(0), GetSystemMetrics(1))

while 1:
    try:
        if pyautogui.locateOnScreen('umbrella.png', confidence=0.8) != None:
            semsiyelocation = pyautogui.locateOnScreen('umbrella.png', confidence=0.8)
            x, y = pyautogui.center(semsiyelocation)
            print("Görebiliyorum")
            print(x)
            print(y)
            dcObj.Rectangle((x-70, y-30, x+100, y+110))
            sleep(3)
            win32gui.InvalidateRect(hwnd, monitor, True) # Refresh the entire monitor
            sleep(1)
            a = 1
        else:
                print("Göremiyorum")
                time.sleep(1)
        if a == 12:
            print("Kareyi çizdim")
            time.sleep(3)
            b = 1
    except TypeError:
        print(TypeError)
        pass