from graphics import *
import time

a = False
b = False
c = False

aLabel = Text(Point(25, 80), "OFF")
bLabel = Text(Point(125, 80), "OFF")
cLabel = Text(Point(225, 80), "OFF")
dataLabel = Text(Point(325, 80), "OFF")

pin_data = "DATA"
pin_clear = "CLEAR"
pin_clock = "CLOCK"

pin_a = "A"
pin_b = "B"
pin_c = "C"

registerHighs = []; # keeps track of POSITIONS all 1's in the data registers

data = False

win = GraphWin("Sign Emulator", 900, 70) # Each light bulb is 10 x 10
registerWin = GraphWin("Bit Registers", 900, 10)
pinWin = GraphWin("Pins", 380, 100)

registersEnabled = False
clocked = False

def setPin(name, high):
    global a, b, c, registerHighs, data

    if name == pin_a:
        a = high;
        updatePinLabel(aLabel, high)
    elif name == pin_b:
        b = high;
        updatePinLabel(bLabel, high)
    elif name == pin_c:
        c = high;
        updatePinLabel(cLabel, high)
    elif name == pin_clock:
        if (clocked == False and high == True and registersEnabled): # we push left after a 0, we ignore if a 1

            # check if the farthest left bit is at the end of the sign, we want to remove it if True
            if (len(registerHighs) > 0 and registerHighs[0] == 0):
                registerHighs.pop(0)

            # Iterate through registers and move every bit to the left 1
            for i in range(len(registerHighs)):
                registerHighs[i] -= 1

            if (data): # if data is set to 1, we append a bit in the register
                registerHighs.append(89)
        clocked = high
    elif name == pin_clear: # Ignores 'high', I'm pretty sure that's how it works
        if (high):
            registersEnabled = True
        else:
            registersEnabled = False
            registerHighs = []
    elif name == pin_data:
        data = high
        updatePinLabel(dataLabel, high)

    rowSelected = a * 4 + b * 2 + c

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
    aPin.draw(pinWin)
    bPin.draw(pinWin)
    cPin.draw(pinWin)
    dataPin.draw(pinWin)
    aLabel.setTextColor('red')
    bLabel.setTextColor('red')
    cLabel.setTextColor('red')
    dataLabel.setTextColor('red')
    aLabel.draw(pinWin)
    bLabel.draw(pinWin)
    cLabel.draw(pinWin)
    dataLabel.draw(pinWin)

main()
