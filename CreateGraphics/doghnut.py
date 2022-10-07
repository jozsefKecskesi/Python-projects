import turtle
import random

turtle.speed(0)
turtle.colormode(255)
turtle.bgcolor('light blue')
turtle.color(209,154,98)
turtle.dot(600)

turtle.color('pink')
turtle.dot(550)
turtle.color('light blue')
turtle.dot(220)

col = ['white', 'yellow', 'magenta']

turtle.width(10)
for s in range(60):
    turtle.seth(s*6)
    turtle.pu()
    turtle.goto(0,0)
    turtle.fd(random.randint(150, 230))
    turtle.seth(random.randint(1, 360))
    turtle.color(random.choice(col))
    turtle.pd()
    turtle.fd(32)