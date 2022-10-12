import turtle
import random

def flower(x, y, pCol):
    turtle.pu()
    turtle.goto(x, y)
    turtle.pd()
    turtle.width(5)
    turtle.seth(90)
    turtle.color('green')
    turtle.fd(70)

    for n in range(5):
        turtle.width(25)
        turtle.rt(72)
        turtle.color(pCol)
        turtle.fd(25)
        turtle.bk(25)
    turtle.color('black')
    turtle.dot(30)

turtle.speed(0)
turtle.bgcolor('lightgreen')
cols = ['red', 'yellow', 'purple', 'orange', 'blue']

for f in range(40):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    flower(x, y, random.choice(cols))