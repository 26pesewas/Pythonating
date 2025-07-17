from turtle import Screen, Turtle


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game ")
x_positions = [-10, -20, -30]

for index in range(0,3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.goto(x=x_positions[index],y=0 )


screen.exitonclick()