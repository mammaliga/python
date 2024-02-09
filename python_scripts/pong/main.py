from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from time import sleep

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0, 2000)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.listen()

speed = 0.005
game_is_on = True
while game_is_on:
    screen.update()
    sleep(speed)
    ball.move()

    if ball.ycor() > 289 or ball.ycor() < -289:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(
            l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()
        speed -= 0.001

    if ball.xcor() > 384:
        score.l_point()
        ball.reset()

    if ball.xcor() < -384:
        score.r_point()
        ball.reset()

screen.exitonclick()
