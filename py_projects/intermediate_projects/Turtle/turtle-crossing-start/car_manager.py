from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10




class CarManager():
    def __init__(self):
        self.cars = []
        self.counter = 0
        self.last_color = None
        self.car_speed = STARTING_MOVE_DISTANCE

    def generate_car(self):
        """Creates a new car at a random position along the y-axis respecting a rule of 50px away from edge of the screen"""
        new_car = Turtle()
        new_car.shape("square")
        new_color = random.choice(COLORS)
        # checking if new car's color = old car's color and if true, gives the new car a different color
        while new_color == self.last_color:
            new_color = random.choice(COLORS)
        self.last_color = new_color
        new_car.color(new_color)

        new_car.shapesize(1, 2)
        new_car.penup()
        random_y = random.randint(-250,250)
        new_car.goto(300,y=random_y)
        self.cars.append(new_car)

    def move_car(self):
            self.counter += 1
            if self.counter % 6 == 0:
                self.generate_car()

            for car in self.cars:
                car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT


