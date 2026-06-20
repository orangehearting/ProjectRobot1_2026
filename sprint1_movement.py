from microbit import *
import tinybit

# Sprint 1: Basic Movement + Speed Control

def move_forward(speed=255, duration=1000):
    """Move forward with user-defined speed"""
    display.show(Image.ARROW_N)
    tinybit.setMotorPWM(speed, speed, duration)

def move_backward(speed=255, duration=1000):
    """Move backward with user-defined speed"""
    display.show(Image.ARROW_S)
    tinybit.setMotorPWM(-speed, -speed, duration)

def stop(duration=500):
    """Stop the car"""
    display.show(Image.NO)
    tinybit.setMotorPWM(0, 0, duration)

# Main program
while True:
    display.show(Image.HAPPY)
    sleep(500)