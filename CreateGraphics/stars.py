import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')

paint = ['red', 'blue', 'orange', 'green', 'yellow', 'lightblue', 'white']

for n in range(150):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    for s in range(5):
        turtle.pendown()        
        turtle.fd(50)
        turtle.rt(144)
    turtle.color(random.choice(paint))
    turtle.penup()
    turtle.goto(x,y)
    