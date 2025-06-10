from turtle import Turtle, Screen
import random


def draw_polygon(sides):
    """This function draws a regular polygon with the given number of sides"""

    for _ in range(sides):
        angle = 360 / sides  # The angle the turtle must turn at each corner
        christopher.forward(100)  # Move forward by the side length
        christopher.right(angle)      # Turn right to create the next side

# Create the screen and turtle
screen = Screen()
christopher = Turtle()
christopher.speed(6)  # Set drawing speed to a moderate pace (1 is slowest, 10 is fastest)

# turtle colors
turtle_colors = ['red', 'blue', 'green', 'purple', 'orange', 'yellow', 'cyan', 'magenta', 'brown', 'pink']

# Loop to draw polygons with 3 to 10 sides
for shape_sides in range(3, 11):  # 3 = triangle, 4 = square, ..., 10 = decagon
    christopher.color(random.choice(turtle_colors))
    draw_polygon(shape_sides)

screen.exitonclick()  # Keep the window open until you click on it
