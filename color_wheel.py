# Creating a simple Color wheel
from turtle import *

# Create a window for the graphics
setup()

# Create a turtle for drawing
t1 = Turtle()

# Create a list of colors to randomly choose from
colors = ['red', 'blue', 'green', 'yellow', 'purple', 'orange']

import random

t1.up()
t1.goto(-200, 0)
t1.down()

# Change the pen's thickness
t1.width(5)
t1.hideturtle()

# Create a loop for the graphics to be built
for i in range(9001):
    colorchoice = random.choice(colors)
    t1.color(colorchoice)
    t1.forward(400)
    t1.right(181)
    