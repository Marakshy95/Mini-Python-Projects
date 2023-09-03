from turtle import Screen
from frog import Frog
from cars import CarManager
from levels import Level
import time

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Frogger")
screen.colormode(255)
screen.tracer(0)

frog = Frog()
car = CarManager()
level = Level()

screen.listen()
screen.onkey(frog.go_up, "Up")

is_on = True
while is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.cars_move()


    for x in car.all_cars:
      if x.distance(frog) < 20:
         is_on = False

    if frog.ycor() > 390:
       car.increase_speed()
       frog.reset_position()
       frog.increase_size()
       level.add_level()

screen.exitonclick()

