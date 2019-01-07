#!/usr/bin/python
import RPi.GPIO as GPIO
from motor.motor import *
from controller.controller import *
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

  def RPress(btn, ctn):
    if motors[1]['speed'] > 0 and motors[2]['speed'] < 0 :
      pass
    else:
      motors[1]['speed']=0
      motors[2]['speed']=0
    incSpeed(motors[1])
    decSpeed(motors[2])
    updateMotor(btn, motors[1])
    updateMotor(btn, motors[2])

  def LPress(btn, ctn):
    if motors[2]['speed'] > 0 and motors[1]['speed'] < 0 :
      pass
    else:
      motors[1]['speed']=0
      motors[2]['speed']=0
    incSpeed(motors[2])
    decSpeed(motors[1])
    updateMotor(btn, motors[1])
    updateMotor(btn, motors[2])

  def YPress(btn, ctn):
    incSpeed(motors[1])
    updateMotor(btn, motors[1])
 
  def BPress(btn, ctn):
    decSpeed(motors[1])
    updateMotor(btn, motors[1])

  def XPress(btn, ctn):
    incSpeed(motors[2])
    updateMotor(btn, motors[2])
 
  def APress(btn, ctn):
    decSpeed(motors[2])
    updateMotor(btn, motors[2])

  def StartPress(btn, ctn):
    motors[2]['speed'] = 0
    motors[1]['speed'] = 0
    updateMotor(btn, motors[1])
    updateMotor(btn, motors[2])

  
  try:
    
    js = getController()
   
    js.buttons[0]['cb']=APress
    js.buttons[1]['cb']=BPress
    js.buttons[3]['cb']=XPress
    js.buttons[4]['cb']=YPress
    js.buttons[6]['cb']=LPress
    js.buttons[7]['cb']=RPress
    js.buttons[11]['cb']=StartPress
     
    for e in loop(js):
      sleep(0.01)
      pass

  finally:
    GPIO.cleanup()    
     
if __name__ == "__main__":
  main()


