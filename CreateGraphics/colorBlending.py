import turtle

turtle.speed(0)
turtle.colormode(255)

for x in range(0, 200):
    turtle.color(255,128,x)
    turtle.goto(x,0)
    turtle.goto(x, 200)