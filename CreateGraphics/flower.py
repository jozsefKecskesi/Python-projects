import turtle

turtle.bgcolor('lightgreen')
turtle.speed(0)

turtle.width(10)
turtle.seth(90)
turtle.color('green')
turtle.fd(140)

for n in range(5):
    turtle.width(50)
    turtle.rt(72)
    turtle.color('orange')
    turtle.fd(50)
    turtle.bk(50)

turtle.color('red')
turtle.dot(60)