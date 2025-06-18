import turtle
import random

naa = turtle.Turtle()
turtle.colormode(255)
screen = turtle.Screen()

# list of rgb colors
color_list = [(249, 228, 236), (224, 242, 230), (243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134),
          (200, 163, 114), (216, 228, 238), (202, 131, 191), (116, 168, 241), (220, 231, 5), (76, 173, 37),
          (71, 103, 230), (125, 205, 126), (45, 111, 39), (75, 37, 30), (151, 74, 156), (60, 100, 153),
          (241, 162, 196), (244, 55, 28), (187, 28, 12), (203, 13, 78), (140, 216, 237), (248, 170, 166),
          (76, 67, 47), (148, 185, 244), (159, 212, 173), (253, 10, 4), (42, 90, 32)]

# Turtle starting position and setup
naa.hideturtle()
naa.speed(0)
naa.penup()
naa.setheading(225)
naa.fd(300)
naa.setheading(90) # Start by pointing up

dots_per_line = 10
dot_size = 20
dot_space = 30

# Function to draw the letter "N"
def draw_n():
    # Part 1: Draw the first vertical line, going up
    for _ in range(dots_per_line - 1):
        naa.dot(dot_size, random.choice(color_list))
        naa.fd(dot_space)
        naa.dot(dot_size, random.choice(color_list))

    # Part 2: Draw the diagonal line
    naa.setheading(315)
    diagonal_space = dot_space * 1.4
    for _ in range(dots_per_line - 1):
        naa.dot(dot_size, random.choice(color_list))
        naa.fd(diagonal_space)
        naa.dot(dot_size, random.choice(color_list))

    # Part 3: Draw the second vertical line, going up
    naa.setheading(90)
    for _ in range(dots_per_line - 1):
        naa.dot(dot_size, random.choice(color_list))
        naa.fd(dot_space)
        naa.dot(dot_size, random.choice(color_list))

draw_n()

screen.exitonclick()