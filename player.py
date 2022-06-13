from turtle import Turtle
from car_manager import CarManager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 260

car = CarManager


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def backwards(self):
        self.back(MOVE_DISTANCE)

    def level_up(self):
        self.goto(STARTING_POSITION)
        self.clear()






