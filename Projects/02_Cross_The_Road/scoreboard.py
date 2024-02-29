from turtle import Turtle, Screen

FONT = ("Courier", 24, "normal")
SCORE_POSITION = (-260,255)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.print_score()

        
    def print_score(self):
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Level: {self.level}", align="left", font=FONT )

    def increase_level(self):
        self.level += 1
        self.print_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center", font=FONT)
        self.write()

