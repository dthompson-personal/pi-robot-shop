import pygame as pg
import os
from time import sleep

def simpleBtnCB(button,controler):
  """ a simple callback for printing the event """
  print button['name'],'-',button['value']

class SNES8BitDo():
  """ models the state of an 8bitDo SNES controller """
  def __init__(self,js):
    
    self.js = js
    self.pos=[0,0]
    self.dpos=[0.0, 0.0]
    self.tick = 0
    
    self.buttons = {
      0 : { 'name': 'A', 'value':False, 'cb': simpleBtnCB },
      1 : { 'name': 'B', 'value':False, 'cb': simpleBtnCB },
      3 : { 'name': 'X', 'value':False, 'cb': simpleBtnCB },
      4 : { 'name': 'Y', 'value':False, 'cb': simpleBtnCB },
      6 : { 'name': 'L', 'value':False, 'cb': simpleBtnCB },
      7 : { 'name': 'R', 'value':False, 'cb': simpleBtnCB },
      11 : { 'name': 'start', 'value':False, 'cb': simpleBtnCB },
      10 : { 'name': 'select', 'value':False, 'cb': simpleBtnCB }
    }
    
    self.action = {
      pg.JOYAXISMOTION : lambda x: self.doAxis(x),
      pg.JOYBUTTONUP: lambda x: self.buttonUp(x),
      pg.JOYBUTTONDOWN: lambda x: self.buttonDown(x)
    }
 
  def getPos(self):
    return self.pos

  def buttonUp(self,event):
    self.buttons[event.button]['value'] = False
  
  def buttonDown(self,event):
    self.buttons[event.button]['value'] = True
    self.buttons[event.button]['cb']( self.buttons[event.button], self)
  
  def doAxis(self, event):
    print event
    if event.axis < 2 : 
      self.dpos[event.axis] = event.value / 100.0     
  
  def update(self,event):
    if event:
      self.action[event.type](event)

    self.pos = [ i+j for i,j in zip(self.pos, self.dpos) ]
    if self.pos[0] > 0.15: self.pos[0] = 0.15
    if self.pos[0] < -0.15: self.pos[0] = -0.15
    if self.pos[1] > 0.15: self.pos[1] = 0.15
    if self.pos[1] < -0.15: self.pos[1] = -0.15
  
  def __str__(self):
    buttonstr = ' '.join( ["%s:%s"%(v['name'],v['value']) for v in self.buttons.values() ] )
    return "%s-%s %s"%(self.pos, self.dpos, buttonstr )

def getController():

  while True:
    try:
      os.putenv('SDL_VIDEODRIVER', 'fbcon')
      pg.display.init()
      pg.init()
      
      js = pg.joystick.Joystick(0)
      js.init()
      print "Connected to %s"%(js.get_name())
      state = SNES8BitDo(js)
      return state
    except Exception, e:
      print str(e)
      print "Unable to find controller ... "
      pg.display.quit()
      pg.quit()
      sleep(1)

def loop( controller ):
  """ loop indefinitely yield at least every iteration"""
  while True:
    for e in pg.event.get():
      controller.update(e)
      yield e
    controller.update(None)
    yield None


