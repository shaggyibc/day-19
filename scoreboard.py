from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=80, stretch_wid=3)
        self.speed("fastest")
        self.goto(-300, -150)
