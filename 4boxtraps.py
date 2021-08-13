from datetime import datetime
import pyautogui
import time
import keyboard
import pyautogui
import random

#Defaultzoom = 12 zoomsm, bekreftet 12. aug
#Defaultzoom asuspc = 8 zooms, bekreftet natt 13/morgen 14.

random_click_delay = random.uniform(0.2, 0.4)

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

random_m_click_and_release = random.uniform(0.2, 0.4)

def trap_then_move():
    #random_m_click_and_release = random.uniform(0.2, 0.4)
    #random_ish3s_wait = random.uniform(5, 5.5)
    random_ish3s_wait = random.uniform(4, 4.5)
    keyboard.press("m")
    time.sleep(random_m_click_and_release)
    keyboard.release("m")
    time.sleep(random_ish3s_wait)

def move_to_start():
    #random_x_interval = random.uniform(1410, 1432)
    ##random_x_interval = 1417
    random_x_interval = random.uniform(1416, 1417)
    #random_y_interval = random.uniform(531, 548)
    ##random_y_interval = 540
    random_y_interval = random.uniform(540, 541)
    random_mouse_movement_speed = random.uniform(0.3, 0.8)

    pyautogui.moveTo(random_x_interval, random_y_interval, random_mouse_movement_speed)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4.8, 5.5))

def move_to_char():
    center_x_interval = random.uniform(950, 970)
    center_y_interval = random.uniform(526, 538)
    random_mouse_movement_speed = random.uniform(0.2, 0.5)

    pyautogui.moveTo(center_x_interval, center_y_interval, random_mouse_movement_speed)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3, 4))

def lootpress():
    keyboard.press(",")
    time.sleep(random_m_click_and_release)
    keyboard.release(",")
    keyboard.press("SPACE")
    time.sleep(random_m_click_and_release)
    keyboard.release("SPACE")

def repeat_sequence():

    trap_then_move()
    time.sleep(random.uniform(1, 1.5))
    move_to_char()
    #time.sleep(random.uniform(1, 1.5))
    lootpress()

    trap_then_move()
    time.sleep(random.uniform(1.5, 2))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.5))
    lootpress()

    trap_then_move()
    time.sleep(random.uniform(1.5, 2))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.5))
    lootpress()

    trap_then_move()
    time.sleep(random.uniform(1.5, 2))
    lootpress()

##
    time.sleep(random.uniform(1.5, 2))


def init_trap():
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
    boxtrap(12)
