import sys
from parser import parse_args
from led import LED

def display(self):
    for row in range(7):
        self.clear()
        self.shiftBit(1)
        self.switchRow(row)

def main(argv):
    options = parse_args(argv)
    led = LED(options)
    led.run(display)

if __name__ == '__main__':
    main(sys.argv[1:])
