import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("gray")
screen.tracer(0)

#Create the Critter
player = Player()

#Create score board
scoreboard = Scoreboard()

#Create random traffic
car_manager = CarManager()

#Listen for keypress
screen.listen()
screen.onkeypress(player.move_up,"Up")




#The game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.full_throttle()
    #Finish line and rest position to start
    player.finish_line()
    if player.finish_line() == True:
        scoreboard.level_up()
        scoreboard.level_score()








#Screen close on click
screen.exitonclick()