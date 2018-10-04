import sys
import os
import getopt
import time
import threading

class BaseLED:
    def __init__(self, emulating=True):
        self.emulating = emulating
        # self.display = None
        # self.start = None
    
    def shiftByte(self, str):

        for x in range(len(str)):
            self.shiftBit(int(str[x]))
    
    def run(self):
        self.start()


        

