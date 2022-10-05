import turtle
import random

turtle.speed(0)
turtle.width(120)
turtle.colormode(255)

for angle in range(0, 360, 10):
    turtle.goto(0,0)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.color(r,g,b)
    turtle.seth(angle)
    turtle.forward(800)