import time
import keyboard
import pyautogui
import random

def smith_corrupted_pre(hours):
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave corrupted ore with you\n')
    print("program to start in 2 seconds. Press p to start")

    time.sleep(2)

    keyboard.wait("p")



    current_time = time.time()
    stop_at = current_time + hours* 60 * 60

    try:
        while time.time() < stop_at:
            random_mouse_click = random.uniform(0.2, 0.4)
            random_smithGui_open_delay = random.uniform(0.9, 1.2)
            random_space_press_and_release = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(144, 145)

            pyautogui.click(interval=random_mouse_click)
            time.sleep(random_smithGui_open_delay)

            keyboard.press("SPACE")
            time.sleep(random_space_press_and_release)
            keyboard.release("SPACE")

            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, guidelay and space: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "{:.6f}".format(random_smithGui_open_delay) + "\t"
                  + "{:.6f}".format(random_space_press_and_release) + "\t"
                  + "\t\t Cycle delay (144 ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


if __name__ == "__main__":
    smith_corrupted_pre(4);