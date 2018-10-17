import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
GPIO.setmode(GPIO.BOARD)             # choose BCM or BOARD  
GPIO.setup(12, GPIO.OUT)           # set GPIO24 as an output   
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
 
try:  
    GPIO.output(12, 0)	# blue             
    GPIO.output(11, 0)	# white
    GPIO.output(13, 0)	# purple
    GPIO.output(15, 0)	# yellow
    GPIO.output(16, 0)	# green	
    GPIO.output(18, 0)	# orange

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt  
    GPIO.cleanup()                 # resets all GPIO ports used by this program  
