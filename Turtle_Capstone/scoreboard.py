from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.level_score()

    def level_score(self):
        self.clear()
        self.goto(-150,250)
        self.write(f"Level:{self.level}", align="right", font=("Courier", 24, "bold"))

    def level_up(self):
        self.level += 1
        self.level_score()

    def game_over(self):
        pass