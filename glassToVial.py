import time
import keyboard
import pyautogui, sys
import random


def auto_vial_maker(number_of_hours):

    #i = 1  ==> tar 50.5s--> 51s
    #i = 10 ==> tar 50.5min --> 52m
    # 1 time med operasjonen = 72 sykler, dvs 72*50 = 3600
    number_of_cycles = number_of_hours*72
    i = 0

    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "time" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave molten glass set to "y" key\n')
    print("program to start in 2 seconds. Press y to start")

    time.sleep(2)
    keyboard.wait("y")

    try:
        while i < number_of_cycles:

            random_mouse_click = random.uniform(0.2, 0.4)
            random_bank_open_delay = random.uniform(0.9, 1.2)
            random_f1_click_and_release = random.uniform(0.2, 0.4)
            random_delay_before_y_press = random.uniform(0.5, 0.8)
            random_y_click_and_release = random.uniform(0.2, 0.4)
            random_delay_before_space_press = random.uniform(0.8, 1.2)
            random_space_click_and_release = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(50.8, 51.3)


            #>>> pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
            pyautogui.click(interval=random_mouse_click)

            time.sleep(random_bank_open_delay)

            keyboard.press("F1")
            time.sleep(random_f1_click_and_release)
            keyboard.release("F1")

            time.sleep(random_delay_before_y_press)

            keyboard.press("Y")
            time.sleep(random_y_click_and_release)
            keyboard.release("Y")

            time.sleep(random_delay_before_space_press)

            keyboard.press("Space")
            time.sleep(random_space_click_and_release)
            keyboard.release("Space")

            #vent i ish 50s, 50.5-->51s
            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, f1 and y: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "{:.6f}".format(random_bank_open_delay) + "\t"
                  + "{:.6f}".format(random_f1_click_and_release) + "\t"
                  + "{:.6f}".format(random_delay_before_y_press) + "\t"
                  + "{:.6f}".format(random_y_click_and_release) + "\t"
                  + "{:.6f}".format(random_delay_before_space_press) + "\t"
                  + "{:.6f}".format(random_space_click_and_release) + "\t"
                  + "\t\t Cycle delay (50 ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

def improved_vial_maker(hours):
    run_for_x_hours = hours*3600

    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard", "pyautogui", "random" and "time" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave molten glass set to "y" key\n')
    print("program to start in 2 seconds. Press y to start")

    time.sleep(2)
    keyboard.wait("y")

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    try:
        while time.time() < stop_at:
            random_mouse_click = random.uniform(0.2, 0.4)
            random_bank_open_delay = random.uniform(0.9, 1.2)
            random_f1_click_and_release = random.uniform(0.2, 0.4)
            random_delay_before_y_press = random.uniform(0.5, 0.8)
            random_y_click_and_release = random.uniform(0.2, 0.4)
            random_delay_before_space_press = random.uniform(0.8, 1.2)
            random_space_click_and_release = random.uniform(0.2, 0.4)

            random_cycle_delay = random.uniform(50.8, 51.3)

            # >>> pyautogui.click(x=moveToX, y=moveToY, clicks=num_of_clicks, interval=secs_between_clicks, button='left')
            pyautogui.click(interval=random_mouse_click)

            time.sleep(random_bank_open_delay)

            keyboard.press("F1")
            time.sleep(random_f1_click_and_release)
            keyboard.release("F1")

            time.sleep(random_delay_before_y_press)

            keyboard.press("Y")
            time.sleep(random_y_click_and_release)
            keyboard.release("Y")

            time.sleep(random_delay_before_space_press)

            keyboard.press("Space")
            time.sleep(random_space_click_and_release)
            keyboard.release("Space")

            # vent i ish 50s, 50.5-->51s
            time.sleep(random_cycle_delay)

            print("delay generert, mouseclick, f1 and y: \t"
                  + "{:.6f}".format(random_mouse_click) + "\t"
                  + "{:.6f}".format(random_bank_open_delay) + "\t"
                  + "{:.6f}".format(random_f1_click_and_release) + "\t"
                  + "{:.6f}".format(random_delay_before_y_press) + "\t"
                  + "{:.6f}".format(random_y_click_and_release) + "\t"
                  + "{:.6f}".format(random_delay_before_space_press) + "\t"
                  + "{:.6f}".format(random_space_click_and_release) + "\t"
                  + "\t\t Cycle delay (50 ish sec): \t"
                  + "{:.6f}".format(random_cycle_delay)
                  )

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #auto_vial_maker(5)
    improved_vial_maker(5)
