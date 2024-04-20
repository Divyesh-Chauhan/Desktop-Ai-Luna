import pyautogui

from time import sleep

def volumeup():
    for i in range(5):
        pyautogui.press("up")
        sleep(0.1)

def volumedown():
    for i in range(5):
        pyautogui.press("down")
        sleep(0.1)

