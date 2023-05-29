from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.color('white')
        self.hideturtle()
        self.goto(-310, 200)
        self.current_score()

    def current_score(self):
        self.write(f'Level: {self.level}', align='center', font=FONT)

    def add_score(self):
        self.level += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER', align='center', font=FONT)

