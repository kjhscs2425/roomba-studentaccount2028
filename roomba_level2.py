# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Dr. EB <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward, speed
import room

# Make the turtle go faster
speed(10)

# Draw the Level 2 version of the room
window = room.draw_room(level = 2)


###
# Start your code here
def left1():
    left(90)
    forward(40)
    left(90)
def right1():
    right(90)
    forward(40)
    right(90)
def forward1():
    for i in range(14):
        forward(40)

for i in range(10):
    forward1()
    left1()
    forward1()
    right1()


 
 
# End your code here
###
 
window.exitonclick()