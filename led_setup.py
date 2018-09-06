import sys
import os
import getopt
import time
import threading

class Setup:
    def __init__(self, emulator=False, ledStart=None):
        self.emulator = emulator
        self.ledStart = ledStart

        if(emulator):
            import sign_emulator as emul
            self.emul = emul
        else:
            import RPi.GPIO as GPIO
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
            GPIO.OUTPUT(pin, value)

    def run(self):
        if(self.emulator):
            t = threading.Thread(target=self.ledStart, args=(self.setPin, ))
            t.start()
            self.emul.setup()
        else:
            self.ledStart(self.setPin)

    def getFunc(self):
        return self.setPin
