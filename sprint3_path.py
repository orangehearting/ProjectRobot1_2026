from microbit import *
import tinybit

# ========== Sprint 3: Path Control ==========

def move_forward(speed=255, duration=1000):
    """Move forward"""
    display.show(Image.ARROW_N)
    tinybit.setMotorPWM(speed, speed, duration)

def move_backward(speed=255, duration=1000):
    """Move backward"""
    display.show(Image.ARROW_S)
    tinybit.setMotorPWM(-speed, -speed, duration)

def turn_left(speed=255, duration=1000):
    """Turn left"""
    display.show(Image.ARROW_W)
    tinybit.setMotorPWM(-speed, speed, duration)

def turn_right(speed=255, duration=1000):
    """Turn right"""
    display.show(Image.ARROW_E)
    tinybit.setMotorPWM(speed, -speed, duration)

def stop(duration=500):
    """Stop"""
    display.show(Image.NO)
    tinybit.setMotorPWM(0, 0, duration)

def square_path(speed=255):
    """Move in a square path"""
    for i in range(4):
        move_forward(speed, 2000)   # Forward 2s
        stop(500)
        turn_right(speed, 1000)      # Turn right 90 degrees
        stop(500)

def s_path(speed=255):
    """Move in S-shaped path"""
    move_forward(speed, 1500)
    turn_left(speed, 1000)
    move_forward(speed, 1500)
    turn_right(speed, 1000)
    move_forward(speed, 1500)
    stop(500)

# Main program - demonstrate path control
while True:
    display.show(Image.HEART)        # Show heart before start
    sleep(1000)
    
    square_path(255)                 # Run square path
    
    stop(2000)                       # Pause between paths
    
    s_path(255)                      # Run S path
    
    stop(3000)                       # Long pause before repeat