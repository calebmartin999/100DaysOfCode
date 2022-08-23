from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.write("Level: " + str(self.level), False, "Left", FONT)

    def write_level(self):
        self.clear()
        self.level += 1
        self.write("Level: " + str(self.level), False, "Left", FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", False, "Center", FONT)