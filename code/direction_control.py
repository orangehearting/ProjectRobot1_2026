from microbit import * 
lf = pin0 
lb = pin1 
rf = pin2 
rb = pin3 
def stop(): 
    lf.write_analog(0) 
    lb.write_analog(0) 
    rf.write_analog(0) 
    rb.write_analog(0) 
def forward(s=600): 
    lf.write_analog(s) 
    rf.write_analog(s) 
    lb.write_analog(0) 
    rb.write_analog(0) 
def turn_left(s=500): 
    lf.write_analog(0) 
    rf.write_analog(s) 
def turn_right(s=500): 
    lf.write_analog(s) 
    rf.write_analog(0) 
forward() 
sleep(1500) 
turn_left() 
sleep(800) 
turn_right() 
sleep(800) 
backward() 
sleep(1500) 
stop() 
