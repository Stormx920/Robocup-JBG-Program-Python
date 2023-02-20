import sys
from time import sleep
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, GyroSensor, UltrasonicSensor,  InfraredSensor
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from time import sleep

leftMotor = Motor(OUTPUT_A)
rightMotor = Motor(OUTPUT_D)
lineSensorLeft = ColorSensor(INPUT_1)
lineSensorRight = ColorSensor(INPUT_4)
driveSpeed = 20
proportionalGain = 1.3
ultraSensor = UltrasonicSensor(INPUT_3)
tank = MoveTank(OUTPUT_A, OUTPUT_D)
minval = 65
maxval = -65

def main():
    lineSensorRight.MODE_COL_REFLECT
    lineSensorLeft.MODE_COL_REFLECT
    error = lineSensorLeft.reflected_light_intensity - lineSensorRight.reflected_light_intensity
    turnRate = error * proportionalGain
    turnRate = max(maxval, turnRate)
    turnRate = min(minval, turnRate)
    if turnRate >= 60:
        driveSpeed = 10
    if turnRate <=60:
        driveSpeed = 20
    leftMotor.on(speed = driveSpeed + turnRate)
    rightMotor.on(speed = driveSpeed - turnRate - 12)

def roundnround():
    if ultraSensor.distance_centimeters_continuous < 6:
        sleep(0.5)
        tank.on_for_seconds(-25, -25, 1)
        tank.on_for_seconds(20, -20, 1)
        tank.on_for_seconds(65, 80, 0.8)
        tank.on_for_seconds(30, 80, 1.5)

#def jail():
    #tank.on_for_seconds(10, 40, 7)
    #if ultrasensor.distance_centimeters_continuous < 10:

def green():
    if lineSensorRight.color == 3:
        leftMotor.on(speed = 100)
        rightMotor.on(speed = -5)
        sleep(0.5)

def green2():
    if lineSensorRight.color == 3:
        leftMotor.on(speed = 20)
        rightMotor.on(speed = 50)
        sleep(3)
    if lineSensorLeft.color ==3:
        leftMotor.on(speed = 50)
        rightMotor.on(speed = 20)
        sleep(3)

def balls():
    tank.on_for_seconds(30, -30, 1.6)
    