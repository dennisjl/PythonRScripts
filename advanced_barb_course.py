import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

def compass_south_calibration():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.5)
    pyautogui.moveTo(1540, 75, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

def advanced_barbarian_course(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("press space to start")

    keyboard.wait("SPACE")

    #juster zoom til å være 20 hakk fra min
    #compass_south_calibration()

    try:
        while time.time() < stop_at:
            agility()
            #move to start
            pyautogui.moveTo(390, 584, 0.3)
            pyautogui.click(interval=random.uniform(0.2, 0.4))
            time.sleep(random.uniform(3.5, 3.7))

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

def agility():
    # spot1: Ropes
    pyautogui.moveTo(random.uniform(958, 966), 465, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4.4, 4.6))

    # spot2: Log-balance
    pyautogui.moveTo(random.uniform(1060, 1086), random.uniform(442, 451), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # spot3: Walljump
    pyautogui.moveTo(random.uniform(1124, 1151), random.uniform(295, 339), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # spot4: climb wall
    pyautogui.moveTo(random.uniform(1055, 1060), random.uniform(517, 593), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 5.2))

    # spot5: fire spring device
    pyautogui.moveTo(random.uniform(1144, 1168), random.uniform(531, 546), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 5.7))

    # spot6: balance beam
    pyautogui.moveTo(random.uniform(800, 846), random.uniform(559, 563), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.2, 3.3))

    # spot7: jump
    pyautogui.moveTo(random.uniform(824, 867), random.uniform(559, 585), 0.1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(2.5, 2.7))

    # spot8: slide roof
    pyautogui.moveTo(random.uniform(800, 837), random.uniform(554, 595), 0.1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4, 4.2))

if __name__ == "__main__":
    advanced_barbarian_course(2.5)