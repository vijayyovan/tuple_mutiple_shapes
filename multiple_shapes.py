import turtle
from turtle import Turtle, Screen


tim = Turtle()
turtle.shape("arrow")
turtle.color("red")

# triangle
for _ in range(3):
    tim.forward(100)
    tim.right(120)

for _ in range(4):
    tim.forward(100)
    tim.right(90)

for _ in range(5):
    tim.forward(100)
    tim.right(72)

for _ in range(6):
    tim.forward(100)
    tim.right(60)

for _ in range(7):
    tim.forward(100)
    tim.right(51.43)

for _ in range(8):
    tim.forward(100)
    tim.right(45)

for _ in range(9):
    tim.forward(100)
    tim.right(40)

for _ in range(10):
    tim.forward(100)
    tim.right(36)


screen = Screen()
screen.exitonclick()

