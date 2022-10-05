import turtle
import random

turtle.speed(0)
turtle.bgcolor('pink')
turtle.colormode(255) # Preparing for rgb color mode

for n in range(500):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    r = (random.randint(0,255))
    g = (random.randint(0,255))
    b = (random.randint(0,255))
    turtle.width(random.randint(2, 8))
    turtle.color(r,g,b)
    turtle.goto(x,y)