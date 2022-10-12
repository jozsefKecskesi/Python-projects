import turtle

def drawSpiral(side):
    turtle.fd(side)
    turtle.rt(45)
    if (side > 10):
        drawSpiral(side - 5)

turtle.color('orange')
turtle.width(5)

turtle.pu()
turtle.goto(-200, 400)
turtle.pd()
turtle.speed(0)
drawSpiral(330)