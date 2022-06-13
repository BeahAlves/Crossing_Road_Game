from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.level = 1
        self.penup()
        self.goto(-280, 250)
        self.write(f"Level {self.level}", align='left', font=FONT)
        self.hideturtle()

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", align='center', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('Game Over', align='center', font=FONT)





