# python built in functions: https://docs.python.org/3/library/functions.html
# Ask for the user's first name and display the "Hello [firstname]" output message

firstname = input("Please enter your first name: ")
print("Hello ",firstname,"!", sep='')

# Ask for the user's full name and display the "Hello [firstname] [surname]" output message
# Note: surname value is already set above!

surname = input("Please enter your surname: ")
print ("Hello ",firstname, " ",surname,"!", sep='')

# Print two line with a single line of code

print("What do you call a bear with no teeth?\nA gummy bear!")

# Add two numbers together
num1 = int(input("Please enter your first number: "))
num2 = int(input("Please enter your second number: "))
calc1 = num1 + num2
print("The sum of these numbers is:", calc1)

# More maths
num3 = int(input("Please enter one more number: "))
calc2 = (num1 + num2) * num3
print("The first two numbers' sum, multiplied with the third number is:", calc2)

# Track your remaining pizza slices amount
startSlices = int(input("Please enter the number of pizza slices you started with: "))
eatedSlices = int(input("How many slices have you eaten? "))
slicesLeft = startSlices - eatedSlices
print("You have", slicesLeft, "slices remaining")

# How old you will be next?
age = int(input("How old are you? "))
newAge = age + 1
print(firstname, surname, "in your next birthday you will be", newAge, "years old.")