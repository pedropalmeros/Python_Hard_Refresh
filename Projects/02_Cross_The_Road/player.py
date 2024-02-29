from turtle import Turtle

STARTING_POSITION = (0, -280)

MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.restart_turtle()
        self.shape("turtle")

    def restart_turtle(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            print("GANANDO")
            return True
        else:
            return False

    
