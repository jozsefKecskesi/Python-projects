import turtle

turtle.pu()
turtle.colormode(255)

def eye():
    turtle.color('white')
    turtle.dot(40)
    turtle.color('black')
    turtle.dot(25)   

def ear():
    turtle.width(40)
    turtle.color(104, 60, 17)
    turtle.pd()
    turtle.seth(270)
    turtle.fd(90)

turtle.goto(0, -300)
turtle.color(147, 96, 55)
turtle.width(150)
turtle.goto(0, -120)
turtle.pd()
turtle.goto(350, -120)

turtle.width(60)
turtle.goto(400, -400)
turtle.goto(350, -120)
turtle.goto(300, -400)
turtle.width(20)
turtle.goto(350, -120)
turtle.goto(400, 100)
turtle.pu()
turtle.width(60)
turtle.goto(0, -120)
turtle.pd()
turtle.goto(-50, -400)
turtle.goto(0, -120)
turtle.goto(50, -400)
turtle.pu()

turtle.goto(0, 0)
turtle.color(177, 127, 74)
turtle.dot(150)

turtle.goto(-30, 30)
eye()
turtle.goto(30, 30)
eye()

turtle.goto(0, -40)
turtle.color(202, 158, 103)
turtle.dot(80)

turtle.goto(0, -10)
turtle.color('black')
turtle.dot(30)

turtle.goto(-80, 20)
ear()
turtle.pu()
turtle.goto(80, 20)
ear()