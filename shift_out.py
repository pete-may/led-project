import RPi.GPIO as GPIO
from time import sleep 

GPIO.setmode(GPIO.BOARD)
PIN_DATA  = 16	# GREEN
PIN_CLEAR = 15	# YELLOW
PIN_CLOCK = 18	# ORANGE

PIN_A = 12 # BLUE
PIN_B = 11 # WHITE
PIN_C = 13 # PURPLE

GPIO.setup(PIN_A, GPIO.OUT)

GPIO.setup(PIN_DATA,  GPIO.OUT)
GPIO.setup(PIN_CLEAR, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def shiftout(byte):
  for x in range(8):
    GPIO.output(PIN_DATA, (byte >> x) & 1)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)

GPIO.output(PIN_CLEAR, 1)
for x in range(255):
  shiftout(x)
  sleep(0.01)
print "done."


