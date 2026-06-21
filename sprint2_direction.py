from microbit import *
import tinybit

# ========== Sprint 2: Direction Control ==========

def move_forward(speed=255, duration=1000):
    """Move forward"""
    display.show(Image.ARROW_N)
    tinybit.setMotorPWM(speed, speed, duration)

def move_backward(speed=255, duration=1000):
    """Move backward"""
    display.show(Image.ARROW_S)
    tinybit.setMotorPWM(-speed, -speed, duration)

def turn_left(speed=255, duration=1000):
    """Turn left: left motor backward, right motor forward"""
    display.show(Image.ARROW_W)
    tinybit.setMotorPWM(-speed, speed, duration)

def turn_right(speed=255, duration=1000):
    """Turn right: left motor forward, right motor backward"""
    display.show(Image.ARROW_E)
    tinybit.setMotorPWM(speed, -speed, duration)

def stop(duration=500):
    """Stop"""
    display.show(Image.NO)
    tinybit.setMotorPWM(0, 0, duration)

# Main program - demonstrate direction control
while True:
    move_forward(255, 2000)   # Forward 2s
    stop(1000)                # Stop 1s
    turn_left(255, 1000)      # Turn left 1s
    stop(1000)
    move_backward(255, 2000)  # Backward 2s
    stop(1000)
    turn_right(255, 1000)     # Turn right 1s
    stop(1000)