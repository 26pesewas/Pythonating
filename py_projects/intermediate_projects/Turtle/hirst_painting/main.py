import turtle
import random

# import colorgram
#
# rgb_colors = []
# hirst_colors = colorgram.extract('img.jpg', 30)
#
# extract each rgb color from color object
# for color in hirst_colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colors = (r,g,b)
#     rgb_colors.append(new_colors)


ben = turtle.Turtle()

turtle.colormode(255)
screen = turtle.Screen()

color_list = [(249, 228, 236), (224, 242, 230), (243, 236, 68), (183, 75, 21), (228, 154, 7), (234, 72, 134),
              (200, 163, 114), (216, 228, 238), (202, 131, 191), (116, 168, 241), (220, 231, 5), (76, 173, 37),
              (71, 103, 230), (125, 205, 126), (45, 111, 39), (75, 37, 30), (151, 74, 156), (60, 100, 153),
              (241, 162, 196), (244, 55, 28), (187, 28, 12), (203, 13, 78), (140, 216, 237), (248, 170, 166),
              (76, 67, 47), (148, 185, 244), (159, 212, 173), (253, 10, 4), (42, 90, 32)]

# starting position
ben.setheading(225)
ben.penup()
ben.hideturtle()
ben.speed(0)
ben.forward(300)
ben.setheading(0)

# drawing the dots
num_of_dots = 100
dots_per_row = 10
dot_space = 50

for dot in range(1, num_of_dots + 1):
    ben.dot(20, random.choice(color_list))
    ben.fd(dot_space)
    if dot % dots_per_row == 0:
        ben.setheading(90)
        ben.fd(dot_space)
        ben.setheading(180)
        ben.fd(dot_space * dots_per_row)
        ben.setheading(0)


screen.exitonclick()
