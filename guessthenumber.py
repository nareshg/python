# "Guess the number" mini-project by Naresh Ghanate
# www.naresh.tk
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

# initialize global variables used in your code

rand=0
chance=0
flag=0
# define event handlers for control panel
    
def init():
    global flag
    flag=0
    range100()

def range100():
    global rand
    global chance
    global flag
    flag=0
    rand=random.randrange(1,100)
    #print rand
    chance=7
    print ("New game. Range is from 0 to 100")
    print ("Number of remaining guesses is 7")
    print ""
    # button that changes range to range [0,100) and restarts

def range1000():
    global rand
    global chance
    global flag
    flag=0
    rand=random.randrange(1,1000)
    #print rand
    chance=10
    print ("New game. Range is from 0 to 1000")
    print ("Number of remaining guesses is 10")
    print ("")
    # button that changes range to range [0,1000) and restarts
    
def get_input(guess):
# main game logic goes here
    global chance
    global rand
    global flag
    chance=chance-1
    print"Guess was:",guess
    print "Number of remaining guesses is",chance
    if flag==0 and chance==0:
        if(int(guess)==rand):
            print ("Correct!")
            print ""
            flag=1
            init()
        else:    
            print "Game over!"
            print ""
            init()
    elif chance>0:        
        if(int(guess)==rand):
            print ("Correct!")
            print ""
            flag=1
            init()
        elif(int(guess)>rand):
            print ("Lower!")
            print ""
        elif(int(guess)<rand):
            print ("Higher!")
            print ""
    
    
# create frame
f = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", get_input,200)

init()

# start frame
f.start()

# always remember to check your completed program against the grading rubric