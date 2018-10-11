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

    def print(self, str, scroll):
        buffer = []
        for x in range(7):
            row = ""
            for y in range(len(str)):
                row += ascii_consts[str[y]][6-x]
                row += '0'
            buffer.append(row)
        if not scroll:
            def disp(self, scroll):
                for row in range(7):   
                    self.clear()
                    for x in range(len(str)):
                        self.shiftBits(ascii_consts[str[x]][6-row])
                        self.shiftBit(0)
                    for x in range(scroll):
                        self.shiftBit(0)
                    self.switchRow(row)
        else:
            print(buffer)
            def disp(self, pos):
                for row in range(7):   
                    self.clear()
                    for x in range(pos):
                        if x >= len(buffer[row]):
                            self.shiftBit(0)
                            continue
                        self.shiftBit(int(buffer[row][x]))
                    self.switchRow(row)


        def strt(self):
            print("Starting")
            try:
                self.clear()
                self.switchRow(7)
                for x in range(90 + len(buffer[0])):
                    self.wrappedDisplay(x, 0.01)
                    time.sleep(.01)

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


        

