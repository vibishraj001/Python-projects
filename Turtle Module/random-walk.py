from turtle import *
import random
tim =Turtle()
tim.speed("fastest")

colors = ["dark red","antique white","indigo","yellow","dark blue"]

directions = [0,90,180,270]
tim.pensize(15)

for i in range(200):
    tim.color(random.choice(colors))
    tim.forward(40)
    tim.setheading(random.choice(directions))


