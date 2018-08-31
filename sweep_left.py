import sys
import os
import getopt
import time

from led_setup import Setup

emulator = False

PIN_A = 12 # BLUE
PIN_B = 11 # WHITE
PIN_C = 13 # PURPLE

PIN_DATA  = 16	# GREEN
PIN_CLOCK = 18	# ORANGE
PIN_CLEAR = 15	# YELLOW


usage = 'usage: python ' + os.path.basename(__file__) + ' <file_with_data>'

def parse_args(argv):
    global emulator
    try:
        opts, args = getopt.getopt(argv, "he", ["help", "emulator"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        if opt == '-e':
            emulator = True
            print("emulating")

def switchRow(setPin, row):
    # print("switch to row")
    # print(row)
    setPin(PIN_A, 1)
    setPin(PIN_B, 1)
    setPin(PIN_C, 1)

    if row == 0:
        setPin(PIN_A, 0)
        setPin(PIN_B, 0)
        setPin(PIN_C, 0)
    elif row == 1:
        setPin(PIN_A, 0)
        setPin(PIN_B, 0)
        setPin(PIN_C, 1)
    elif row == 2:
        setPin(PIN_A, 0)
        setPin(PIN_B, 1)
        setPin(PIN_C, 0)
    elif row == 3:
        setPin(PIN_A, 0)
        setPin(PIN_B, 1)
        setPin(PIN_C, 1)
    elif row == 4:
        setPin(PIN_A, 1)
        setPin(PIN_B, 0)
        setPin(PIN_C, 0)
    elif row == 5:
        setPin(PIN_A, 1)
        setPin(PIN_B, 0)
        setPin(PIN_C, 1)
    elif row == 6:
        setPin(PIN_A, 1)
        setPin(PIN_B, 1)
        setPin(PIN_C, 0)
    elif row == 7:
        setPin(PIN_A, 1)
        setPin(PIN_b, 1)
        setPin(PIN_c, 1)
    time.sleep(0.001)
    setPin(PIN_A, 1)
    setPin(PIN_B, 1)
    setPin(PIN_C, 1)

def main(argv):
    parse_args(argv)

    setup = Setup(emulator)
    setPin = setup.getFunc()

    setPin(PIN_CLEAR, 1)
    try:
        for x in range(0,90):
            timeout = time.time() + 0.1
            # print(x)
            while True:
                if time.time() > timeout:
                    break
                for row in range(7):
                    setPin(PIN_CLEAR, 0)
                    setPin(PIN_CLEAR, 1)

                    setPin(PIN_DATA, 1)
                    setPin(PIN_CLOCK, 1)
                    setPin(PIN_CLOCK, 0)
                    for y in range(x):
                        setPin(PIN_DATA, 0)
                        setPin(PIN_CLOCK, 1)
                        setPin(PIN_CLOCK, 0)
                    switchRow(setPin, row)

    except KeyboardInterrupt:
        pass

    setPin(PIN_CLEAR, 0)
    print("done.")

if __name__ == '__main__':
    main(sys.argv[1:])
