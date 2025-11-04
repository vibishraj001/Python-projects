from turtle import *
import random
tim =Turtle()


colors = ["dark red","antique white","indigo","yellow","dark blue"]

def draw_shape(num_side):
    angle = 360 / num_side
    for i in range(num_side):
        tim.forward(100)
        tim.right(angle)

for i in range(3,11):
    tim.color(random.choice(colors))
    draw_shape(i)



