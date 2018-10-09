import sys
import os
import getopt
import time
from ascii_consts import *

class BaseLED:
    def __init__(self, emulating=True):
        self.emulating = emulating
    
    def shiftBits(self, str):
        for x in range(len(str)):
            self.shiftBit(int(str[x]))

    def print(self, str):
        def disp(self, scroll):
            for row in range(7):   
                self.clear()
                for x in range(len(str)):
                    self.shiftBits(ascii_consts[str[x]][row])
                    self.shiftBit(0)
                for x in range(scroll):
                    self.shiftBit(0)
                self.switchRow(row)

        def strt(self):
            print("Starting")
            try:
                self.clear()
                self.switchRow(7)
                #for x in range(90):
                self.wrappedDisplay(0, 0.1)
                time.sleep(5)

            except KeyboardInterrupt:
                pass

            self.clear()
            print("done.")
        self.display=disp
        self.start=strt
        self.run()

    def display(self):
        pass

    def start(self):
        pass
    
    def run(self):
        self.start(self)


        

