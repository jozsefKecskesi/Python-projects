# Import the 'Decimal' and 'random' modules for precision with decimal numbers and generating random numbers, respectively
from decimal import Decimal
import random

# Create an array of 5 random numbers with two decimal places between 10 and 100
numbers = [Decimal(random.uniform(10, 100)) for i in range(5)]

# Ask the user for a whole number between 2 and 5
while True:
    try:
        # Get the user's input and convert it to a whole number
        user_input = int(input("Enter a whole number between 2 and 5: "))

        # Check if the number is between 2 and 5
        if 2 <= user_input <= 5:
            # If it is, exit the loop
            break
        else:
            # If it isn't, display an error message and ask again
            print("Error: Please enter a number between 2 and 5.")
    except ValueError:
        # If the user enters something that can't be converted to a whole number, display an error message and ask again
        print("Error: Please enter a whole number between 2 and 5.")

# Divide each number in the array by the user's input and display the results
for number in numbers:
    result = number / user_input
    # Use the 'round' function to round the result to two decimal places
    print(round(result, 2))
