from turtle import Screen,Turtle
import time

screen = Screen()

#global constants
X_POSITIONS = [-10, -20, -30]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake():
    """Creating a snake class"""
    def __init__(self):
        self.my_snakes = []
        self.create_snake()
        self.head = self.my_snakes[0]


    def create_snake(self):
        for index in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=X_POSITIONS[index], y=0)
            self.my_snakes.append(new_turtle)

    def move(self):
        for coordinates in range(len(self.my_snakes) - 1, 0, -1):
            new_x = self.my_snakes[coordinates - 1].xcor()
            new_y = self.my_snakes[coordinates - 1].ycor()
            self.my_snakes[coordinates].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)


