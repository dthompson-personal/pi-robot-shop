#!/usr/bin/python
import RPi.GPIO as GPIO
from motor.motor import *
from controller.controller import *
from servo.servo import *
from time import sleep


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

def incSpeed(m):
  speed = m['speed']
  speed = min( 100, speed + 10 )
  m['speed'] = speed

def decSpeed(m):
  speed = m['speed']
  speed = max( -100, speed - 10 )
  m['speed'] = speed

def updateMotor(btn, m):
  speed = m['speed']

  if speed > 0 : 
    m['motor'].changeDutyCycle(speed)
    m['motor'].forward()
    print "Forward : %s : %d" %(btn['name'] , speed)

  elif speed < 0 :
    m['motor'].changeDutyCycle(-1*speed)
    m['motor'].reverse()
    print "Reverse : %s : %d" %(btn['name'] , speed)

  elif speed == 0:
    m['motor'].stop()
    print "Stop : %s : %d" %(btn['name'] , speed)


def main():
  GPIO.setmode(GPIO.BOARD)
  
  motors = {
    1 : { 'motor': GpioMotor(21,19,23), 'speed' : 0 },
    2 : { 'motor': GpioMotor(18,16,22), 'speed' : 0 },
    3 : { 'motor': GpioMotor(13,11,15), 'speed' : 0 },
    4 : { 'motor': GpioMotor(10, 8,12), 'speed' : 0 }
  }

  servos = PCA9685()
  servos.setZero(0)
  
  try:
    
    js = getController()

    def IncPress(btn, ctn):
      incSpeed(motors[1])
      updateMotor(btn, motors[1])
   
    def DecPress(btn, ctn):
      decSpeed(motors[1])
      updateMotor(btn, motors[1])


    def StartPress(btn, ctn):
      motors[1]['speed'] = 0
      js.pos = [0.0, 0.0]
      updateMotor(btn, motors[1])
      servos.setZero(0)
   
    js.buttons[0]['cb']=DecPress  # A callback
    js.buttons[1]['cb']=DecPress  # B callback
    js.buttons[3]['cb']=IncPress  # X callback
    js.buttons[4]['cb']=IncPress  # Y callback
    js.buttons[11]['cb']=StartPress
    
    i=0 
    for e in loop(js):
      sleep(0.02)
      x,y=js.getPos()

      if i>= 50:
        i=0
        print x / 0.15 * 90.0

      if x > 0.15: x = 0.15
      if x < -0.15: x = -0.15
      servos.setAngle(0,  x / 0.15 * 90.0 )
      i+=1

  finally:
    GPIO.cleanup()    
     
if __name__ == "__main__":
  main()


