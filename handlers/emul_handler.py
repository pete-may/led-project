from handlers.base_handler import BaseHandler

import os
import time
import signal

# EmulHandler renders patterns on emulator; inherits functions from BaseHandler
# Comes in two flavors: console, and applet with graphics
# Console - better for testing patterns and time sensitive changes
# Applet - looks cool, but doesn't render quick enough for real testing

class EmulHandler(BaseHandler):
    def __init__(self, options):
        self.options = options

        self.graphic = self.options.get('graphic')

        # define internal state of virtual sign
        # selectedRow - current row selected
        # registerBits - current state of shift registers
        # bitMap - state of every led on sign 7x90=630 either on or off, used for final render

        self.selectedRow = 7
        self.registerBits = 0
        self.bitMap = [0] * 7
        for i in range(7):
            self.bitMap[i] = [0] * 90

        # python graphics setup

        if(self.graphic):
            from lib.graphics import GraphWin, Rectangle, Point 
            global Rectangle, Point
            self.win = GraphWin("Sign Emulator", 900, 70) # Each light bulb is 10 x 10
            self.flush = self.clearScreen
        else:
            self.flush = self.cls

    # switchRow selects new row, when called this functions updates bitMap with 
    # values from registerBits and then clears registerBits for new row

    def switchRow(self, row):
        self.selectedRow = row
        for x in range(0, 90):
            if(self.registerBits & (1 << x)):
                self.bitMap[6-self.selectedRow][89-x] = 1
        
        self.registerBits = 0

    # shiftBit pushes either 0 or 1 into virtual registers

    def shiftBit(self, value):
       self.registerBits = self.registerBits << 1
       if (value):
            self.registerBits = self.registerBits | 1

    # clear set values in registerBits to 0

    def clear(self):
        self.registerBits = 0

    # graphicDisplay is used when applet mode is selected, writes all values of bitMap to 
    # grid of yellow and black squares
    
    def graphicDisplay(self, x):
        self.clearScreen()
        self.display(x)
        for i in range(7):
            for j in range(90):
                if self.bitMap[i][j]:
                    self.lightOn(Point(j * 10, i * 10))

        for i in range(7):
            self.bitMap[i] = [0] * 90
        
        if x < 0:
            signal.pause()
        else:
            time.sleep(0.05)

    # consoleDisplay is used when console mode is selected, writes all values of bitMap to
    # STDOUT in the form of X's for ON and _'s for OFF

    def consoleDisplay(self, x):
        self.cls()
        self.display(x)
        ledArray = []
        for i in range(7):
            for j in range(90):
                if self.bitMap[i][j]:
                    ledArray.append("X")
                else:
                    ledArray.append("_")
            ledArray.append("\n")
        print("".join(ledArray), end='')

        for i in range(7):
            self.bitMap[i] = [0] * 90

        if x < 0:
            while(True):
                if self.options.get('reset'):
                    break
        else:
            time.sleep(0.05)

    # wrappedDisplay selects either applet mode or console mode, based on given options

    def wrappedDisplay(self, x):
        if(self.graphic):
            self.graphicDisplay(x)
        else:
            self.consoleDisplay(x)

    #applet functions

    def drawRect(self, point, color):
        rect = Rectangle(point, Point(point.x + 10, point.y + 10))
        rect.setFill(color)
        rect.draw(self.win)

    def lightOn(self, point):
        self.drawRect(point, 'yellow')

    def lightOff(self, point):
        self.drawRect(point, 'black')

    def clearScreen(self):
        blackBackground = Rectangle(Point(0, 0), Point(self.win.width, self.win.height))
        blackBackground.setFill('black')
        blackBackground.draw(self.win)

    #end of applet functions

    # cls is used in console mode, clears STDOUT for writing to console

    def cls(self):
        for i in range(7):
            print("\033[F", end='')

