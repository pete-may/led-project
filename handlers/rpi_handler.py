from handlers.base_handler import BaseHandler
from pin_consts import *

import time

# RPIHandler governs communication to the raspberry pi and renders
# patterns on led sign; inherits functions from BaseHandler

class RPIHandler(BaseHandler):
    def __init__(self, options):
        self.options = options

        import RPi.GPIO as GPIO
        self.GPIO = GPIO

        # raspbery pi library setup

        self.GPIO.setmode(GPIO.BOARD)

        self.GPIO.setup(PIN_A, self.GPIO.OUT)
        self.GPIO.setup(PIN_B, self.GPIO.OUT)
        self.GPIO.setup(PIN_C, self.GPIO.OUT)

        self.GPIO.setup(PIN_DATA,  self.GPIO.OUT)
        self.GPIO.setup(PIN_CLEAR, self.GPIO.OUT)
        self.GPIO.setup(PIN_CLOCK, self.GPIO.OUT)
    
    # switchRow selects a row to turn on by multiplexing three inputs A, B, and C
    # e.g. to turn on row 0, A=0 B=0 C=0, to turn on row 1 A=0 B=0 C=1, etc.
    # 7 rows total

    def switchRow(self, row):
        if row == 0:
            self.GPIO.output(PIN_A, 0)
            self.GPIO.output(PIN_B, 0)
            self.GPIO.output(PIN_C, 0)
        elif row == 1:
            self.GPIO.output(PIN_A, 0)
            self.GPIO.output(PIN_B, 0)
            self.GPIO.output(PIN_C, 1)
        elif row == 2:
            self.GPIO.output(PIN_A, 0)
            self.GPIO.output(PIN_B, 1)
            self.GPIO.output(PIN_C, 0)
        elif row == 3:
            self.GPIO.output(PIN_A, 0)
            self.GPIO.output(PIN_B, 1)
            self.GPIO.output(PIN_C, 1)
        elif row == 4:
            self.GPIO.output(PIN_A, 1)
            self.GPIO.output(PIN_B, 0)
            self.GPIO.output(PIN_C, 0)
        elif row == 5:
            self.GPIO.output(PIN_A, 1)
            self.GPIO.output(PIN_B, 0)
            self.GPIO.output(PIN_C, 1)
        elif row == 6:
            self.GPIO.output(PIN_A, 1)
            self.GPIO.output(PIN_B, 1)
            self.GPIO.output(PIN_C, 0)
        elif row == 7:
            self.GPIO.output(PIN_A, 1)
            self.GPIO.output(PIN_B, 1)
            self.GPIO.output(PIN_C, 1)
        time.sleep(0.003)
        self.GPIO.output(PIN_A, 1)
        self.GPIO.output(PIN_B, 1)
        self.GPIO.output(PIN_C, 1)
    
    # shiftBit sequentially pushes a 0 or 1 to the shift registers on the sign

    def shiftBit(self, value):
        self.GPIO.output(PIN_DATA, value)
        self.GPIO.output(PIN_CLOCK, 1)
        self.GPIO.output(PIN_CLOCK, 0)

    # clear sets all values of shift registers to 0

    def clear(self):
        self.GPIO.output(PIN_CLEAR, 0)
        self.GPIO.output(PIN_CLEAR, 1)

    # wrappedDisplay is a wrapper function that renders patterns defined
    # by display() in a looping fasion that is required by hardware of sign

    def wrappedDisplay(self, x):
        timeout = time.time() + 0.015
        while True:
            if x >= 0 and time.time() > timeout:
                break
            if self.options.get('reset') or self.options.get('time'):
                break
            self.display(x)

