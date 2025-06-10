import turtle
import random

christopher = turtle.Turtle()
turtle.colormode(255)
christopher.pensize(10)
christopher.speed("fastest")

#angles we'd like the turtle to move in
directions = [0, 90, 180, 270]

def random_colors():
    """Returns random rgb colors"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)

    #create a tuple of random colors
    random_color = (r, g, b)
    return random_color


# drawing the turtle
for _ in range(200):
    christopher.color(random_colors())
    christopher.forward(20)
    christopher.setheading(random.choice(directions))