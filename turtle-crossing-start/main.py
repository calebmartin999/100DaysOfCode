import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

scoreboard = Scoreboard()

car_manager = CarManager()
car_manager.starting_cars()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
new_car_timer = 0
while game_is_on:
    time.sleep(0.1)
    # car movement and testing for collision are in the same function
    if not car_manager.move(player.pos()):
        game_is_on = False
        scoreboard.game_over()
    if new_car_timer >= 4:
        car_manager.new_car()
        new_car_timer = 0
    else:
        new_car_timer += 1
    if player.check_finish():
        scoreboard.write_level()
        car_manager.speed_up()
        car_manager.clear_cars()
        car_manager.starting_cars()
    screen.update()

screen.exitonclick()