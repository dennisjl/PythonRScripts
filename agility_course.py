import time
import keyboard
import pyautogui
import random

random_click_delay = random.uniform(0.2, 0.4)

def anachronia(hours):
    current_time = time.time()
    stop_at = current_time + hours * 60 * 60

    print("press space to start")

    keyboard.wait("SPACE")

    compass_calibration()
    try:
        while time.time() < stop_at:

            section1()
            section2()
            section3()




            keyboard.press("ENTER")
            time.sleep(60)


    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

def section3():
    #herbywallsection:

    # 21 on the herby wall:
    pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.9, 6.1))

    # 22 still on wall:
    # pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.moveTo(1137, 563, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.9, 6.1))

    # 23 last part of the wall
    # pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.moveTo(1137, 563, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.6, 3.8))
    surge(0.1, 0.2)
    time.sleep(random.uniform(2, 2.2))

    # 24
    # pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.moveTo(1176, 678, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # 25:   #juster litt her, ulik basert på skjerm
    # pyautogui.moveTo(939, 787, 0.3)
    pyautogui.moveTo(1176, 678, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(8.5)

    # 26: kan ignoreres pga laptopskjerm
    #pyautogui.moveTo(1086, 637, 0.2)
    #pyautogui.click(interval=random.uniform(0.2, 0.4))
    #time.sleep(7)

    # 27: surger between the vines
    # pyautogui.moveTo(1175, 705, 0.2)
    pyautogui.moveTo(1105, 678, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(2)
    surge(0.1, 0.2)
    time.sleep(1.5)

    # 28:
    pyautogui.moveTo(951, 779, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(1.5)
    # 29: kan ignoreres pga skjerm
    # pyautogui.moveTo(951, 800, 0.2)
    # pyautogui.click(interval=random.uniform(0.2, 0.4))
    # time.sleep(6)

    # 30: bladed surge:
    bds()
    time.sleep(0.5)

def section1():
    #On laptopscreen:
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

    #next section start:
    # spot 7: moveto wall,
    pyautogui.moveTo(1768, 165, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4, 4.2))

    # 7,5 up on wall
    # pyautogui.moveTo(1168, 290, 0.4)
    pyautogui.moveTo(1057, 398, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.2, 8.3))

    # spot 8, on the wall
    pyautogui.moveTo(982, 350, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 5.2))

    # spot 9, still on wall, going down
    # pyautogui.moveTo(982, 350, 0.5)
    pyautogui.moveTo(958, 464, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.6, 5.8))

    # spot 10: the surge
    surge_on_location(1050, 488, 0.5, 0.2, 0.3)
    time.sleep(2)

def section2():
    # spot 11:
    # pyautogui.moveTo(1508, 570, 0.3)
    # pyautogui.moveTo(1344, 496, 0.3)
    pyautogui.moveTo(1761, 181, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 5.7))

    # spot12
    pyautogui.moveTo(1008, 464, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4.8, 5))

    # spot 13, på veggen igjen:
    # pyautogui.moveTo(1366, 641, 0.3)
    pyautogui.moveTo(1199, 623, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 7))

    # spot14. roots,
    # pyautogui.moveTo(1374, 807, 0.3)
    pyautogui.moveTo(1245, 726, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(2, 2.5))
    surge(0.2, 0.3)
    time.sleep(1.8)

    #surgedown straight
    pyautogui.moveTo(1731, 235, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(5)
    surge(0.1, 0.2)
    time.sleep(2.8)

    # spot 15, enter dinospine
    # 1087, 554          1338, 538
    # 1087, 664          1338, 664
    pyautogui.moveTo(random.uniform(1087, 1338), random.uniform(554, 664), 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # spot 16, climb on spine
    pyautogui.moveTo(1272, 520, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # spot 17, climb off dino:
    pyautogui.moveTo(1375, 694, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.6, 6.7))

    # 18 climb down wall
    pyautogui.moveTo(975, 800, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4.3, 4.5))

    # 19: ready to surge
    surge_on_location(1062, 736, 0.2, 0.1, 0.2)
    time.sleep(random.uniform(1.5, 1.6))

    # 20 climb new wall:
    pyautogui.moveTo(1030, 600, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 7.2))

def part31To40():
    compass_south_calibration()

    # 31: vine traverse
    pyautogui.moveTo(945, 385, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.5, 6.7))

    # 32:
    pyautogui.moveTo(291, 142, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.5, 6.7))

    # 33: bd til 224, 425
    bladed_dive(224, 425, 0.3)
    time.sleep(random.uniform(1, 1.2))

    # 34 click på root og så surge
    pyautogui.moveTo(797, 527, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(2)
    surge(0.1, 0.2)
    time.sleep(random.uniform(1.9, 2.1))

    # 35:
    pyautogui.moveTo(1686, 125, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6.1, 6.2))

    # 36: crossing the water
    pyautogui.moveTo(958, 112, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(5.5)
    surge(0.1, 0.2)
    time.sleep(2)

    # 37: mapsclick in ruins
    pyautogui.moveTo(1722, 125, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(7)

    # 38: click on brick
    pyautogui.moveTo(1099, 436, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(3.5)

    # 39: bladed dive over til vine:
    bladed_dive(1743, 150, 0.3)
    time.sleep(random.uniform(2.1, 2.2))

    # 40 click on vine then surge
    pyautogui.moveTo(927, 287, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.5, 3.7))
    surge(0.1, 0.2)
    time.sleep(random.uniform(1.4, 1.5))

def part21To30():

    #21 on the herby wall:
    pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.6, 5.8))

    #22 still on wall:
    pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.6, 5.8))

    # 23 last part of the wall
    pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.6, 5.8))
    surge(0.1, 0.2)
    time.sleep(random.uniform(1, 1.2))

    # 24
    pyautogui.moveTo(1402, 497, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8.5, 8.7))

    # 25:   #juster litt her, ulik basert på skjerm
    pyautogui.moveTo(939, 787, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(2)
    # 26:
    pyautogui.moveTo(1086, 637, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(7)
    # 27: surger between the vines
    pyautogui.moveTo(1175, 705, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(2)
    surge(0.1, 0.2)
    time.sleep(1.5)
    # 28:
    pyautogui.moveTo(951, 779, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(1.5)
    # 29:
    pyautogui.moveTo(951, 800, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(6)

    # 30: bladed surge:
    bds()
    time.sleep(0.5)


def part11To20():
    # spot 11:
    #pyautogui.moveTo(1508, 570, 0.3)
    #pyautogui.moveTo(1344, 496, 0.3)
    pyautogui.moveTo(1515, 562, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(2, 2.1))
    surge(0.2, 0.3)
    time.sleep(random.uniform(3, 3.1))

    # spot12
    pyautogui.moveTo(1008, 464, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4, 5))

    #spot 13, på veggen igjen:
    pyautogui.moveTo(1366, 641, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 7))

    #spot14. roots,
    pyautogui.moveTo(1374, 807, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(2, 2.5))
    surge(0.2, 0.3)
    time.sleep(1)

    # spot 15, enter dinospine
    pyautogui.moveTo(1734, 295, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(11, 11.3))
    pyautogui.moveTo(1186, 441, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # spot 16, climb on spine
    pyautogui.moveTo(1272, 520, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(8, 8.2))

    # spot 17, climb off dino:
    pyautogui.moveTo(1375, 694, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 7.2))

    # 18 climb down wall
    pyautogui.moveTo(975, 800, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(6, 6.2))

    # 19: ready to surge
    surge_on_location(1062, 736, 0.2, 0.1, 0.2)
    time.sleep(random.uniform(1.2, 1.4))

    # 20 climb new wall:
    pyautogui.moveTo(1030, 618, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 7.2))


def partOneToTen():
    # spot1:
    pyautogui.moveTo(959, 530, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.8, 4))

    # spot2:
    #pyautogui.moveTo(800, 500, 0.2)
    #1920/1080 on laptopscreen:
    pyautogui.moveTo(783, 448, 0.3)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5, 6))

    # spot3:
    pyautogui.moveTo(909, 285, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

    # spot4:
    pyautogui.moveTo(1284, 389, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

    # spot 5, about to enter hole
    pyautogui.moveTo(948, 284, 1)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.5, 6.5))

    # spot6: over roots
    pyautogui.moveTo(1360, 588, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

    # spot 7: moveto wall,
    pyautogui.moveTo(1768, 165, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(3.5, 4))
    # 7,5 up on wall
    pyautogui.moveTo(1168, 290, 0.4)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(7, 8))

    # spot 8, on the wall
    pyautogui.moveTo(982, 350, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(4, 5))

    # spot 9, still on wall
    pyautogui.moveTo(982, 350, 0.5)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    time.sleep(random.uniform(5.8, 6))

    #########first part done and working.
    # spot 10
    ##surge_on_location(1063, 407, 0.5, 0.2, 0.3)
    ##time.sleep(random.uniform(0.2, 0.3))
    # spot 10
    #surge_on_location(1063, 407, 0.5, 0.2, 0.3)
    surge_on_location(1050, 488, 0.5, 0.2, 0.3)
    time.sleep(2)

#todo:noe er fakka her
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

def bladed_dive(x,y,t):
    keyboard.press_and_release("c")
    time.sleep(1)
    pyautogui.moveTo(x,y,t)
    pyautogui.click()

def bds():
    #sequence for triangle bladed dive surge
    keyboard.press_and_release("c")
    time.sleep(1)
    pyautogui.moveTo(1681, 230, 0.1)
    pyautogui.click()

    time.sleep(random.uniform(2, 2.1))

    pyautogui.moveTo(1043, 623, 0.1)
    pyautogui.click()
    time.sleep(0.5)
    keyboard.press_and_release("A")

def compass_calibration():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.click(interval=random_click_delay)

def compass_south_calibration():
    pyautogui.moveTo(1540, 40, 1)  # placement of the compass on a 1920 x 1080 display
    pyautogui.rightClick(interval=random_click_delay)
    time.sleep(0.5)
    pyautogui.moveTo(1540, 75, 0.2)
    pyautogui.click(interval=random.uniform(0.2, 0.4))
    keyboard.press("UP")
    time.sleep(1)
    keyboard.release("UP")

if __name__ == "__main__":
    anachronia(1)