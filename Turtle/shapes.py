from turtle import Turtle, Screen
pen = Turtle()
pen.penup()
pen.backward(50)
pen.pendown()
for t in range(3):
    pen.forward(100)
    pen.right(120)
pen.color("red")
for s in range(4):
    pen.forward(100)
    pen.right(90)
pen.color("blue")
for p in range(5):
    pen.forward(100)
    pen.right(72)
pen.color("green")
for h in range(6):
    pen.forward(100)
    pen.right(60)
pen.color("yellow")
for he in range(7):
    pen.forward(100)
    pen.right(51.42)
pen.color("brown")
for o in range(8):
    pen.forward(100)
    pen.right(45)
pen.color("orange")
for n in range(9):
    pen.forward(100)
    pen.right(40)
pen.color("purple")
for d in range(10):
    pen.forward(100)
    pen.right(36)
screen = Screen()
screen.exitonclick()