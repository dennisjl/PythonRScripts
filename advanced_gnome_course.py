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

def compass_north_calibration():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)

def advanced_gnome_course(hours):
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
            pyautogui.moveTo(240, 549, 0.3)
            pyautogui.click(interval=random.uniform(0.2, 0.4))
            time.sleep(random.uniform(3.5, 3.7))
            compass_south_calibration()

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

def agility():
    # spot1: log balance
    pyautogui.moveTo(random.uniform(946, 963), random.uniform(515,527), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 5.2))

    # spot 2: obstacle net
    pyautogui.moveTo(random.uniform(956, 1031), random.uniform(337, 399), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.5, 3.7))

    # spot 3: climb branch
    pyautogui.moveTo(random.uniform(954, 970), random.uniform(419, 430), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(2.5, 2.7))

    # spot 4: another climb
    pyautogui.moveTo(random.uniform(1032, 1039), random.uniform(450, 454), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.5, 3.7))

    # spot 5: signpost
    pyautogui.moveTo(random.uniform(573, 627), random.uniform(372, 444), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.5, 3.7))

    # spot 6: pole
    compass_north_calibration()
    pyautogui.moveTo(random.uniform(997, 1029), random.uniform(261, 263), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(9.5, 9.7))

    # spot 7: downthe hole
    pyautogui.moveTo(random.uniform(940, 975), random.uniform(460, 482), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.5, 6.7))


if __name__ == "__main__":
    advanced_gnome_course(2.5)