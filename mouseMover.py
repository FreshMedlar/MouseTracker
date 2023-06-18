import pyautogui
import math, time
import random

while True:
    x, y = pyautogui.position()
    offset_x = random.randint(-50, 50)
    offset_y = random.randint(-50, 50)
    pyautogui.moveTo(x + offset_x, y + offset_y, duration=0.25)


