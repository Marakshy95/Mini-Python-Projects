from turtle import Turtle
from turtle import Screen

char = Turtle()       # << Turtle is class(blueprint to create an object, capital first letter?!), char is the OBJECT
print(char)
char.shape("turtle")
char.forward(100)


my_screen = Screen()
print(my_screen.canvheight)   #<<<<<< tapping into an attribute which is the screena nd u can see the size is 300 ???? basically saved variables ???
my_screen.exitonclick()       #<<<< this is a method.... methods are kinda like functions that are built it indicated by the () at the end.
