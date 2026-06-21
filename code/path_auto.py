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
def turn_left(s=500): 
    rf.write_analog(s) 
def turn_right(s=500): 
    lf.write_analog(s) 
display.scroll("Run custom path") 
forward() 
sleep(2000) 
turn_right() 
sleep(700) 
forward() 
sleep(2000) 
turn_left() 
sleep(700) 
forward() 
sleep(2000) 
stop() 
display.show(Image.HAPPY) 
