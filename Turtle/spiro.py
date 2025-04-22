from turtle import Turtle, Screen
import random

Me = Turtle()
Me.speed(0)
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

for _ in range(72):
    Me.color(random_color())
    Me.circle(100)
    Me.left(5)

screen = Screen()
screen.exitonclick()