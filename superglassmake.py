from datetime import datetime
import time
import keyboard
import pyautogui
import random

def superglassmake(hours):
    run_for_x_hours = hours*3600

    print(datetime.now())
    print(time.time())
    #hver glassmake tar 5 sec:
    #3600/5 = 720 ganger i timen
    #1 cycle = 5s
    '''
    cycle = 5
    sec_in_hour = 3600
    hours = hours*sec_in_hour
    number_of_times = hours/cycle
    print(number_of_times)
    '''
    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "timey" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave glassmake set to "y" key via lunar spellbook\n')
    print("program to start in 2 seconds. Press p to start")

    time.sleep(2)
    keyboard.wait("p")

    current_time = time.time()

    try:
        while current_time < current_time + run_for_x_hours:

            random_mouse_click = random.uniform(0.2, 0.4)
            random_bank_open_delay = random.uniform(0.9, 1.2)
            random_f3_click_and_release = random.uniform(0.2, 0.4)
            random_delay_before_y_press = random.uniform(0.5, 0.8)
            random_y_click_and_release = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(3.6 , 4.9)

            pyautogui.click(interval=random_mouse_click)
            time.sleep(random_bank_open_delay)

            keyboard.press("F3")
            time.sleep(random_f3_click_and_release)
            keyboard.release("F3")

            time.sleep(random_delay_before_y_press)

            keyboard.press("Y")
            time.sleep(random_y_click_and_release)
            keyboard.release("Y")

            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, F3 and Y: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "{:.6f}".format(random_bank_open_delay) + "\t"
                  + "{:.6f}".format(random_f3_click_and_release) + "\t"
                  + "{:.6f}".format(random_delay_before_y_press) + "\t"
                  + "{:.6f}".format(random_y_click_and_release) + "\t"
                  + "\t\t Cycle delay (5 ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )


    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass





if __name__ == "__main__":
    superglassmake(1);
