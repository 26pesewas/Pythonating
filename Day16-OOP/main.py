# # importing Turtle and Screen class from turtle library
# from turtle import Turtle, Screen
#
#
# # creating an object from the class Turtle
# benji = Turtle()
#
# #assigning attributes to our new turtle, benji
# benji.shape("turtle")
# benji.color("DarkGoldenrod1")
# benji.forward(100)
# # creating another object from class Screen
# my_screen = Screen()
#
#
# # Attributes are variables associated with objects. aka what the object has
# # assigning an attribute from Screen class to my_screen object
# print(my_screen.canvheight)
#
# # Methods are functions associated with objects. aka what the object can do
# # calling a method from Screen class
# my_screen.exitonclick()
from IPython.lib.pretty import Printable
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table. add_column("Type", ["Electric", "Water", "Fire"])

# reassigning an attribute
table.align = "l"
print(table)