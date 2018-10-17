from handlers.base_handler import BaseHandler

import os
import time
import signal

class EmulHandler(BaseHandler):
    def __init__(self, options):
        self.options = options

        self.graphic = self.options.get('graphic')

        self.selectedRow = 7
        self.registerBits = 0
        self.bitMap = [0] * 7
        for i in range(7):
            self.bitMap[i] = [0] * 90

        # python graphics
        if(self.graphic):
            from graphics import GraphWin, Rectangle, Point 
            global Rectangle, Point
            self.win = GraphWin("Sign Emulator", 900, 70) # Each light bulb is 10 x 10

    def switchRow(self, row):
        self.selectedRow = row
        for x in range(0, 90):
            if(self.registerBits & (1 << x)):
                self.bitMap[6-self.selectedRow][89-x] = 1
        
        self.registerBits = 0

    def shiftBit(self, value):
       self.registerBits = self.registerBits << 1
       if (value):
            self.registerBits = self.registerBits | 1

    def clear(self):
        self.registerBits = 0

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
            signal.pause()
        else:
            time.sleep(0.05)

    def wrappedDisplay(self, x):
        if(self.graphic):
            self.graphicDisplay(x)
        else:
            self.consoleDisplay(x)

    # python graphics

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

    def cls(self):
        for i in range(7):
            print("\033[F", end='')

