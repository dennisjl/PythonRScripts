from datetime import datetime
import pyautogui
import time
import keyboard
import pyautogui
import random


random_click_delay = random.uniform(0.2, 0.4)


##Portable to north, bank to west:
## x = 906,  y = 66
## x = 1076, y = 102


## Bank to the west position
## x = 1206,  y = 473
## x = 1253,  y = 626

#mousemovementspeed    
random_mouse_movement_speed = random.uniform(0.3, 0.8)
interface_delay = random.uniform(1,1.2)
random_preset_delay = random.uniform(0.2, 0.4)

def move_to_bank():
    random_x_interval = random.uniform(1380, 1400)
    random_y_interval = random.uniform(435, 477)

    pyautogui.moveTo(random_x_interval, random_y_interval, 1)
    
    #pyautogui.doubleClick(interval=random.uniform(0.2, 0.4))
    pyautogui.click(clicks=2, interval=random.uniform(0.2, 0.3))
    time.sleep(random_preset_delay)
    pyautogui.click(clicks=2, interval=random.uniform(0.2, 0.3))
    time.sleep(interface_delay)
    
    keyboard.press("F1")
    time.sleep(random_preset_delay)
    keyboard.release("F1")

def click_pw():

    #CAMWEST=UP

    
    #BANK RIGHT = NORTH
    #WELL LEFT = SOUTH
    #random_x_interval = random.uniform(321, 448)
    #random_y_interval = random.uniform(483, 550)

    #BANK RIGHT = NORTH
    #WELL DIRECTLY UNDER CHAR
    #random_x_interval = random.uniform(931, 996)
    #random_y_interval = random.uniform(505, 560)

    #BANK RIGHT = NORTH
    #WELL UP = TO THE WEST
    random_x_interval = random.uniform(929, 1011)
    random_y_interval = random.uniform(42, 86)

    pyautogui.moveTo(random_x_interval, random_y_interval, 1)
    pyautogui.doubleClick(interval=random.uniform(0.2, 0.4))

    time.sleep(interface_delay)
    
    keyboard.press("SPACE")
    time.sleep(random_preset_delay)
    keyboard.release("SPACE")
    time.sleep(interface_delay)

def con(hours):
    run_for_x_hours = hours * 3600
    print(datetime.now())
    print(time.time())
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave boxtrap on "m", zoom max in\n')
    print("note: funker passe ræv på w84 full, da det er shitton med folk her som fører til inputlag og deadclicks")
    print("MANUAL PLACE CAMERA WITH WEST = UP, ZOOM IN MAX")
    print("BANK TO THE RIGHT/NORTH")
    print("PORTABLE WELL TO LEFT/SOUTH")
    print("program to start in immediately. Press space to start")

    keyboard.wait("SPACE")

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    try:
        while time.time() < stop_at:
            move_to_bank()
            click_pw()
            time.sleep(random.uniform(16.3, 17.1))

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

if __name__ == "__main__":
    con(0.75)    
