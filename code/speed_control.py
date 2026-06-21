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
def move(speed): 
    if speed  speed = 1023 
    lf.write_analog(speed) 
    rf.write_analog(speed) 
display.scroll("Slow speed 300") 
move(300) 
sleep(1500) 
stop() 
sleep(1000) 
display.scroll("Fast speed 900") 
move(900) 
sleep(1500) 
stop() 
