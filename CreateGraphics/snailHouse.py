import turtle
import random

turtle.speed(0)
turtle.width(4)
turtle.colormode(255)
turtle.bgcolor('pink')

for n in range(500):
    turtle.goto(0,0)
    angle = random.randint(0,360)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.color(r,g,b)
    turtle.seth(angle)
    turtle.forward(angle)