import sys
import os
import getopt
import time
from ascii_consts import *

# BaseHandler contains functions used by both EmulHandler and RPIHandler

class BaseHandler:
    def __init__(self, options):
        self.options = options
        self.buffer = []
        
    # shiftBits takes a string of 0s and 1s and shifts accordingly
    # currently unused

    def shiftBits(self, str):
        for x in range(len(str)):
            self.shiftBit(int(str[x]))

    # staticDisplay and scrollDisplay are wrapped by wrappedDisplay
    # they display a pattern either inanimate or scrolling

    def staticDisplay(self, scroll):
        str = self.options.get('message')
        for row in range(7):   
            self.clear()
            for x in range(len(str)):
                self.shiftBits(ascii_consts[str[x]][6-row])
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
    


    def flush(self):
        self.options['message'] = ""
        self.clear()
    
    # run is called either by led_print or by an external source
    # it deconstructs a string into its ascii representation and then 
    # translates the information into bits recognized by the sign
    # also inserts spaces in between characters and selects either static or scroll
    # display based on options
    
    def run(self):
        self.buffer = []
        str = self.options.get('message')
        print(str)
        for x in range(7):
            row = ""
            for y in range(len(str)):
                row += ascii_consts[str[y]][6-x]
                row += '0'
            self.buffer.append(row)
        if self.options.get('scroll'):
            self.display=self.scrollDisplay
        else:
            self.display=self.staticDisplay

        try:
            self.clear()
            self.switchRow(7)
            if self.options.get('scroll'):
                for x in range(90 + len(self.buffer[0])):
                    if self.options.get('reset'):
                        break
                    self.wrappedDisplay(x)
            else:
                self.wrappedDisplay(-1)

        except KeyboardInterrupt:
            pass

        self.flush()


        

