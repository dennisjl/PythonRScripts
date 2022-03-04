from datetime import datetime
from compass_methods import compass_calibration_north
import time
import keyboard
import pyautogui
import random

#todo: adjust a bit randomness in location of initial sandstone at start of while loop

def fine_sand(hours):

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("press space to start")

    keyboard.wait("SPACE")

    #calibrate compass
    compass_calibration_north()


    try:
        while time.time() < stop_at:
            #starts the sequence by moving to a mining location:

            #Stand to the east of the rock:
            #mining-coordinates:
            #900,525 ---915, 535
            
            mena_x = random.uniform(900, 915)
            mena_y = random.uniform(525, 535)
            print("x: " + format(int(round(mena_x))) + "\ty: " + format(int(round(mena_y))))
            pyautogui.moveTo(mena_x, mena_y, 0.5)  # targets sandstone

            local_random_click_delay_1 = random.uniform(0.2, 0.4)
            local_random_click_delay_2 = random.uniform(0.2, 0.4)
            local_random_click_delay_3 = random.uniform(0.2, 0.4)
            local_random_click_delay_4 = random.uniform(0.2, 0.4)

            #aprox 1 minute to fill up inventory, should click once in 15ish seconds
            first_ish_15_click = random.uniform(14, 15)
            second_ish_15_click = random.uniform(14, 15)
            third_ish_15_click = random.uniform(14, 15)
            fourth_ish_15_click = random.uniform(14, 15)

            ##mining sequence starts here
            pyautogui.click(interval=local_random_click_delay_1)
            time.sleep(first_ish_15_click)

            pyautogui.click(interval=local_random_click_delay_2)
            time.sleep(second_ish_15_click)

            pyautogui.click(interval=local_random_click_delay_3)
            time.sleep(third_ish_15_click)

            pyautogui.click(interval=local_random_click_delay_4)
            time.sleep(fourth_ish_15_click)

            random_counter = random.uniform(0, 60)
            print("random 0->60 : " + format((random_counter)))

            

            #grind sequence
            #1110,1130-980,985
            
            random_x_coordinate = random.uniform(1110, 1130)
            random_y_coordinate = random.uniform(980, 985)
            rightclick_delay = random.uniform(0.2, 0.4)
            pyautogui.moveTo(random_x_coordinate, random_y_coordinate, 1)
            pyautogui.rightClick(interval=rightclick_delay)
            time.sleep(0.5)
            pyautogui.click(interval=random.uniform(0.2, 0.4))


            #GUI-delay
            time.sleep(random.uniform(0.8, 1.2))
            keyboard.press("SPACE")
            time.sleep(random.uniform(0.4, 0.8))
            keyboard.release("SPACE")

            time.sleep(31)



    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


if __name__ == "__main__":
    fine_sand(1)
