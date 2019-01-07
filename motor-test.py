from time import sleep
import RPi.GPIO as GPIO
from motor.motor import *

# ---------------------------------
# |                               |  
# |        == G  P  I  O  S  ==   |
# |                               |
# |  P                            |
# |  W    L293    L293            |
# |  R                            |
# |                               |
# |      #1  #2   #3  #4          |
# ---------------------------------


GPIO.setmode(GPIO.BOARD)
m1 = GpioMotor(21,19,23, duty=75)
m2 = GpioMotor(18,16,22, duty=75)
m3 = GpioMotor(13,11,15, duty=75)
m4 = GpioMotor(10, 8,12, duty=75)

for m,i in [(m1,1),(m2,2),(m3,3),(m4,4)]:
  print "starting %d in 5 seconds ..."%(i)
  sleep(5)
  print "forward"
  m.forward()
  sleep(2)
  print "reverse"
  m.reverse()
  sleep(2)
  print "stopping"
  m.stop()
  


GPIO.cleanup()      


