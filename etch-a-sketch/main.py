from turtle import Turtle, Screen

tom = Turtle()
screen = Screen()
def move_forward():
    tom.forward(10)
def move_backward():
    tom.backward(10)
def move_counterclock():
    tom.left(10)
def clockwise():
    tom.right(10)
def eraser():
    tom.penup()
    tom.home()
    tom.clear()
    tom.pendown()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counterclock)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=eraser)
screen.exitonclick()