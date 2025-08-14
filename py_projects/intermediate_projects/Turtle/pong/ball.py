from turtle import Turtle
START_POSITION = (0,0)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bounce_y(self):
        # reduces y coordinates while x increases
        self.y_move *= -1

    def bounce_x(self):
        # reduces x coordinates while y increases
        self.x_move *= -1
        # increases move speed
        self.move_speed *= 0.9

    def reset_ball(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.bounce_x()






