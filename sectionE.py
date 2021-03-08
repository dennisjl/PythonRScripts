import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

def compass_calibration_north():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)


def surge_on_location(x, y, t , s, a):
    #surge on spot 10:
    pyautogui.moveTo(x, y, t)
    pyautogui.click(interval=random.uniform(0.1, 0.15))
    time.sleep(random.uniform(1, 1.2))
    surge(s,a)

def surge(s,a):
    keyboard.press("A")
    time.sleep(random.uniform(s, a))  # a press and release
    keyboard.release("A")

def sectionEFromNorth():
    # On laptopscreen:

    # 18 climb down wall
    pyautogui.moveTo(random.uniform(933, 978), random.uniform(601, 718), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.7, 3.8))

    # 19: ready to surge
    surge_on_location(random.uniform(990, 1032), random.uniform(676, 710), 0.2, 0.1, 0.2)
    time.sleep(random.uniform(1.6, 1.7))

    # 20 climb new wall:
    pyautogui.moveTo(random.uniform(986, 1029), random.uniform(532, 573), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 7.2))

    # 21 on the herby wall:
    pyautogui.moveTo(random.uniform(1196, 1323), random.uniform(504, 542), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 7.2))

    # 22 still on wall:
    pyautogui.moveTo(random.uniform(1190, 1259), random.uniform(558, 580), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.6, 5.8))

    # 23 last part of the wall plus surge
    pyautogui.moveTo(random.uniform(1190, 1256), random.uniform(547, 570), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 5.2))
    surge(0.1, 0.2)
    time.sleep(random.uniform(2, 2.2))

    # 24: traverse the root
    pyautogui.moveTo(random.uniform(1219, 1280), random.uniform(713, 738), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(9, 9.2))

    # 25:  onto vine from roots
    pyautogui.moveTo(random.uniform(1052, 1057), random.uniform(746, 755), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.6))

    # 27: surger between the vines
    pyautogui.moveTo(random.uniform(1105, 1129), random.uniform(675, 696), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(1, 1.2))
    surge(0.1, 0.2)
    time.sleep(random.uniform(2, 2.2))

    # 28: next vine:
    pyautogui.moveTo(random.uniform(936, 948), random.uniform(705, 759), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.1))

def sectionEFromSouth():
    # 28: first vine:
    pyautogui.moveTo(random.uniform(951, 960), random.uniform(529, 539), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 5.6))
    surge(0.1, 0.2)
    time.sleep(random.uniform(2, 2.2))

    #27: crossed vine2
    pyautogui.moveTo(random.uniform(781, 782), random.uniform(256, 262), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # 25:  onto roots from vine
    pyautogui.moveTo(random.uniform(910, 941), random.uniform(439, 459), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 6.2))

    # 24: onto herby wall:
    pyautogui.moveTo(random.uniform(121, 166), random.uniform(430, 442), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(9, 9.2))

    # 23 herby wall
    pyautogui.moveTo(random.uniform(567, 629), random.uniform(495, 515), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 6.2))

    # 22 herby wall
    pyautogui.moveTo(random.uniform(745, 793), random.uniform(502, 531), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # 21 off the herby wall: //something weird happens here     #TODO: look at this.
    #pyautogui.moveTo(random.uniform(665, 686), random.uniform(547, 561), 0.3)
    pyautogui.moveTo(665, 547, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    #time.sleep(random.uniform(5.2, 5.4))
    time.sleep((random.uniform(6.2, 6.4)))

    # 20 climb the start wall:
    pyautogui.moveTo(random.uniform(605, 647), random.uniform(151, 191), 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))


def run(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("zoom posision: 25 scrolls on g502 \npress space to start")

    keyboard.wait("SPACE")
    compass_calibration_north()

    try:
        while time.time() < stop_at:

            sectionEFromNorth()
            time.sleep(random.uniform(3.2, 3.4))
            sectionEFromSouth()


    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass


if __name__ == "__main__":
    run(3)