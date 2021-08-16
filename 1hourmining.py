import time
import keyboard
import pyautogui
import random

def miningclicksprem(hours):
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\nada game requirements cuz beach dung\n')
    print("program to start in 2 seconds. Press space to start")


    keyboard.wait("SPACE")



    current_time = time.time()
    #stop_at = current_time + hours* 60 * 60
    stop_at = current_time + hours* 60 * 60

    try:
        while time.time() < stop_at:
            random_mouse_click = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(15.5, 22.5)

            pyautogui.click(interval=random_mouse_click)

            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, guidelay and space: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "\t\t Cycle delay (79,5-81  ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass
 

if __name__ == "__main__":
    miningclicksprem(1)

