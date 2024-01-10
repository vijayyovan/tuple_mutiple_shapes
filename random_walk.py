
from random import random, randint


import turtle as t
from turtle import Turtle, Screen

colours = ["red", "blue", "green"]


for i in range(100):
    for x in colours:
        steps = int(random() * 100)  # Now you can just use random()
        angle = int(random() * 360)
    # turtle.color(R)
        t.pencolor(x)
        t.pensize(5)
        t.right(angle)
        t.fd(steps)
screen = Screen()
screen.exitonclick()
