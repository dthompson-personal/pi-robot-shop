import pygame as pg
import os
import RPi.GPIO as GPIO
from time import sleep
from motor import *

GPIO.setmode(GPIO.BOARD)
m = GpioMotor(18,16,22,duty=75)

os.putenv('SDL_VIDEODRIVER', 'fbcon')
pg.display.init()
pg.init()

js = pg.joystick.Joystick(0)
js.init()
print "Connected to %s"%(js.get_name())

try:
  while True:
    for e in pg.event.get():
      m.forward()
      sleep(1) 
      print e
      m.stop()

    
except KeyboardInterrupt:
  GPIO.cleanup()      

