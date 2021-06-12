from turtle import Turtle,Screen
import random

#Create a Food class with inheritance from Turtle class to access all atributes
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("lime")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_locX = random.randint(-275, 275)
        random_locY = random.randint(-275, 275)
        self.goto(random_locX, random_locY)
