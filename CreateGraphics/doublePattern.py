import turtle
import random

turtle.speed(0)
turtle.width(2)
turtle.bgcolor('pink')
turtle.colormode(255)

for angle in range(0, 360, 5):
    turtle.goto(0,0)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.color(r,g,b)
    turtle.seth(angle)
    turtle.forward(800)

for angle in range(0, 360, 5):
    turtle.goto(150,150)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.color(r,g,b)
    turtle.seth(angle)
    turtle.forward(800)