from turtle import Turtle
import random

CAR_SPEED = 5

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = CAR_SPEED

    def create_car(self):
            random_chance = random.randint(1,6)
            if random_chance == 1:
                car = Turtle("square")
                car.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                car.penup()
                car.shapesize(stretch_wid=2, stretch_len=1)
                car.tilt(90)
                new_x = random.randint(350, 400)
                new_y = random.randint(-350, 350)
                car.setx(new_x)
                car.sety(new_y)
                car.setheading(180)
                car.speed("fast")
                self.all_cars.append(car)

    def cars_move(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    
    def increase_speed(self):
        self.car_speed += 5
        for car in self.all_cars:
            car.forward(self.car_speed)
