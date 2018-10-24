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
        self.len = 0
        
    # shiftBits takes a string of 0s and 1s and shifts accordingly
    # currently unused

    def shiftBits(self, str):
        for x in range(len(str)):
            self.shiftBit(int(str[x]))

    # staticDisplay and scrollDisplay are wrapped by wrappedDisplay
    # they display a pattern either inanimate or scrolling

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
    
    # print is called either by led_print or by an external source
    # it deconstructs a string into its ascii representation and then 
    # translates the information into bits recognized by the sign
    # also inserts spaces in between characters and selects either static or scroll
    # display based on options

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
    
    # run starts the session and either scrolls a message or 
    # displays one staic indefinitely
    
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
                self.wrappedDisplay(-1)

        except KeyboardInterrupt:
            pass

        self.clear()
        print("done.")


        

