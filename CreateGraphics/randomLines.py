from random import random
import turtle
import random

paint = ['red', 'blue', 'yellow', 'orange', 'green', 'lightgreen', 'lightblue', 'darkgreen']

turtle.speed(0)
turtle.bgcolor('pink')

for n in range(100):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    turtle.width(random.randint(20, 60))
    turtle.color(random.choice(paint))
    turtle.goto(x,y)