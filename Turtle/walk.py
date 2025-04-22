from turtle import Turtle, Screen
import random

screen = Screen()
walker = Turtle()
walker.speed(0)  # Fastest speed
walker.pensize(3)

# List of possible directions (degrees)
directions = [0, 90, 180, 270]

# Function to generate a random color
def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    return (r, g, b)

# Perform the random walk
for _ in range(500):
    walker.color(random_color())
    walker.setheading(random.choice(directions))
    walker.forward(20)

# Exit on click
screen.exitonclick()
