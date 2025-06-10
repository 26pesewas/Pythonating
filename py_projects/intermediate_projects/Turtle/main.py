from turtle import Turtle, Screen

christopher = Turtle()
christopher.shape("turtle")
christopher.color("DarkGoldenrod")

# # drawing a square
# for _ in range(4):
#     christopher.forward(90)
#     christopher.right(90)

# # drawing a dashed line

for _ in range(6):
    christopher.forward(10)
    christopher.penup()
    christopher.forward(10)
    christopher.pendown()





screen = Screen()
screen.exitonclick()
