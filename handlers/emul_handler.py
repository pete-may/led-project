from base_led import BaseLED

import os
import time

class EmulHandler(BaseLED):
    def __init__(self, emulating=True, graphic=False):
        self.emulating = emulating
        self.graphic = graphic

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

    def graphicDisplay(self, scroll, duration):
        self.clearScreen()
        self.display(self, scroll)
        for i in range(7):
            for j in range(90):
                if self.bitMap[i][j]:
                    self.lightOn(Point(j * 10, i * 10))

        for i in range(7):
            self.bitMap[i] = [0] * 90
        # time.sleep(duration)

    def consoleDisplay(self, scroll, duration):
        self.cls()
        self.display(self, scroll)
        ledArray = []
        for i in range(7):
            for j in range(90):
                if self.bitMap[i][j]:
                    ledArray.append("X")
                else:
                    ledArray.append("_")
            ledArray.append("\n")
        print("".join(ledArray), end='')
        time.sleep(duration)
        
        for i in range(7):
            self.bitMap[i] = [0] * 90

    def wrappedDisplay(self, scroll, duration):
        if(self.graphic):
            self.graphicDisplay(scroll, duration)
        else:
            self.consoleDisplay(scroll, duration)

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

    def display(self):
        pass

    def start(self):
        pass

    def run(self):
        os.system('clear')
        self.start(self)
