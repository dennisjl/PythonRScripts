import keyboard
import time
import random

def auto_aggro(number_of_hours):
    # 3600s i en time. sleep(10) ==> 360 = 1 time
    number_of_cycles = number_of_hours*360
    i = 0

    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave targetcycle set to the "|" key in combat settings '
          '\n\t\t\t\thave chain set to "y" key\n')
    print("program to start in 2 seconds. Press y to start")

    time.sleep(2)
    keyboard.wait("y")      #press enter to start

    try:
        while i<number_of_cycles:
            #generate random numbers
            random_aprox_10_float = random.uniform(9.5, 10.5)
            random_keystroke_float = random.uniform(0.2, 0.4)

            # plus modificator allows to press more buttons at the same time
            #keyboard.press_and_release("u")    #probably too static
            #keyboard.press_and_release("|+y")  #probably too static
            keyboard.press("u")
            time.sleep(random_keystroke_float)
            keyboard.release("u")

            keyboard.press("|")
            keyboard.press("y")
            time.sleep(random_keystroke_float)
            keyboard.release("y")
            keyboard.release("|")

            time.sleep(random_aprox_10_float)  #sleep in x-time, with unit in seconds
            print("delay generert: " + "{:.6f}".format(random_aprox_10_float) +
                  "\t\t\t keystroke generert: " +
                  "{:.6f}".format(random_keystroke_float))
            i+=1
    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

    print("process finished after" + number_of_cycles + "times. This ran for" + number_of_hours + "hours")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auto_aggro(3)


