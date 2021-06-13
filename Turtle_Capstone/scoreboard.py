from turtle import Turtle
FONT = ("Courier", 24, "normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("red")
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level_score()

    def level_score(self):
        self.clear()
        self.write(f"Level:{self.level}", align="left", font=("Courier", 24, "bold"))

    def level_up(self):
        self.level += 1
        self.level_score()

    def game_over(self):
        self.goto(100,0)
        self.write(f"GAME OVER !", align="right", font=("Courier", 24, "bold"))
