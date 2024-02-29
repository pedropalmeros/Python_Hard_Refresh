from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

game_is_on = False
screen = Screen()
screen.bgcolor("black")
screen.setup(width=1100, height=850)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

game_is_on = True

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > (280) or ball.ycor() < - 280:
        ball.bounce('y')


    if ball.xcor() > (380):
        ball.reset_position()
        scoreboard.r_point()

    if  ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.l_point()

    #Detect collision with the paddel
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330) or (ball.distance(l_paddle)< 50 and ball.xcor() < -330):
        ball.bounce('x')

screen.exitonclick()







