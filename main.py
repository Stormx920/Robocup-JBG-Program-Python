#!/usr/bin/env python3
import sys
from time import sleep
from ev3dev2.button import Button
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, GyroSensor, UltrasonicSensor,  InfraredSensor
from ev3dev2.motor import Motor, OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D, SpeedPercent, MoveTank, MoveSteering
from time import sleep
from threading import Thread
from mint import main, green, roundnround, green2, balls

start = 0
button = Button()
leftMotor = Motor(OUTPUT_A)
rightMotor = Motor(OUTPUT_D)
lineSensorLeft = ColorSensor(INPUT_1)
lineSensorRight = ColorSensor(INPUT_4)
ultraSensor = UltrasonicSensor(INPUT_3)

while True:
    if button.up:
        start = 1
        print("Nono")

    while start == 1:
        main()
        #green2()
        roundnround()
        sleep(0.001)
        if button.down:
            start = 0
        if 


    while ballHunt == 1
        balls