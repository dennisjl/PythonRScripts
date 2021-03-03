from datetime import datetime
import time
import keyboard
import pyautogui
import random

#todo: adjust a bit randomness in location of initial sandstone at start of while loop

def fine_sand(hours):

    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("press P to start")

    time.sleep(1)
    keyboard.wait("p")

    random_click_delay = random.uniform(0.2, 0.4)

    #calibrate compass
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)
    time.sleep(1)
    keyboard.press("UP")
    time.sleep(random.uniform(1, 1.5))
    keyboard.release("UP")
    pyautogui.moveTo(1000, 40, 1)
    pyautogui.middleClick()
    pyautogui.scroll(5000)


    try:
        while time.time() < stop_at:
            #starts the sequence by moving to a mining location:
            """
            init sandstone in quarry
            x = 669	y = 024				x = 981	    y = 024
            x = 669	y = 228				x = 981 	y = 218
            
            menaphos:
            x = 807	y = 029				x = 1153	y = 029
            x = 807	y = 208				x = 1153 	y = 198
            
            """
            """either quarry or mena
            quarry_x_coordinate = random.uniform(670, 980)
            quarry_y_coordinate = random.uniform(25, 218)
            print("x: " + format(int(round(quarry_x_coordinate))) + "\ty: " + format(int(round(quarry_y_coordinate))))
            pyautogui.moveTo(quarry_x_coordinate, quarry_y_coordinate, 0.5) #targets sandstone
            """

            """
            menaphos:
            x = 807	y = 029				x = 1153	y = 029
            x = 807	y = 208				x = 1153 	y = 198
            """
            mena_x = random.uniform(807, 1153)
            mena_y = random.uniform(29, 198)
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

            #slot 2, with randomness
            if(0 <= random_counter < 10):
                """
                Slot 2, with randomness, the coordinates
                x = 1211	y = 850				x = 1240	y = 848
                x = 1210	y = 874				x = 1238	y = 874
                """
                random_x_coordinate = random.uniform(1210, 1230)
                random_y_coordinate = random.uniform(850, 875)
                rightclick_delay = random.uniform(0.2, 0.4)
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate, 1)
                pyautogui.rightClick(interval=rightclick_delay)
                time.sleep(0.5)
                go_to_grind = 35
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate+go_to_grind, 0.2)
                pyautogui.click(interval=random.uniform(0.2, 0.4))


            elif(10 <= random_counter < 20):
                """
                slot 10/28
                x = 1251	y = 889				x = 1280	y = 890
                x = 1252	y = 911				x = 1279 	y = 911
                """
                random_x_coordinate = random.uniform(1252, 1280)
                random_y_coordinate = random.uniform(889, 911)
                rightclick_delay = random.uniform(0.2, 0.4)
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate, 1)
                pyautogui.rightClick(interval=rightclick_delay)
                time.sleep(0.5)
                go_to_grind = 35
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate + go_to_grind, 0.2)
                pyautogui.click(interval=random.uniform(0.2, 0.4))

            elif (20 <= random_counter < 30):
                """
                slot 13/28
                x = 1371	y = 888				x = 1397	y = 888 
                x = 1371	y = 908				x = 1397 	y = 908
                """
                random_x_coordinate = random.uniform(1371, 1397)
                random_y_coordinate = random.uniform(888, 908)
                rightclick_delay = random.uniform(0.2, 0.4)
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate, 1)
                pyautogui.rightClick(interval=rightclick_delay)
                time.sleep(0.5)
                go_to_grind = 35
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate + go_to_grind, 0.2)
                pyautogui.click(interval=random.uniform(0.2, 0.4))

            elif (30 <= random_counter < 50):
                """
                slot 7/28
                x = 1413	y = 855				x = 1437	y = 855 
                x = 1413	y = 874				x = 1437 	y = 874
                """
                random_x_coordinate = random.uniform(1413, 1437)
                random_y_coordinate = random.uniform(855, 874)
                rightclick_delay = random.uniform(0.2, 0.4)
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate, 1)
                pyautogui.rightClick(interval=rightclick_delay)
                time.sleep(0.5)
                go_to_grind = 35
                pyautogui.moveTo(random_x_coordinate, random_y_coordinate + go_to_grind, 0.2)
                pyautogui.click(interval=random.uniform(0.2, 0.4))

            elif (50 <= random_counter <= 60):
                #Denne er for slot16
                ##flytt mus til inventory og start grindsekvens
                #pyautogui.moveTo(1250, 900, 1) #begge to treffer
                pyautogui.moveTo(1250, 950, 1)
                rightclick_delay = random.uniform(0.2 ,0.4)
                pyautogui.rightClick(interval=rightclick_delay)
                time.sleep(0.5)
                pyautogui.moveTo(1250, 965, 0.2)
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
