import sys
import os
import getopt
import time

from handlers.emul_handler import EmulHandler
from handlers.rpi_handler import RPIHandler
from pin_consts import *
from alpha_consts import *

emulator = False
graphic = False
scroll = False
message = None

# usage = 'usage: python ' + os.path.basename(__file__) + ' <file_with_data>'

def parse_args(argv):
    global emulator, graphic, scroll, message
    try:
        opts, args = getopt.getopt(argv, "hegsm:", ["help", "emulator", "graphic" "scroll", "message="])
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
        if opt == '-g':
            graphic = True
        if opt == '-s':
            scroll = True
        if opt == '-m':
            message = arg

def main(argv):
    # global graphic, emulator, scroll
    parse_args(argv)

    if(emulator):
        runner = EmulHandler(graphic=graphic)
    else:
        runner = RPIHandler()

    # runner.display = display
    # runner.start = start
    # runner.run()
    # print(scroll)
    # print(argv[1])
    # print(message)
    runner.print(message, scroll)

if __name__ == '__main__':
    main(sys.argv[1:])
