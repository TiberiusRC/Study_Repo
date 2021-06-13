from turtle import Turtle
START_POS = (0, -280)
BRAVE_MOVE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.color("lime")
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.running_start()


    def running_start(self):
        self.goto(START_POS)

    def finish_line(self):
        if self.ycor() > FINISH_LINE_Y :
            return True
        else:
            return False
            # self.goto(STARTING_POSITION)
            # car_manager.road_rage()

    def move_up(self):
        self.forward(BRAVE_MOVE)


