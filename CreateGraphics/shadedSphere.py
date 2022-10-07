import turtle

turtle.colormode(255)
turtle.speed(0)
turtle.bgcolor('pink')

for size in range(255, 0, -1):
    turtle.color(120, size, size)
    turtle.dot(3*size)