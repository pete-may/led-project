import getopt
import sys
import os

usage = 'usage: python '

defaultOptions = {
    "emulator": False,
    "graphic": False,
    "scroll": False,
    "message": ""
}

# parse args from console

def parse_args(argv):
    options = defaultOptions
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
            options['emulator'] = True
            print("emulating")
        if opt == '-g':
            options['graphic'] = True
        if opt == '-s':
            options['scroll'] = True
        if opt == '-m':
            options['message'] = arg
    return options
