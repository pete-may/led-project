import sys
import os
import getopt
import time
import threading

PIN_A = 12 # BLUE
PIN_B = 11 # WHITE
PIN_C = 13 # PURPLE

PIN_DATA  = 16  # GREEN
PIN_CLOCK = 18  # ORANGE
PIN_CLEAR = 15  # YELLOW

class Setup:
    def __init__(self, emulator=False, ledStart=None):
        self.emulator = emulator
        self.ledStart = ledStart

        if(emulator):
            import sign_emulator as emul
            self.emul = emul
        else:
            import RPi.GPIO as GPIO
            self.GPIO = GPIO
            GPIO.setmode(GPIO.BOARD)

            GPIO.setup(PIN_A, GPIO.OUT)
            GPIO.setup(PIN_B, GPIO.OUT)
            GPIO.setup(PIN_C, GPIO.OUT)

            GPIO.setup(PIN_DATA,  GPIO.OUT)
            GPIO.setup(PIN_CLEAR, GPIO.OUT)
            GPIO.setup(PIN_CLOCK, GPIO.OUT)

    def setPin(self, pin, value):
        if(self.emulator):
            self.emul.setPin(pin, value)
        else:
            self.GPIO.output(pin, value)

    def run(self):
        if(self.emulator):
            t = threading.Thread(target=self.ledStart, args=(self.setPin, ))
            t.start()
            self.emul.setup()
        else:
            self.ledStart(self.setPin)

    def getFunc(self):
        return self.setPin
