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

usage = 'usage: python ' + os.path.basename(__file__) + ' <file_with_data>'

def parse_args(argv):
    global emulator, graphic
    try:
        opts, args = getopt.getopt(argv, "heg", ["help", "emulator", "graphic"])
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

def main(argv):
    global graphic, emulator
    parse_args(argv)

    if(emulator):
        runner = EmulHandler(graphic=graphic)
    else:
        runner = RPIHandler()

    # runner.display = display
    # runner.start = start
    # runner.run()
    print(argv[1])
    runner.print(argv[1])

if __name__ == '__main__':
    main(sys.argv[1:])
