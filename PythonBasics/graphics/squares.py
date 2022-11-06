import turtle

def square():
    turtle.begin_fill()
    for i in range(0, 4):
        turtle.forward(70)
        turtle.right(90)
    turtle.penup()
    turtle.end_fill()

turtle.color("black", "red")
square()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
square()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "green")
square()

turtle.exitonclick()