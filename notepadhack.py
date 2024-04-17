import pyautogui
import time

pyautogui.hotkey("winleft","r")
pyautogui.write("notepad")
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("you are hacked")
pyautogui.hotkey("ctrl","s")
pyautogui.press("enter")


