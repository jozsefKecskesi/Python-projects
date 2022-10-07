import turtle

turtle.speed(0)
turtle.colormode(255)
turtle.bgcolor('blue')
turtle.width(1)

for n in range(255):
    turtle.pencolor(255, 255-n, n)
    turtle.fd(n*2)
    turtle.rt(92)