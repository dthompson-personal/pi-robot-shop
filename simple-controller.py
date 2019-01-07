#!/usr/bin/python

from controller.controller import *
from time import sleep


js = getController()
tick = 0
for e in loop(js):
  sleep(0.01)
  tick +=1
  if tick == 15:
    tick = 0
    print js.getPos();
