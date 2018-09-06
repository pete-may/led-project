from graphics import *
from enum import Enum
import sys
import os
import getopt
import time

class Pin(Enum):
    A = 12
    B = 11
    C = 13

    DATA  = 16
    CLOCK = 18
    CLEAR = 15

state = {}
for pin in Pin:
    state[pin] = 0

registerBits = []; # keeps track of POSITIONS all 1's in the data registers
bitMap = 0
oldBitMap = [0, 0, 0, 0, 0, 0, 0]


aLabel = Text(Point(25, 80), "OFF")
bLabel = Text(Point(125, 80), "OFF")
cLabel = Text(Point(225, 80), "OFF")
dataLabel = Text(Point(325, 80), "OFF")
clockLabel = Text(Point(425, 80), "OFF")
clearLabel = Text(Point(525, 80), "OFF")


win = GraphWin("Sign Emulator", 900, 70) # Each light bulb is 10 x 10
# registerWin = GraphWin("Shift Registers", 900, 10)

buttons = False

usage = 'usage: python ' + os.path.basename(__file__) + ' <file_with_data>'

def parse_args(argv):
    global emulator, buttons
    try:
        opts, args = getopt.getopt(argv, "hb", ["help", "emulator"])
    except getopt.GetoptError:
        print(usage)
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print(usage)
            sys.exit()
        if opt == '-b':
            buttons = True
            print("buttons enabled")

def setPin(pin, value):
    global registerBits, bitMap, oldBitMap

    pin = Pin(pin)
    # print("pin = {}".format(pin))
    # print("value = {}".format(value))
    # print("value=" + value)
    # time.sleep(1)

    if pin == Pin.A:
        state[Pin.A] = value;
        updatePinLabel(aLabel, value)
    elif pin == Pin.B:
        state[Pin.B] = value;
        updatePinLabel(bLabel, value)
    elif pin == Pin.C:
        state[Pin.C] = value;
        updatePinLabel(cLabel, value)
    elif pin == Pin.CLOCK:
        if (value == True):
            if(state[Pin.CLOCK] == 0 and state[Pin.CLEAR] == 1): # we push left after a 0, we ignore if a 1

                # check if the farthest left bit is at the end of the sign, we want to remove it if True
                # if (len(registerBits) > 0 and registerBits[0] == 0):
                #     registerBits.pop(0)

                # Iterate through registers and move every bit to the left 1
                # for i in range(len(registerBits)):
                #     registerBits[i] -= 1

                bitMap = bitMap << 1

                if (state[Pin.DATA]): # if data is set to 1, we append a bit in the register
                #     registerBits.append(89)
                    bitMap = bitMap | 1
            state[Pin.CLOCK] = 1
            updatePinLabel(clockLabel, value)
        else:
            state[Pin.CLOCK] = 0
            updatePinLabel(clockLabel, value)
    elif pin == Pin.CLEAR: # Ignores 'value', I'm pretty sure that's how it works
        if (value):
            state[Pin.CLEAR] = 1
            updatePinLabel(clearLabel, value)
        else:
            state[Pin.CLEAR] = 0
            updatePinLabel(clearLabel, value)
            # registerBits = []
            bitMap = 0
    elif pin == Pin.DATA:
        state[Pin.DATA] = value
        updatePinLabel(dataLabel, value)
        # updatePinLabel(dataLabel, value)

    rowSelected = state[Pin.A] * 4 + state[Pin.B] * 2 + state[Pin.C]
    if pin == Pin.C and rowSelected != 7:
        # clearScreen(win)
        # clearRow(win, rowSelected)
        # clearScreen(registerWin)

        # for column in registerBits:
        #     if (rowSelected != 7):
        #         lightOn(Point(column * 10, rowSelected * 10), win)

        for x in range(0, 90):
            # print(bitMap)
            if(bitMap & (1 << x)):
                # print("Match")
                # print(x)
                if not(oldBitMap[rowSelected] & (1 << x)):
                    lightOn(Point((89 - x) * 10, rowSelected * 10), win)
                # print(bitMap)
            elif(oldBitMap[rowSelected] & (1 << x)):
                lightOff(Point((89 - x) * 10, rowSelected * 10), win)
            # lightOn(Point(column * 10, 0), registerWin)x
        oldBitMap[rowSelected] = bitMap

def updatePinLabel(label, value):
    newText = "ON" if value else "OFF"
    newColor = "green" if value else "red"
    label.setText(newText)
    label.setTextColor(newColor)

def drawRect(point, win, color):
    rect = Rectangle(point, Point(point.x + 10, point.y + 10))
    rect.setFill(color)
    rect.draw(win)

def lightOn(point, win):
    drawRect(point, win, 'yellow')

def lightOff(point, win):
    drawRect(point, win, 'black')

def clearScreen(window):
    blackBackground = Rectangle(Point(0, 0), Point(window.width, window.height))
    blackBackground.setFill('black')
    blackBackground.draw(window)

def clearRow(window, row):
    x1 = 0
    y1 = row * 10
    x2 = window.width
    y2 = (row + 10) * 10
    blackBackground = Rectangle(Point(x1, y1), Point(x2, y2))
    blackBackground.setFill('black')
    blackBackground.draw(window)

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def setup():
    clearScreen(win)

def main(argv):
    parse_args(argv)

    global buttons

    # row (out of 7) chosen by 3 wires A,B,C Binary 111 = off

    # keep row off, shift Data from last column to desired column using Data, Clock, & Clear
    # then turn row on

    # make Sign and Register windows black
    clearScreen(win)
    # clearScreen(registerWin)

    #Set up the Pin Monitor
    pinWin = GraphWin("Pins", 580, 100)
    aPin = Text(Point(25, 25), "A")
    bPin = Text(Point(125, 25), "B")
    cPin = Text(Point(225, 25), "C")
    dataPin = Text(Point(325, 25), "Data")
    clockPin = Text(Point(425, 25), "Clock")
    clearPin = Text(Point(525, 25), "Clear")
    aPin.draw(pinWin)
    bPin.draw(pinWin)
    cPin.draw(pinWin)
    dataPin.draw(pinWin)
    clockPin.draw(pinWin)
    clearPin.draw(pinWin)
    aLabel.setTextColor('red')
    bLabel.setTextColor('red')
    cLabel.setTextColor('red')
    dataLabel.setTextColor('red')
    clockLabel.setTextColor('red')
    clearLabel.setTextColor('red')
    aLabel.draw(pinWin)
    bLabel.draw(pinWin)
    cLabel.draw(pinWin)
    dataLabel.draw(pinWin)
    clockLabel.draw(pinWin)
    clearLabel.draw(pinWin)

    aRect = Rectangle(Point(10, 60), Point(43, 93))
    aRect.draw(pinWin)

    bRect = Rectangle(Point(110, 60), Point(143, 93))
    bRect.draw(pinWin)

    cRect = Rectangle(Point(210, 60), Point(243, 93))
    cRect.draw(pinWin)

    dataRect = Rectangle(Point(310, 60), Point(343, 93))
    dataRect.draw(pinWin)

    clockRect = Rectangle(Point(410, 60), Point(443, 93))
    clockRect.draw(pinWin)

    clearRect = Rectangle(Point(510, 60), Point(543, 93))
    clearRect.draw(pinWin)
    if buttons:
        try:
            while True:
                clickPoint = pinWin.getMouse()

                if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
                    aLabel.setText("")
                elif inside(clickPoint, aRect):
                    if(state[Pin.A]):
                        setPin(Pin.A, 0);
                        aLabel.setText("OFF")
                        aLabel.setTextColor('red')
                    else:
                        setPin(Pin.A, 1);
                        aLabel.setText("ON")
                        aLabel.setTextColor('green')
                elif inside(clickPoint, bRect):
                    if(state[Pin.B]):
                        setPin(Pin.B, 0);
                        bLabel.setText("OFF")
                        bLabel.setTextColor('red')
                    else:
                        setPin(Pin.B, 1);
                        bLabel.setText("ON")
                        bLabel.setTextColor('green')
                elif inside(clickPoint, cRect):
                    if(state[Pin.C]):
                        setPin(Pin.C, 0);
                        cLabel.setText("OFF")
                        cLabel.setTextColor('red')
                    else:
                        setPin(Pin.C, 1);
                        cLabel.setText("ON")
                        cLabel.setTextColor('green')
                elif inside(clickPoint, dataRect):
                    if(state[Pin.DATA]):
                        setPin(Pin.DATA, 0);
                        dataLabel.setText("OFF")
                        dataLabel.setTextColor('red')
                    else:
                        setPin(Pin.DATA, 1);
                        dataLabel.setText("ON")
                        dataLabel.setTextColor('green')
                elif inside(clickPoint, clockRect):
                    if(state[Pin.CLOCK]):
                        setPin(Pin.CLOCK, 0);
                        clockLabel.setText("OFF")
                        clockLabel.setTextColor('red')
                    else:
                        setPin(Pin.CLOCK, 1);
                        clockLabel.setText("ON")
                        clockLabel.setTextColor('green')
                elif inside(clickPoint, clearRect):
                    if(state[Pin.CLEAR]):
                        setPin(Pin.CLEAR, 0);
                        clearLabel.setText("OFF")
                        clearLabel.setTextColor('red')
                    else:
                        setPin(Pin.CLEAR, 1);
                        clearLabel.setText("ON")
                        clearLabel.setTextColor('green')

        except KeyboardInterrupt:
            pass

    print("\nExited.")

setup()

if __name__ == '__main__':
    main(sys.argv[1:])
