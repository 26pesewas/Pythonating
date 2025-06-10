from turtle import Turtle
import random

christopher = Turtle()
christopher.pensize(10)
christopher.speed("fastest")

turtle_colors= [
    "red", "blue", "green", "yellow", "orange", "purple", "pink", "black", "white",
    "gray", "cyan", "magenta", "brown", "turquoise", "salmon", "gold", "navy", "lime",
    "indigo", "violet", "coral", "maroon", "olive", "teal", "orchid", "plum", "tan",
    "beige", "azure", "chocolate", "crimson", "khaki", "lavender", "mint cream", "old lace",
    "sea green", "silver", "slate blue", "snow", "spring green", "tomato", "wheat"
]

#angles we'd like the turtle to move in
directions = [0, 90, 180, 270]


# drawing the turtle
for _ in range(200):
    christopher.color(random.choice(turtle_colors))
    christopher.forward(20)
    christopher.setheading(random.choice(directions))