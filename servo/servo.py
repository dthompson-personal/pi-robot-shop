# Class fo  using the PCA96855 I2C pwm to drive the HS422 servo
# author: David Thompson
# date: Feb 19, 2018
from __future__ import division
import time

import Adafruit_PCA9685

PWM_FREQ = 50 # hz
MAX_PULSE = 2100 # us  (+67.5 deg)
MIN_PULSE =  900 # usi (-67.5 deg)
ZERO_PULSE = 1500 # us
PULSE_LENGTH_PER_BIT = 1000000.0 / PWM_FREQ / 4096 # us / bit
PULSE_PER_DEGREE = 400.0 / 45 # us / deg

class PCA9685():
  """ a class for managing a bunch of HS422 Servos on a PCA9685 """
  def __init__(self, address=0x40, busnum=1):
    self.pwm = Adafruit_PCA9685.PCA9685(address) 
    self.pwm.set_pwm_freq(PWM_FREQ);

  def setPulse(self, channel, pulse):
    """ pulse is an amount in us """
    
    if pulse > MAX_PULSE:
      pulse = MAX_PULSE
    if pulse < MIN_PULSE:
      pulse = MIN_PULSE
    
    #print "Channel %d set to %d us (%d bits)"%(channel, pulse, int(pulse/PULSE_LENGTH_PER_BIT) )
    self.pwm.set_pwm(channel, 0, int(pulse / PULSE_LENGTH_PER_BIT) )

  def setZero(self, channel):
    """ zero the servo at the specified channel """
    self.setPulse(channel, ZERO_PULSE)

  def setAngle(self, channel, angle):
    """ set the angle of the servo in degrees (-67.5 deg -> 67.5 deg )"""
    pulse = PULSE_PER_DEGREE*angle + ZERO_PULSE 
    self.setPulse(channel, pulse)   
   
