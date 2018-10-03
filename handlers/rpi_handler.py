from base_led import BaseLED
from pin_consts import *

import time

class RPIHandler(BaseLED):
    def __init__(self, emulating=False):
        self.emulating = emulating

        import RPi.GPIO as GPIO
        self.GPIO = GPIO

        self.GPIO.setmode(GPIO.BOARD)

        self.GPIO.setup(PIN_A, self.GPIO.OUT)
        self.GPIO.setup(PIN_B, self.GPIO.OUT)
        self.GPIO.setup(PIN_C, self.GPIO.OUT)

        self.GPIO.setup(PIN_DATA,  self.GPIO.OUT)
        self.GPIO.setup(PIN_CLEAR, self.GPIO.OUT)
        self.GPIO.setup(PIN_CLOCK, self.GPIO.OUT)

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

    def shiftBit(self, value):
        self.GPIO.output(PIN_DATA, value)
        self.GPIO.output(PIN_CLOCK, 1)
        self.GPIO.output(PIN_CLOCK, 0)

    def clear(self):
        self.GPIO.output(PIN_CLEAR, 0)
        self.GPIO.output(PIN_CLEAR, 1)

    def wrappedDisplay(self, scroll, duration):
        timeout = time.time() + duration
        while True:
            if time.time() > timeout:
                break
            self.display(scroll)