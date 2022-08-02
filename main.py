import turtle
from turtle import Turtle, Screen
import random
screen = Screen()
turtle.colormode(255)
is_race_on = False
winner = screen.textinput(title="Turtle Race Game", prompt="Pick the winner of the race:red, "
                                                           "green, purple, yellow, orange, or blue")

colors = ["red","green", "purple", "yellow", "orange", "blue"]
y_position = [-90, -60, -30, 30, 60, 90]
all_turtles = []


for turtle_index in range(0, 6):
    new_turtles = Turtle()
    new_turtles.shape("turtle")
    new_turtles.color(colors[turtle_index])
    new_turtles.penup()
    new_turtles.goto(x=-300, y=y_position[turtle_index])
    all_turtles.append(new_turtles)

if winner:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        move_distance = random.randrange(0, 10)
        turtle.forward(move_distance)
        if turtle.xcor() > 280:
            color_win = turtle.pencolor()
            print(f"{color_win} was the winner!")
            if color_win == winner:
                print(f"You won!!!!")
            else:
                print("You lose")
            is_race_on = False

# for x in range(100):
#     move_distance = random.randrange(1, 10) + 1
#     timmy.forward(move_distance)
#     x = timmy.xcor()
#     if x > 300:
#         print("Timmy wins!!!")
#         break
#     move_distance = random.randrange(1, 10)
#     green.forward(move_distance)
#     move_distance = random.randrange(1, 10)
#     blue.forward(move_distance)
#     move_distance = random.randrange(1, 10)
#     purp.forward(move_distance)
#     move_distance = random.randrange(1, 10)
#     orange.forward(move_distance)




screen.exitonclick()

# def move_up():
#     # y = timmy.ycor()
#     # timmy.sety(y+10)
#     timmy.forward(5)
#
# def move_down():
#     # y = timmy.ycor()
#     # timmy.sety(y-10)
#     timmy.back(5)
#
# def move_left():
#     # x = timmy.xcor()
#     # timmy.setx(x-10)
#     timmy.left(5)
#
# def move_right():
#     # x = timmy.xcor()
#     # timmy.setx(x+10)
#     timmy.right(5)
#
# def clear_screen():
#     # screen.clear()
#     timmy.clear()
#     timmy.reset()
#
# screen.listen()
# screen.onkey(key="Up", fun=move_up)
# screen.onkey(key="Down", fun=move_down)
# screen.onkey(key="Left", fun=move_left)
# screen.onkey(key="Right", fun=move_right)
# screen.onkey(key="c", fun=clear_screen)
