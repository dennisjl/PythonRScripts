import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

def compass_calibration_north():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)

def compass_south_calibration():
    pyautogui.moveTo(1540, 40, 0.2)  # placement of the compass on a 1920 x 1080 display
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.2)
    pyautogui.moveTo(1540, 75, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))

def sectionGNorth():
    # On laptopscreen:
    # spot1:
    pyautogui.moveTo(959, 530, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.8, 4))

    # spot2:
    # pyautogui.moveTo(800, 500, 0.2)
    # 1920/1080 on laptopscreen:
    pyautogui.moveTo(866, 484, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 5.2))

    # spot3:
    pyautogui.moveTo(909, 285, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # spot4:
    # pyautogui.moveTo(1284, 389, 0.5)
    pyautogui.moveTo(1201, 428, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # spot 5, about to enter hole
    # pyautogui.moveTo(948, 284, 1)
    pyautogui.moveTo(961, 335, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 6.5))

    # spot6: over roots, finishing section G
    # pyautogui.moveTo(1360, 588, 0.4)
    pyautogui.moveTo(1243, 562, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

def sectionGSouth():
    #6 traverse roots:
    #828.514    889,514
    #828,562    889,562
    pyautogui.moveTo(random.uniform(828, 889), random.uniform(514, 562), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

    # 5 enter hole
    # 776, 459   830, 453
    # 783, 545   830, 545
    pyautogui.moveTo(random.uniform(783, 830), random.uniform(459, 545), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 6.5))

    # 4
    # 925, 783   982, 783
    # 925, 807   982, 807
    pyautogui.moveTo(random.uniform(925, 982), random.uniform(783, 807), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 6.2))

    # 3
    # 522, 712
    #            530, 805
    pyautogui.moveTo(random.uniform(522, 530), random.uniform(712, 805), 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    compass_south_calibration()

    # spot2:
    # 890, 189   958, 295
    pyautogui.moveTo(random.uniform(890, 958), random.uniform(189, 295), 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.5, 6.7))

    # spot1:
    # 821, 369       902, 481
    pyautogui.moveTo(random.uniform(821, 902), random.uniform(369, 481), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.8, 4))


def run(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("press space to start")

    keyboard.wait("SPACE")

    try:
        while time.time() < stop_at:
            compass_calibration_north()
            sectionGNorth()
            sectionGSouth()

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


if __name__ == "__main__":
    run(1)