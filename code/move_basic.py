from microbit import * 
left_motor_forward = pin0 
left_motor_back = pin1 
right_motor_forward = pin2 
right_motor_back = pin3 
def move_forward(speed=600): 
    left_motor_forward.write_analog(speed) 
    left_motor_back.write_analog(0) 
    right_motor_forward.write_analog(speed) 
    right_motor_back.write_analog(0) 
def move_backward(speed=600): 
    left_motor_forward.write_analog(0) 
    left_motor_back.write_analog(speed) 
    right_motor_forward.write_analog(0) 
    right_motor_back.write_analog(speed) 
def stop_car(): 
    left_motor_forward.write_analog(0) 
    left_motor_back.write_analog(0) 
    right_motor_forward.write_analog(0) 
    right_motor_back.write_analog(0) 
move_forward() 
sleep(2000) 
stop_car() 
sleep(1000) 
move_backward() 
sleep(2000) 
stop_car() 
