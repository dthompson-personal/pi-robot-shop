# simple servo test for PCA9685 with HS422
from servo.servo import *
from time import sleep

pca = PCA9685() 
pca.setZero(0)
sleep(2)
for a in xrange(-67,67,1):
  pca.setAngle(0,a)
  sleep(0.05)
for a in xrange(67,0,-1):
  pca.setAngle(0,a)
  sleep(0.05)
