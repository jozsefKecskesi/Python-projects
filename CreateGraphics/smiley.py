import turtle # Import turtle graphics library

turtle.pu() # Stop drawing lines
turtle.color('yellow') # Set color
turtle.dot(400) # Draw a circle

turtle.color('black') # Set color
turtle.goto(80, 70) # Move cursor
turtle.dot(40) # Draw a circle
turtle.goto(-80, 70) # Go to the other side
turtle.dot(40) # Draw a circle
turtle.goto(0, -60) # Go back to the center and down
turtle.dot(160) # Draw a circle
turtle.goto(0, -20) # Go back to the center and little down
turtle.color('yellow') # Set the color
turtle.dot(160) # Draw a circle