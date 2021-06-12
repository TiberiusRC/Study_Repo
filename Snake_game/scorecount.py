from turtle import Turtle

#Creat a scoreboard from turtle class
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("lime")
        self.penup()
        self.goto(0, 270)
        self.write(f"SCORE :{self.score}", align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def increase_count(self):
        self.score +=1
        self.write(f"SCORE :{self.score}", align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.color("red")
        self.goto(0,0)
        self.write(f"Game over!", align="center", font=("Arial", 20, "bold"))



