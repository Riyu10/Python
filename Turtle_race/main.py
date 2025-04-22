from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race?:\n red, orange, yellow, green, blue, indigo, violet")

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
racers = []
 
for index in range(len(colors)):
    racer = Turtle()
    racer.shape("turtle")
    racer.color(colors[index])
    racer.penup()
    racer.goto(-240, 150 - index * 50)
    racer.pendown()
    racers.append(racer)

def start_race():
 while True:
    for racer in racers:
        distance = random.randint(1, 10)
        racer.forward(distance)
        if racer.xcor() >= 230:
            winning_color = racer.pencolor()
            if user_bet == winning_color:
                print("You win.")
            else:
               print("You lose.")
            print(f"The winner is the {winning_color} turtle!")
            return
start_race()
screen.exitonclick()