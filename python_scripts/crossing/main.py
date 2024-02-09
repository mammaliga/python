import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
cars = CarManager()
level = Scoreboard()

screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    for car in cars.cars:
        cars.move(car)
        if player.distance(car) < 25:
            level.game_over()
            game_is_on = False

    if car.xcor() < 300:
        cars.add_car()

    if player.ycor() > 280:
        player.finish()
        level.update_score()
        cars.speed_up()

screen.exitonclick()
