import turtle
import random

turtle.speed(0)
turtle.width(2)
turtle.bgcolor('pink')
turtle.colormode(255)

for size in range(800, 0, -10):
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.color(r,g,b)
    turtle.dot(size)