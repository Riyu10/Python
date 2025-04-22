import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")
turtle.colormode(255)

# Create turtle
spot_painter = turtle.Turtle()
spot_painter.penup()
spot_painter.hideturtle()
spot_painter.speed("fastest")

# Function to generate a random RGB color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Painting settings
num_dots = 10  # Number of dots per row and column
dot_size = 20
spacing = 50

# Starting position
start_x = -spacing * num_dots / 2
start_y = -spacing * num_dots / 2
spot_painter.setpos(start_x, start_y)

# Draw the dots
for row in range(num_dots):
    for col in range(num_dots):
        spot_painter.dot(dot_size, random_color())
        spot_painter.forward(spacing)
    # Move up to next row
    spot_painter.setx(start_x)
    spot_painter.sety(start_y + spacing * (row + 1))

# Exit on click
screen.exitonclick()
