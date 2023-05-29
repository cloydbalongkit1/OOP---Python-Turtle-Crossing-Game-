from turtle import Turtle

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('red')
        self.penup()
        self.goto(0, -220)
        self.setheading(90)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

