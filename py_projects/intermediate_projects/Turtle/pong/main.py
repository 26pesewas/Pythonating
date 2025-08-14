import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create player 1
right_player = Paddle()
right_player.create_paddle((350,0))
right_player.go_up()
right_player.go_down()

# create player 2
left_player = Paddle()
left_player.create_paddle((-350,0))
right_player.go_up()
right_player.go_down()

# creating the ball
my_pong = Ball()

# score
score = Scoreboard()

screen.listen()
# key controls per player
screen.onkey(right_player.go_up,"Up")
screen.onkey(right_player.go_down,"Down")
screen.onkey(left_player.go_up,"w")
screen.onkey(left_player.go_down,"s")


# Main game
game_on = True
winning_point = 3

while game_on:
    screen.update()
    time.sleep(0.04)
    my_pong.move()

    # Detect collision with wall
    if my_pong.ycor() > 280 or my_pong.ycor() < -280:
        my_pong.bounce_y()

    # Detect collision with paddles
    if my_pong.distance(right_player) < 50 and my_pong.xcor() > 320 or my_pong.distance(left_player) < 50 and my_pong.xcor() < -320:
        my_pong.bounce_x()

    # Detect when ball goes out of bounds
    # Add score to a player when ball goes out of bounds

    # if right player misses ball
    if my_pong.xcor() > 400:
        my_pong.reset_ball()
        score.update_l()

    # if left player misses ball
    elif my_pong.xcor() < -400:
        my_pong.reset_ball()
        score.update_r()

    # detecting winner
    if score.l_score == winning_point:
        game_on = False
        print("Left player wins")
    elif score.r_score == winning_point:
        game_on = False
        print("Right player wins")








screen.exitonclick()
