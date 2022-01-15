import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

#start by moving to fishspot 3 and 4, aka the eastmost spot
#that access two spots from one square

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

########################################################################
###SEQUENCE FOR FIRST FISHSPOT, spot 3, directly west for character

def first_fish_spot():
    #Coordinates for west spot
    #920->928    525->532
    x = random.uniform(920, 928)
    y = random.uniform(525, 532)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random_click_delay)


########################################################################
###SEQUENCE FOR FIRST FISHSPOT, spot 4, directly south for character

def second_fish_spot():
    #Coordinates for south spot
    #955->960    552->560
    x = random.uniform(955, 960)
    y = random.uniform(552, 560)
    
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(interval=random_click_delay)


def gwd3_fishing(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("\n go to right/east-most fishing spot, press SPACE to start")
    keyboard.wait("SPACE")

    ###INIT RUN###
    compass_calibration_north()

    try:
        while time.time() < stop_at:
            
            random_counter = random.uniform(0, 60)
            fish_duration = random.uniform(20, 110)
            ##Based on measured datapoitns 
            #2:01 --> 120s      1:22 --> 82s        8s
            #49s                1:25 --> 85s        1:30 --> 90s
            #34s                24s                 1:41 --> 101s
            #19s                1:31 --> 91s        
            
            print("random 0->60 : " + format((random_counter)) + "\t" + "fish duration: " + format((fish_duration)))
            
            
            if(0 <= random_counter < 40):
                first_fish_spot()
                time.sleep(fish_duration)

            else:
                second_fish_spot()
                time.sleep(fish_duration)
                
            

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass
            

if __name__ == "__main__":
    gwd3_fishing(4)
    print(time.time())
    print("process finished naturally")
    
    
    
