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
GPIO.setup(PIN_B, GPIO.OUT)
GPIO.setup(PIN_C, GPIO.OUT)

GPIO.setup(PIN_DATA,  GPIO.OUT)
GPIO.setup(PIN_CLEAR, GPIO.OUT)
GPIO.setup(PIN_CLOCK, GPIO.OUT)

def switchRow(row):
  GPIO.output(PIN_A, 1)
  GPIO.output(PIN_B, 1)
  GPIO.output(PIN_C, 1)

  if row == 0:
    GPIO.output(PIN_A, 0)
    GPIO.output(PIN_B, 0)
    GPIO.output(PIN_C, 0)
  elif row == 1:
    GPIO.output(PIN_A, 0)
    GPIO.output(PIN_B, 0)
    GPIO.output(PIN_C, 1)
  elif row == 2:
    GPIO.output(PIN_A, 0)
    GPIO.output(PIN_B, 1)
    GPIO.output(PIN_C, 0)
  elif row == 3:
    GPIO.output(PIN_A, 0)
    GPIO.output(PIN_B, 1)
    GPIO.output(PIN_C, 1)
  elif row == 4:
    GPIO.output(PIN_A, 1)
    GPIO.output(PIN_B, 0)
    GPIO.output(PIN_C, 0)
  elif row == 5:
    GPIO.output(PIN_A, 1)
    GPIO.output(PIN_B, 0)
    GPIO.output(PIN_C, 1)
  elif row == 6:
    GPIO.output(PIN_A, 1)
    GPIO.output(PIN_B, 1)
    GPIO.output(PIN_C, 0)
  elif row == 7:
    GPIO.output(PIN_A, 1)
    GPIO.output(PIN_b, 1)
    GPIO.output(PIN_c, 1)
  sleep(0.001)
  GPIO.output(PIN_A, 1)
  GPIO.output(PIN_B, 1)
  GPIO.output(PIN_C, 1)


def shiftout(byte):
  for x in range(8):
    GPIO.output(PIN_DATA, (byte >> x) & 1)
    GPIO.output(PIN_CLOCK, 1)
    GPIO.output(PIN_CLOCK, 0)

GPIO.output(PIN_CLEAR, 1)
try:
  while True:
    for row in range(7):
      GPIO.output(PIN_CLEAR, 0)
      GPIO.output(PIN_CLEAR, 1)
      if row == 0:
        GPIO.output(PIN_DATA, 1)
        GPIO.output(PIN_CLOCK, 1)
        GPIO.output(PIN_CLOCK, 0)
        for x in range(5):
	  GPIO.output(PIN_DATA, 0)
          GPIO.output(PIN_CLOCK, 1)
          GPIO.output(PIN_CLOCK, 0)
      switchRow(row)
except KeyboardInterrupt:
  pass

GPIO.output(PIN_CLEAR, 0) 
print "done."

