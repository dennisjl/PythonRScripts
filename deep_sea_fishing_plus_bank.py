import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

#start by moving to rightmost spot on deepfish hub

def compass_calibration_north():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)
    time.sleep(1)
    keyboard.press("UP")
    time.sleep(random.uniform(1, 1.5))
    keyboard.release("UP")
    pyautogui.moveTo(1000, 40, 1)
    pyautogui.middleClick()
    pyautogui.scroll(-5000)

def compass_south_calibration():
    pyautogui.moveTo(1540, 40, 0.2)  # placement of the compass on a 1920 x 1080 display
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.2)
    pyautogui.moveTo(1540, 75, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(1)
    keyboard.press("UP")
    time.sleep(random.uniform(1, 1.5))
    keyboard.release("UP")


########################################################################
###SEQUENCE FOR FIRST FISHSPOT

def first_fish_spot():
    #Coordinates for rightmost fishspot
    #952    507
    x = random.uniform(951, 953)
    y = random.uniform(506, 508)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

def spot_1_fish():
    first_fish_spot()
    time.sleep(random.uniform(30, 40))
    first_fish_spot()
    time.sleep(random.uniform(30, 40))
    first_fish_spot()
    time.sleep(random.uniform(30, 40))
    first_fish_spot()
    time.sleep(random.uniform(30, 40))
    first_fish_spot()
    time.sleep(random.uniform(30, 40))
    first_fish_spot()
    time.sleep(random.uniform(30, 40))


def first_bank_spot():
    #Coordinates for bankspot relative fishspot 1
    #920    136
    x = random.uniform(901, 940)
    y = 140
    pyautogui.moveTo(x, y, 1)
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.5)
    go_to_deposit_all_fish = 32*2
    pyautogui.moveTo(x, y + go_to_deposit_all_fish, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

def first_fish_spot_after_bank():
    #coordinates to fishspot 1 from bankspot:
    #991    77
    x = random.uniform(990, 992)
    y = random.uniform(76, 78)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

########################################################################
###SEQUENCE FOR FIRST FISHSPOT

def second_fish_spot():
    #Coordinates for rightmost fishspot
    #947    498
    x = random.uniform(946, 947)
    y = random.uniform(497, 498)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

def spot_2_fish():
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    second_fish_spot()
    time.sleep(random.uniform(30, 40))
    
def second_bank_spot():
    #Coordinates for bankspot relative fishspot 2
    #971    137
    #992    135
    x = random.uniform(981, 992)
    y = 137
    pyautogui.moveTo(x, y, 1)
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.5)
    go_to_deposit_all_fish = 32*2
    pyautogui.moveTo(x, y + go_to_deposit_all_fish, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    
def second_fish_spot_after_bank():
    #coordinates to fishspot 1 from bankspot:
    #1077    99
    x = random.uniform(1075, 1077)
    y = random.uniform(98, 100)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))


def deep_sea_fishing(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("\n go to right/east-most fishing spot, press SPACE to start")
    keyboard.wait("SPACE")

    ###INIT RUN###
    compass_calibration_north()
    spot_1_fish()
    first_bank_spot()
    compass_south_calibration()
    time.sleep(8)

    try:
        while time.time() < stop_at:
            
            random_counter = random.uniform(0, 60)
            print("random 0->60 : " + format((random_counter)))
            
            if(0 <= random_counter < 40):
                first_fish_spot_after_bank()
                time.sleep(15)
                compass_calibration_north()
                spot_1_fish()
                first_bank_spot()
                compass_south_calibration()
                #time.sleep(8)
                time.sleep(5)

            else:
                second_fish_spot_after_bank()
                time.sleep(15)
                compass_calibration_north()
                spot_2_fish()
                second_bank_spot()
                compass_south_calibration()
                time.sleep(6)
            

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass
            

if __name__ == "__main__":
    deep_sea_fishing(4)
    print("process finished naturally")
    
    
    
