import sys
import os
import getopt
import time

from handlers.emul_handler import EmulHandler
from handlers.rpi_handler import RPIHandler
from pin_consts import *

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

def display(self, scroll):
    offset = []
    for x in range(scroll):
        offset.append("0")
    for row in range(7):
        if row==0:
            self.shiftByte("10001001110" + "".join(offset))
        elif row==1:
            self.shiftByte("10001000100" + "".join(offset))
        elif row==2:
            self.shiftByte("10001000100" + "".join(offset))
        elif row==3:
            self.shiftByte("11111000100" + "".join(offset))
        elif row==4:
            self.shiftByte("10001000100" + "".join(offset))
        elif row==5:
            self.shiftByte("10001000100" + "".join(offset))
        elif row==6:
            self.shiftByte("10001001110" + "".join(offset))
        self.switchRow(row)


def start(self):
    print("Starting")
    try:
        self.clear()
        self.switchRow(ROW_OFF)
        for x in range(90):
            self.wrappedDisplay(x, 0.1)

    except KeyboardInterrupt:
        pass

    self.clear()
    print("done.")

def main(argv):
    global graphic, emulator
    parse_args(argv)

    if(emulator):
        runner = EmulHandler(graphic=graphic)
    else:
        runner = RPIHandler()

    runner.display = display
    runner.start = start
    runner.run()

if __name__ == '__main__':
    main(sys.argv[1:])
