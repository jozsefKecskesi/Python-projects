import turtle

# Draw circles

turtle.color('green')
turtle.dot(500)
turtle.color('blue')
turtle.dot(400)
turtle.color('yellow')
turtle.dot(300)
turtle.color('red')
turtle.dot(200)
turtle.color('purple')
turtle.dot(100)

# Draw a square

turtle.width(30)
turtle.color('white')

for n in range(4):
    turtle.forward(150)
    turtle.right(90)

# Draw patterns

turtle.width(3)
turtle.color('orange')

turtle.speed(0) # Set the speed to the fastest reducing drawing time

for b in range(36):
    turtle.right(10)
    for n in range(4):
        turtle.forward(200)
        turtle.right(90)

turtle.width(4)
turtle.color('black')
for b in range(36):
    turtle.right(10)
    for n in range(4):
        turtle.forward(160)
        turtle.right(90)