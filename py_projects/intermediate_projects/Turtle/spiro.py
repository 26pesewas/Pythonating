import turtle as t
import random

christopher = t.Turtle()
t.colormode(255)

def random_color():
    """Returns random rgb colors"""
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0,255)

    #create a tuple of random colors
    color = (r, g, b)
    return color

def draw_spiro(tilt_angle):
    """Draws spirograph shape"""
    for _ in range(int(360 / tilt_angle)):
        christopher.color(random_color())
        christopher.circle(100)
        christopher.setheading(christopher.heading() + tilt_angle)

christopher.speed("fastest")
draw_spiro(5)

screen = t.Screen()
screen.exitonclick()