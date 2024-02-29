import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    #DETECT COLLISION
    collision = car_manager.detect_collision(player)
    if collision:
        game_is_on = False
        scoreboard.game_over()

    #DETECT CROSS ROAD
    succeed = player.is_at_finish_line()
    if succeed:
        player.restart_turtle()
        car_manager.level_up()
        scoreboard.increase_level()
    

    
