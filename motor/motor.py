import RPi.GPIO as GPIO
from time import sleep
 
#GPIO.setmode(GPIO.BOARD)

class GpioMotor():
  def __init__(self, in1,in2,en,freq=50,duty=100):
    self.in1=in1
    self.in2=in2
    self.en=en
    self.freq = freq
    self.duty = duty
    
    GPIO.setup(self.in1, GPIO.OUT)
    GPIO.setup(self.in2, GPIO.OUT)
    GPIO.setup(self.en, GPIO.OUT)
    
    self.pwm=GPIO.PWM(self.en,freq)
    
  def changeDutyCycle(self,duty):
    self.duty = duty
    self.pwm.ChangeDutyCycle(self.duty)    
  
  def stop(self):
    self.pwm.stop()
 
  def forward(self):
    GPIO.output(self.in2, GPIO.HIGH)
    GPIO.output(self.in1, GPIO.LOW)
    self.pwm.start(self.duty)

  def reverse(self):
    GPIO.output(self.in1, GPIO.HIGH)
    GPIO.output(self.in2, GPIO.LOW)
    self.pwm.start(self.duty)

  def __str__(self):
    return "Motor(in1=%d,in2=%d,en=%d)"%(self.in1,self.in2,self.en)

#GPIO.cleanup()
