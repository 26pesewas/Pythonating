import turtle as t
import random
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet😼", prompt="Which turtle do you think can win the race? Enter a color: ")
colors = ["red", "yellow", "green", "orange", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
print(user_bet)

for index in range(0,6): # loop 6 times
    new_turtle = t.Turtle(shape="turtle") # creates six new turtles and gives all of them a default shape of turtle
    new_turtle.color(colors[index]) # gives each turtle colors from the colors list
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_positions[index]) # maintain x-coordinates for each turtle and give different y-coordinates to each turtle
    all_turtles.append(new_turtle) # added all six turtle objects to a list of turtles

if user_bet:
    is_race_on = True

    while is_race_on:
        for each_turtle in all_turtles:
            random_distance = random.randint(0,10) # we want each turtle to move forward at random distances
            each_turtle.forward(random_distance) # each turtle will then move by the random distance generated
            if each_turtle.xcor() > 230: # x-coordinate for finish line
                is_race_on = False # stop the game
                winning_color = each_turtle.pencolor() #derive color of winning turtle
                if user_bet == winning_color: # checking if user's bet is same as the color of the winning turtle
                    print("You won! 🥳🥳")
                else:
                    print(f"Sorry. The {winning_color} turtle won. Better luck next time 😔")


screen.listen()
screen.exitonclick()