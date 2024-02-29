from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0        
        self.high_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.load_high_score()
        self.update_scoreboard()
        self.file_name = "data.txt"

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()

        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def load_high_score(self):
        with open('data.txt','r') as score_file:
            data_score = score_file.readline()
        self.high_score = int(data_score)
    
    def write_high_score(self):
        with open('data.txt','w') as score_file:
            score_file.write(f"{self.high_score}")
