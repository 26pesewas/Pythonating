from turtle import Screen,Turtle
import time

screen = Screen()

#global vars
x_positions = [-10, -20, -30]

class Snake():
    """Creating a snake class"""
    def __init__(self):
        self.my_snakes = []
        self.create_snake()


    def create_snake(self):
        for index in range(0, 3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(x=x_positions[index], y=0)
            self.my_snakes.append(new_turtle)

    def move(self):
        game_is_on = True
        while game_is_on:
            screen.update()
            time.sleep(0.1)
            for coordinates in range(len(self.my_snakes) - 1, 0, -1):
                new_x = self.my_snakes[coordinates - 1].xcor()
                new_y = self.my_snakes[coordinates - 1].ycor()
                self.my_snakes[coordinates].goto(new_x, new_y)
            self.my_snakes[0].forward(20)
