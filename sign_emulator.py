from graphics import *
from enum import Enum
import time

class Pin(Enum):
    A = 0
    B = 1
    C = 2

    DATA  = 3
    CLOCK = 4
    CLEAR = 5

state = {}
for pin in Pin:
    state[pin] = 0

registerHighs = []; # keeps track of POSITIONS all 1's in the data registers



win = GraphWin("Sign Emulator", 900, 70) # Each light bulb is 10 x 10
registerWin = GraphWin("Shift Registers", 900, 10)
pinWin = GraphWin("Pins", 580, 100)



def setPin(pin, high):
    global registerHighs

    if pin == Pin.A:
        state[Pin.A] = high;
        # updatePinLabel(aLabel, high)
    elif pin == Pin.B:
        state[Pin.B] = high;
        # updatePinLabel(bLabel, high)
    elif pin == Pin.C:
        state[Pin.C] = high;
        # updatePinLabel(cLabel, high)
    elif pin == Pin.CLOCK:
        if (high == True):
            if(state[Pin.CLOCK] == 0 and state[Pin.CLEAR] == 1): # we push left after a 0, we ignore if a 1

                # check if the farthest left bit is at the end of the sign, we want to remove it if True
                if (len(registerHighs) > 0 and registerHighs[0] == 0):
                    registerHighs.pop(0)

                # Iterate through registers and move every bit to the left 1
                for i in range(len(registerHighs)):
                    registerHighs[i] -= 1

                if (state[Pin.DATA]): # if data is set to 1, we append a bit in the register
                    registerHighs.append(89)
            state[Pin.CLOCK] = 1
        else:
            state[Pin.CLOCK] = 0
    elif pin == Pin.CLEAR: # Ignores 'high', I'm pretty sure that's how it works
        if (high):
            state[Pin.CLEAR] = 1
        else:
            state[Pin.CLEAR] = 0
            registerHighs = []
    elif pin == Pin.DATA:
        state[Pin.DATA] = high
        # updatePinLabel(dataLabel, high)

    rowSelected = state[Pin.A] * 4 + state[Pin.B] * 2 + state[Pin.C]

    clearScreen(win)
    clearScreen(registerWin)

    for column in registerHighs:
        if (rowSelected != 7):
            lightOn(Point(column * 10, rowSelected * 10), win)
        lightOn(Point(column * 10, 0), registerWin)

def updatePinLabel(label, high):
    newText = "ON" if high else "OFF"
    newColor = "green" if high else "red"
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

def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def main():

    # row (out of 7) chosen by 3 wires A,B,C Binary 111 = off

    # keep row off, shift Data from last column to desired column using Data, Clock, & Clear
    # then turn row on

    # make Sign and Register windows black
    clearScreen(win)
    clearScreen(registerWin)

    #Set up the Pin Monitor
    aPin = Text(Point(25, 25), "A")
    bPin = Text(Point(125, 25), "B")
    cPin = Text(Point(225, 25), "C")
    dataPin = Text(Point(325, 25), "Data")
    clockPin = Text(Point(425, 25), "Clock")
    clearPin = Text(Point(525, 25), "Clear")
    aLabel = Text(Point(25, 80), "OFF")
    bLabel = Text(Point(125, 80), "OFF")
    cLabel = Text(Point(225, 80), "OFF")
    dataLabel = Text(Point(325, 80), "OFF")
    clockLabel = Text(Point(425, 80), "OFF")
    clearLabel = Text(Point(525, 80), "OFF")
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

main()
