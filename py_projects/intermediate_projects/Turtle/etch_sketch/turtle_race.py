import turtle
import turtle as t

my_turtle = t.Turtle()
screen = t.Screen()
#moving forward
def forward():
    my_turtle.fd(10)

def backwards():
    my_turtle.bk(10)

def clockwise():
    my_turtle.right(10)

def anticlockwise():
    my_turtle.left(10)

def clear_screen():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()
    my_turtle.pendown()


screen.onkey(key = "w", fun=forward)
screen.onkey(key="a", fun=anticlockwise)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)





screen.listen()
screen.exitonclick()