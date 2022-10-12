import turtle
turtle.speed(0)

def drawSquare(x, y, w, col):
    turtle.goto(x, y)
    turtle.color(col, col) # Set the line and fill color
    turtle.begin_fill()
    for n in range(4):
        turtle.fd(w)
        turtle.rt(90)
    turtle.end_fill()
    if(col == 'blue'):
        col = 'yellow'
    else:
        col = 'blue'
    if(w > 20):
        drawSquare(x + 10, y - 10, w - 20, col)

drawSquare(0, 0, 400, 'blue')