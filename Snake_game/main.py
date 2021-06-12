from turtle import Screen
from snake import Snake
from food import Food
from scorecount import Score
import time

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("A Snake Game in Python by SIK")
screen.tracer(0)

#Call snake
snake = Snake()
#Call food
food = Food()
#Call score
score = Score()
#Listen for keypresses(Arrows)Directions
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#Animate snake en forward momentum
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    #Collision of objects
    if snake.head.distance(food)< 17:
        print("hmmmmm")
        food.refresh()
        snake.extend()
        score.clear()
        score.increase_count()
    #Bang against wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()

    #STEP ON SNEK!!!!
    for segment in snake.segments:
        #Exclude head collision with itself
        if segment == snake.head:
            pass
        #Ouch at any other part
        elif snake.head.distance(segment)< 10:
            game_is_on = False
            score.game_over()
#Click to exit
screen.exitonclick()
