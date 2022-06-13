import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
sb = Scoreboard()


screen.listen()
screen.onkeypress(player.move_forward, 'Up')
screen.onkeypress(player.backwards, 'Down')


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for cars in car.all_cars:
        if player.distance(cars) < 20:
            sb.game_over()
            game_is_on = False

    if player.ycor() > 270:
        player.level_up()
        car.increasing_level()
        sb.next_level()

screen.exitonclick()

