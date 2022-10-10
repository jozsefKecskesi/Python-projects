import turtle # Import the graphics library
import random # Import the random commands

turtle.colormode(255) # Color values can be RGB: 0-255
turtle.bgcolor('light green') # Set background color light green
turtle.color(220, 175, 105) # Set color for the pizza base
turtle.dot(600) # Draw the pizza base
turtle.color(220, 0, 0) # Red for tomato sauce
turtle.dot(500) # Draw the sauce
turtle.color(255, 250, 115) # Pixk yellow for the cheese
turtle.dot(465) # Draw the cheese

turtle.pu() # Stop drawing
for n in range(12): # Repeat the following code 12 times
    turtle.goto(0, 0) # Move to the centre
    turtle.seth(random.randint(1, 360)) # Point to a random direction
    turtle.fd(random.randint(50, 200)) # Move forward a random distance
    turtle.color('black') # Set black for olive
    turtle.dot(35) # Draw a black olive

turtle.color('light green') # Set the same color as the background
turtle.width(5) # Set line width
for s in range(0, 360, 45): # For loop to draw the slice lines
    turtle.goto(0, 0) # Move to the centre
    turtle.pd() # Get ready to draw
    turtle.seth(s) # Set the correct direction
    turtle.fd(300)