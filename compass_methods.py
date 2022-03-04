import keyboard
import pyautogui
import random
import time

random_click_delay = random.uniform(0.2, 0.4)

def compass_calibration_north():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)
    time.sleep(1)
    keyboard.press("UP")
    time.sleep(random.uniform(1, 1.5))
    keyboard.release("UP")
    pyautogui.moveTo(1000, 40, 1)
    pyautogui.middleClick()
    pyautogui.scroll(-5000)
