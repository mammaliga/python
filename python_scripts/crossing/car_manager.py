from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_POSITION_Y = 0
STARTING_MOVE_DISTANCE = 4
MOVE_INCREMENT = 2

class CarManager():

    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.add_car()

    def add_car(self):
        car = self.make_car()
        self.cars.append(car)

    def make_car(self):
        car = Turtle()
        car.shape("square")
        car.color(choice(COLORS))
        car.penup()
        car.setheading(180)
        self._set_position(car)
        car.shapesize(stretch_wid=1, stretch_len=2)
        return car

    def _set_position(self, car):
        random_y = randint(-240, 280)
        car.goto(325, random_y)

    def move(self, car):
        car.forward(self.speed)

    def speed_up(self):
        self.speed += MOVE_INCREMENT
