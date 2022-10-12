import turtle

def square(x, y, size, col):
    turtle.color(col)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.begin_fill()
    for n in range(4):
        turtle.fd(size)
        turtle.left(90)
    turtle.end_fill()

square(40, 200, 240, 'red')
square(-100, 240, 160, 'purple')
square(-260, 100, 260, 'yellow')