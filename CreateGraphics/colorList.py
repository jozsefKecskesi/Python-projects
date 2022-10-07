import turtle

turtle.speed(0)
turtle.colormode(255)
turtle.bgcolor('black')
turtle.width(1)
col = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

for n in range(255):
    turtle.color(col[n%6])
    turtle.fd(n)
    turtle.rt(61)