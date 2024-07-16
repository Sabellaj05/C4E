#!/usr/bin/env python3

import pyautogui
import keyboard
import time

# mover a [x, y] y cuanto tarda en hacerlo
pyautogui.moveTo(100, 400, duration=0.5)
# esperamos 1 seg
time.sleep(1)
# movemos solo en x
pyautogui.moveTo(500, None, duration=0.75)
# clickeamos donde estamos
pyautogui.click()

# podemos escribir

pyautogui.typewrite("me gusta el agua", interval=0.2)
pyautogui.press("enter")
pyautogui.keyDown("shift")
pyautogui.write("uppercase")
pyautogui.keyUp("shift")
pyautogui.press("enter")
pyautogui.write("uppercase")




