import time
from turtle import Screen
from car_manager import Car
from player import Player
from score_board import Scoreboard

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title('Turtle Crossing Game')
screen.bgcolor('black')
screen.tracer(0)

car = Car()

player = Player()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key='Up')
screen.onkey(fun=player.move_backward, key='Down')


on_game = True
while on_game:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if player.ycor() > 180:
        score_board.add_score()
        score_board.clear()
        score_board.current_score()
        player.goto(0, -220)
        car.leve_up()
        time.sleep(1)

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            score_board.game_over()
            on_game = False



screen.exitonclick()
