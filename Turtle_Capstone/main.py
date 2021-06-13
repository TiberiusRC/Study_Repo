# Breakdown of steps to create:
# Create screen
# Create player object
# Create scoreboard object
# Create car object
# Create start and finish
# Create score and speed
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
critter_is_alive = True
while critter_is_alive:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.full_throttle()
    #Splat the critter!!
    for car in car_manager.all_cars:
        if car.distance(player) < 20 :
            scoreboard.game_over()
            critter_is_alive = False
    #Crossed the road
    if player.finish_line():
        player.running_start()
        scoreboard.level_up()
        car_manager.road_rage()

#Screen close on click
screen.exitonclick()