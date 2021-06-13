from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        # Create paddle object
        self.penup()
        self.shape("square")
        self.color("honeydew")
        # Paddle shape
        self.shapesize(5, 1)
        # Paddle start position
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)




