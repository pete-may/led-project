import sys
import os
import getopt
import time
from ascii_consts import *

class BaseHandler:
    def __init__(self, options):
        self.options = options
        self.buffer = []
        self.len = 0
        
    def shiftBits(self, str):
        for x in range(len(str)):
            self.shiftBit(int(str[x]))

    def staticDisplay(self, scroll):
        for row in range(7):   
            self.clear()
            for x in range(self.len):
                self.shiftBits(ascii_consts[self.options.get('message')[x]][6-row])
                self.shiftBit(0)
            self.switchRow(row)
    
    def scrollDisplay(self, pos):
        for row in range(7):   
            self.clear()
            for x in range(pos):
                if x >= len(self.buffer[row]):
                    self.shiftBit(0)
                    continue
                self.shiftBit(int(self.buffer[row][x]))
            self.switchRow(row)
    
    def print(self, str):
        self.buffer = []
        self.len = len(str)
        for x in range(7):
            row = ""
            for y in range(self.len):
                row += ascii_consts[str[y]][6-x]
                row += '0'
            self.buffer.append(row)
        if self.options.get('scroll'):
            self.display=self.scrollDisplay
        else:
            self.display=self.staticDisplay
        self.run()
    
    def run(self):
        os.system('clear')
        print("Starting")
        try:
            self.clear()
            self.switchRow(7)
            if self.options.get('scroll'):
                for x in range(90 + len(self.buffer[0])):
                    self.wrappedDisplay(x)
            else:
                print("here")
                self.wrappedDisplay(-1)

        except KeyboardInterrupt:
            pass

        self.clear()
        print("done.")


        

