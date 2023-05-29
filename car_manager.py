from turtle import Turtle
import random

COLOR = ['green', 'blue', 'yellow', 'white', 'orange']

class Car:

    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.STARTING_SPEED = 5
        self.SPEED_INCREMENT = 2

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.color(random.choice(COLOR))
            new_car.shapesize(1, 2)
            new_car.penup()
            random_y = random.randint(-150, 150)
            new_car.goto(380, random_y)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.STARTING_SPEED)

    def leve_up(self):
        self.STARTING_SPEED += self.SPEED_INCREMENT


