from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_pace = 1
        self.y_pace = 1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x_pace
        new_y = self.ycor() + self.y_pace

        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_pace *= -1

    def bounce_x(self):
        self.x_pace *= -1

    def reset(self):
        self.home()
        self.bounce_x()
