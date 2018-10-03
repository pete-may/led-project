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

    def run(self):
        self.start()

        

