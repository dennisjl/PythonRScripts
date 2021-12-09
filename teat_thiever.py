import time
import keyboard
import pyautogui
import random

def thieve(hours):
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave corrupted ore with you\n')
    print("program to start in 2 seconds. Press SPACE to start")

    keyboard.wait("SPACE")

    current_time = time.time()
    stop_at = current_time + hours* 60 * 60

    try:
        while time.time() < stop_at:
            
            random_mouse_click = random.uniform(0.2, 0.4)
            random_space_press_and_release = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(4, 4.1)

            pyautogui.click(interval=random_mouse_click)
            
            pyautogui.keyDown("G")
            pyautogui.keyDown("H")

            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, guidelay and space: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "\t\t Cycle delay (144 ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


if __name__ == "__main__":
    thieve(1);
