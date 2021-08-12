from datetime import datetime
import pyautogui
import time
import keyboard
import pyautogui
import random


random_click_delay = random.uniform(0.2, 0.4)


#Camera angled west == up, bank to east and workbench on tile straight south of bank

## Bank to the right(east) of center position
## x = 1259,  y = 485
## x = 1384,  y = 561

#mousemovementspeed    
random_mouse_movement_speed = random.uniform(0.3, 0.8)
interface_delay = random.uniform(1,1.2)
random_preset_delay = random.uniform(0.2, 0.4)

def move_to_bank():
    random_x_interval = random.uniform(1259, 1384)
    random_y_interval = random.uniform(485, 561)

    pyautogui.moveTo(random_x_interval, random_y_interval, 1)
    
    #pyautogui.doubleClick(interval=random.uniform(0.2, 0.4))
    pyautogui.click(clicks=1, interval=random.uniform(0.2, 0.3))
    time.sleep(random.uniform(0.4, 0.6))
    pyautogui.click(clicks=2, interval=random.uniform(0.2, 0.3))
    time.sleep(interface_delay)
    
    keyboard.press("F1")
    time.sleep(random_preset_delay)
    keyboard.release("F1")

def click_center_pwb():
    random_x_interval = random.uniform(894, 1039)
    random_y_interval = random.uniform(431, 559)

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
    print("program to start in immediately. Press space to start")

    keyboard.wait("SPACE")

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60


    try:
        while time.time() < stop_at:
            move_to_bank()
            click_center_pwb()
            time.sleep(random.uniform(100, 107))

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

if __name__ == "__main__":
    con(2)    
