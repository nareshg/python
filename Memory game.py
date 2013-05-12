# implementation of card game - Memory by Naresh Ghanate
#www.naresh.tk
 
import simplegui
import random
import time
global loop
global turn
global numbers
global exposed
global paired
global turned1,turned2,turned3
global guesses
global message
 
# helper function to initialize globals
def init():
    global turn,loop,paired,swap1,swap2,exposed,numbers,guesses,message,turned1,turned2,turned3
    guesses=0
    turn=0
    loop=0
    message="Hi lets play the memory game"
    turned1=17
    turned2=17
    turned3=17
    paired=[]
    exposed=[]
    numbers=[]
    drawn=0
    for t in range(16):
        exposed.append(0)
        numbers.append(t%8)
        paired.append(0)
    pass
    for t in range(16):
        swap1=random.randint(0,15)
        print swap1
        swap2=random.randint(0,15)
        print swap2
        swap(swap1,swap2)
    print "new numbers"
    print numbers
 
#def swap
def swap(i,j):
    global numbers
    test=numbers[i]
    numbers[i]=numbers[j]
    numbers[j]=test
 
# define event handlers
def mouseclick(pos):
    global turn,turned1,turned2,turned3,exposed,guesses
    x=0
    a=0
    for testpos in range(16):
        x=testpos*50
        a=a+10
        if exposed[testpos]==0:
            check=x+10+a
            if pos[0]>check and pos[0]<=check+50:
                if pos[1]<110 and pos[1]>10:
                   if turn<=2:
                        guesses+=1
                        turn=turn+1
                        exposed[testpos]=1
                        if turn==2:
                            turned2=testpos
                        elif turn==1:
                            turned1=testpos
                        elif turn==3:
                            turned3=testpos
                   else:
                        pass
 
# cards are logically 50x100 pixels in size
def draw(canvas):
    global exposed,turn,turned1,turned2,turned3,message
    x=0
    a=0
    for i in range(16):
       x=i*50
       a=a+10
       if exposed[i]==0 and paired[i]==0:
          canvas.draw_polyline([(10+x+a, 10),(10+x+a,110 ), (60+x+a, 110),(60+x+a,10),(10+x+a,10)], 6, "Red")
       elif exposed[i]==1 and paired[i]==0:
          canvas.draw_text(str(numbers[i]), (25+x+a, 60), 40, "Red")
          if turn==3:
              if paired[turned2]==0:
                    exposed[turned2]=0
                    exposed[turned1]=0
                    exposed[turned3]=1
                    turn=1
                    turned1=turned3
                    turned3=18
 
              print turn
              break
          elif turn==2:
                if numbers[turned2]==numbers[turned1]:
                    paired[turned2]=1
                    paired[turned1]=1
                    message="U found the pair. Awesome <img src="http://s0.wp.com/wp-includes/images/smilies/icon_biggrin.gif?m=1129645325g" alt=":D" class="wp-smiley"> "
                    turn=0
                    turned1=17
                    turned2=18
                else:
                    message="Sorry wrong guess <img src="http://s0.wp.com/wp-includes/images/smilies/icon_sad.gif?m=1129645325g" alt=":(" class="wp-smiley"> "
          elif turn==1:
              message="Do you know where its pair is? :/"
              pass
       elif exposed[i]==1 and paired[i]==1:
          canvas.draw_text(str(numbers[i]), (25+x+a, 60), 40, "Red")
 
    i=0
    canvas.draw_text("You have guessed "+str(guesses)+" times", (0, 200), 20, "Blue")
    end=1
    for i in range(16):
        if paired[i]!=1:
            end=0
        else:
            pass
    if end==1:
        message="You won <img src="http://s0.wp.com/wp-includes/images/smilies/icon_biggrin.gif?m=1129645325g" alt=":D" class="wp-smiley">  Congrats.. To play again click on Restart"
 
    canvas.draw_text(message, (0, 300), 30, "White")
 
# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 1500, 500)
frame.add_button("Restart", init)
frame.add_button("Shuffle", init)
l=frame.add_label("Moves = 0")
 
# initialize global variables
init()
 
# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
 
# get things rolling
frame.start()