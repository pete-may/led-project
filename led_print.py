import sys
from parser import parse_args
from led import LED

# entry point to print messages to sign

def main(argv):
    options = parse_args(argv)
    led = LED(options)
    led.print(options.get('message'))

if __name__ == '__main__':
    main(sys.argv[1:])
