#"Stopwatch: The Game" by Naresh Ghanate
#www.naresh.tk

import simplegui
# define global variables
timer=0
time=0
message="Our New Stopwatch Game"
attempts=0
success=0
started=0
# define helper function format that converts integer
# counting tenths of seconds into formatted string A:BC.D
 
def timer_handler():
 
    global time
    time=time+1
    format(time)
 
def format(t):
    global message
    a=t%10
    b=t/10
    c=int(b/60)
    d=int(b%60)
 
    if d<10:
        d="0"+str(d)
        message =str(c)+":"+d+"."+str(a)
    else :
        message =str(c)+":"+str(d)+"."+str(a)
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    global started
    started=1
def stop():
    timer.stop()
    global attempts
    global success
    global label
    global started
    if started==1:
        if time%10==0:
            success=success+1
        started=0
        attempts=attempts+1
    label.set_text("Successful/Total Attempts="+str(success)+"/"+str(attempts))
def reset():
    global time
    global started
    global attempts
    global success
    started=0
    attempts=0
    success=0
    timer.stop()
    time=0
    format(time)
    label.set_text("Successful/Total Attempts="+str(success)+"/"+str(attempts))
 
# define event handler for timer with 0.1 sec interval
 
#draw canvas
def draw(canvas):
    canvas.draw_text(message, [20,112], 18, "Red")
 
# create frame
frame = simplegui.create_frame("Home", 300, 200)
frame.add_button("Start", start)
frame.add_button("Stop", stop)
frame.add_button("Reset", reset)
label=frame.add_label("Successful/Total Attempts="+str(success)+"/"+str(attempts),300)
 
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, timer_handler)
 
# start timer and frame
frame.start()