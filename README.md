# pi-robot-shop
Author: David Thompson
Date: January 2018

A fun project for controlling a motor board and some servos off of the GPIO lines, an I2C controller and 8bitdo SNES bluetooth controller.
The project is designed for a raspberry pi 3b v1.2 with 2 auxillary boards:
1) a motor driving board (H-bridges and separate power source) for driving up to 4 motors
2) a I2C pwm PCA96855 for driving upto 16 servos

The motor and servo modules are reusable for different controller configurations.  Currently supports upto 4 motors controlled by GPIO and upto 16 PWM 
controlled servos off I2C.  

## Servos
PCA96855 I2C pwm to drive the HS422 servo

## Motors

A board with the following configuration
---------------------------------
|                               |
|        == G  P  I  O  S  ==   |
|                               |
|  P                            |
|  W    L293    L293            |
|  R                            |
|                               |
|      #1  #2   #3  #4          |
---------------------------------

With the following IO mapping:

1 : GpioMotor(21,19,23)
2 : GpioMotor(18,16,22)
3 : GpioMotor(13,11,15)
4 : GpioMotor(10, 8,12)




