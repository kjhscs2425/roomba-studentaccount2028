# -----------------------------------------------------------------------------
# Roomba in Python
# This file implements an algorithm for a roomba cleaning a room.
#
# Author: Trevor Park <------ REPLACE THIS WITH YOUR NAME!
# -----------------------------------------------------------------------------
 
from turtle import right, left, forward, backward
import room

# Draw the Level 0 version of the room
window = room.draw_room(level = 0)

###
# Start your code here
for i in range(4):
    forward(40)
left(90)
forward(40)
left(90)
for i in range(4):
    forward(40)
right(90)
forward(40)
right(90)
for i in range(4):
    forward(40)
left(90)
forward(40)
left(90)
for i in range(4):
    forward(40)
right(90)
forward(40)
right(90)
for i in range(4):
    forward(40)
    
 
 
# End your code here
###
 
window.exitonclick()