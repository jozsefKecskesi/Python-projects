import turtle
import random

def drawBranch(x, y, size, deg):
    turtle.pu()
    turtle.goto(x, y)
    turtle.setheading(deg)
    turtle.pd()
    turtle.color('brown')
    turtle.width(size * 0.08)
    turtle.fd(size)
    x1 = turtle.xcor() # Store the current x value
    y1 = turtle.ycor() # Store the current y value
    if(size > 5):
        ang1 = deg - random.randint(15, 25)
        ang2 = deg + random.randint(15, 25)
        size1 = size * random.uniform(0.4, 0.8)
        size2 = size * random.uniform(0.4, 0.8)
        drawBranch(x1, y1, size1, ang1)
        drawBranch(x1, y1, size2, ang2)
    else:
        turtle.colormode(255)
        turtle.color(0, random.randint(50, 200), 0)
        turtle.dot(4)
    
turtle.speed(0)
drawBranch(0, 0, 100, 90)

for t in range(5):
    x = 200 * t - 400
    drawBranch(x, -100, 100, 90)