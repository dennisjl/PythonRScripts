import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

def osrsautomine():

    #statisk posisjon
    #pyautogui.moveTo(854, 356, 1)
    #pyautogui.click(interval=random_click_delay)
    #time.sleep(3)
    #pyautogui.moveTo(850, 812, 1)
    #pyautogui.click(interval=random_click_delay)
    #time.sleep(3)

    #random square:
    #random north rock:
    pyautogui.moveTo(random.uniform(781, 915), random.uniform(299, 311), 1)
    pyautogui.click(interval=random_click_delay)
    time.sleep(random.uniform(2, 3))
    #southrock
    pyautogui.moveTo(random.uniform(805, 908), random.uniform(863, 898), 1)
    pyautogui.click(interval=random_click_delay)
    time.sleep(random.uniform(2, 3))

    #statisk drop:
    #keyboard.press("SHIFT")
    #pyautogui.moveTo(1460, 767, 1)
    #pyautogui.click(interval=random_click_delay)
    #pyautogui.moveTo(1498, 768, 1)
    #pyautogui.click(interval=random_click_delay)
    #keyboard.release("SHIFT")

    #dynamisk drop:
    keyboard.press("SHIFT")
    pyautogui.moveTo(random.uniform(1450, 1463), random.uniform(759, 767), 0.5)
    pyautogui.click(interval=random_click_delay)
    pyautogui.moveTo(random.uniform(1492, 1504), random.uniform(758, 767), 0.2)
    pyautogui.click(interval=random_click_delay)
    keyboard.release("SHIFT")

def miningclicksprem(hours):

    print("zoom to max, north = up")
    print("osrs mining bot program to start in 2 seconds. Press space to start")


    keyboard.wait("SPACE")



    current_time = time.time()
    stop_at = current_time + hours* 60 * 60

    try:
        while time.time() < stop_at:
            osrsautomine()

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass
 

if __name__ == "__main__":
    #miningclicksprem(1)
    miningclicksprem(3.2)
    #miningclicksprem(0.8)
    #miningclicksprem(0.25)

