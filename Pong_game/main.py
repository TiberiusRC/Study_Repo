# Breakdown into several steps to make PONG
# Create screen
# Create & move paddle
# Create second paddle
# Create moving ball
# Wall bounce
# paddle bounce
# paddle miss
# 2 player score count
# ---------------------------------------
#Imports
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Create screen object
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong game in Python by 'SIK'")
screen.tracer(0)

#Create scorecounter
scoreboard = Scoreboard()

#Create both paddles
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

#Create ball
ball = Ball()

#Key inputs
screen.listen()
screen.onkeypress(r_paddle.move_up,"Up")
screen.onkeypress(r_paddle.move_down,"Down")
screen.onkeypress(l_paddle.move_up,"w")
screen.onkeypress(l_paddle.move_down,"s")

#Game run
game_runs =True
while game_runs:
    time.sleep(ball.movement)
    screen.update()
    ball.move()
    #Detect bounds for bouncing
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detct paddle bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    #Detect missed R paddle bounce
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    #Detect missed L paddle bounce
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


#Screen stays open till clicked closed
screen.exitonclick()