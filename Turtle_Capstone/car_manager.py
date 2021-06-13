from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_amount = random.randint(1,7)
        if random_amount == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_pos = random.randint(-250,250)
            new_car.goto(300 , random_pos)
            self.all_cars.append(new_car)

    def full_throttle(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)





