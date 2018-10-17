import sys
from parser import parse_args
from led import LED

def main(argv):
    options = parse_args(argv)
    led = LED(options)
    led.print(options.get('message'))

if __name__ == '__main__':
    main(sys.argv[1:])
