# Draw random dots - refer to Python-projects/randomDots.png

import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')

paint = ['red', 'blue', 'orange', 'green', 'yellow', 'lightblue', 'white']

for n in range(150):
    x = random.randint(-400, 400)
    y = random.randint(-400, 400)
    dotsize = random.randint(20, 65)
    turtle.color(random.choice(paint))
    turtle.goto(x,y)
    turtle.dot(dotsize)