from turtle import Turtle, Screen
line = Turtle()
for i in range(20):
    line.forward(5)
    line.penup()
    line.forward(5)
    line.pendown()
screen = Screen()
screen.exitonclick()