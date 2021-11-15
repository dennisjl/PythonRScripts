from datetime import datetime
import pyautogui
import time
import keyboard
import pyautogui
import random

#Zoom on overworld doesnt matter anymore
#rs3 Minimap needs to be max zoomed out tho
#Todo: add aprox 0.5s to the sleep on "move to start" to make it a bit more inefficient

random_click_delay = random.uniform(0.2, 0.4)
random_m_click_and_release = random.uniform(0.2, 0.4)

def compass_calibration_north_up():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)
    time.sleep(1)
    keyboard.press("UP")
    time.sleep(random.uniform(1, 1.5))
    keyboard.release("UP")

#første sekvens:
#m-wait 3,5/4
# move mouse to x = 1410    y=531
#               x = 1432    y=548

def trap_then_move():
    random_m_click_and_release = random.uniform(0.2, 0.4)
    random_ish3s_wait = random.uniform(3.5, 4)
    keyboard.press("m")
    time.sleep(random_m_click_and_release)
    keyboard.release("m")
    time.sleep(random_ish3s_wait)


#Move to start will move mouse to minimap instead, and then click posision on minimap
#Coordinates of starts on minimap:
#x: 1741    y:184       NB! Needs to be static
def move_to_start():
    random_x_interval = random.uniform(1741, 1742)
    random_y_interval = 184
    random_mouse_movement_speed = random.uniform(0.3, 0.8)
    
    pyautogui.moveTo(random_x_interval, random_y_interval, random_mouse_movement_speed)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1.8, 2.2))

def move_to_char():
    center_x_interval = random.uniform(950, 970)
    center_y_interval = random.uniform(526, 538)
    random_mouse_movement_speed = random.uniform(0.2, 0.5)

    pyautogui.moveTo(center_x_interval, center_y_interval, random_mouse_movement_speed)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1.5, 2))

def lootpress():
    keyboard.press(",")
    time.sleep(random_m_click_and_release)
    keyboard.release(",")
    keyboard.press("SPACE")
    time.sleep(random_m_click_and_release)
    keyboard.release("SPACE")


#Improved version doesnt need lootpress
def repeat_sequence():
    move_to_char()
    
    trap_then_move()
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.3))
    #lootpress()

    trap_then_move()
    time.sleep(random.uniform(1, 1.5))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.4))
    #lootpress()

    trap_then_move()
    time.sleep(random.uniform(1, 1.5))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.2))
    #lootpress()

    trap_then_move()
    time.sleep(random.uniform(1, 1.5))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.5))
    #lootpress()

    trap_then_move()
    time.sleep(random.uniform(1, 1.3))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.5))
    #lootpress()

    trap_then_move()
    


def init_trap():
    trap_then_move()
    trap_then_move()
    trap_then_move()
    trap_then_move()
    trap_then_move()
    trap_then_move()
    move_to_start()

def boxtrap(hours):
    run_for_x_hours = hours * 3600
    print(datetime.now())
    print(time.time())
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave boxtrap on "m", zoom 19/26 scrolls from max zoomin\n')
    print("program to start in immediately. Press space to start")

    keyboard.wait("SPACE")

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    compass_calibration_north_up()
    init_trap()
    try:
        while time.time() < stop_at:
            repeat_sequence()
            move_to_start()

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

if __name__ == "__main__":
    #boxtrap(1)
    boxtrap(4)
