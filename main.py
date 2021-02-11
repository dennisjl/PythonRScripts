import keyboard
import time
import random

def auto_aggro(number_of_hours):
    # 3600s i en time. sleep(10) ==> 360 = 1 time
    # endret til sleep(5) * 3 ==> 15s. 3600/15 = 240
    number_of_cycles = number_of_hours*240
    i = 0

    print('\n\n ----pre-reqs: '
          '\n\t\t\t\thave "keyboard" installed via pip ("pip install keyboard")'
          '\n\t\t\t\thave targetcycle set to the "|" key in combat settings '
          '\n\t\t\t\thave chain set to "y" key\n')
    print("program to start in 2 seconds. Press y to start")

    time.sleep(2)
    keyboard.wait("p")      #press p to start

    try:
        while i < number_of_cycles:
            #the random generated numbers:
            d_key_random = random.uniform(0.2, 0.4)
            y_key_random = random.uniform(0.2, 0.4)
            s_key_random = random.uniform(0.2, 0.4)
            t_key_random = random.uniform(0.2, 0.4)
            first_of_three = random.uniform(4.5, 5.5)
            second_of_three = random.uniform(4.5, 5.5)
            third_of_three = random.uniform(4.5, 5.5)

            #Sigil proc
            keyboard.press("d")
            time.sleep(d_key_random)
            keyboard.release("d")

            #corruption shot
            keyboard.press("|")
            keyboard.press("y")
            time.sleep(y_key_random)
            keyboard.release("y")
            keyboard.release("|")

            time.sleep(first_of_three)          # sleep in x time, with unit in seconds

            #chain
            keyboard.press("|")
            keyboard.press("s")
            time.sleep(s_key_random)
            keyboard.release("s")
            keyboard.release("|")

            time.sleep(second_of_three)

            #dbreath
            keyboard.press("|")
            keyboard.press("t")
            time.sleep(t_key_random)
            keyboard.release("t")
            keyboard.release("|")

            time.sleep(third_of_three)

            print("delay generert: \t"
                  + "{:.6f}".format(first_of_three) + "\t\t"
                  + "{:.6f}".format(second_of_three) + "\t\t"
                  + "{:.6f}".format(third_of_three) + "\t\t"
                  + "\t\t\t keystroke generert: \t"
                  + "{:.6f}".format(d_key_random) + "\t\t"
                  + "{:.6f}".format(y_key_random) + "\t\t"
                  + "{:.6f}".format(s_key_random) + "\t\t"
                  + "{:.6f}".format(t_key_random) + "\t\t"
                  )
            i+=1

    except KeyboardInterrupt:
        print("Program exited with CTRL+C")
        pass

    print("process finished after" + number_of_cycles + "times. This ran for" + number_of_hours + "hours")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    auto_aggro(3)


