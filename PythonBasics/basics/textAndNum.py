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

# How much does it cost per head if we split the bill
bill = int(input("What is the total cost of the bill? "))
people = int(input("How many people are there? "))
each = bill / people
print("Each people should pay ", each)

# Number of days exchanged to hours, minutes and seconds.
days = int(input("Enter the number of days: "))
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print("In ", days, " days, there are:\n", hours, " hours, and\n", minutes, " minutes,\n", seconds, " seconds.", sep='')

# Exchange kg to pound
kilo = int(input("Enter the number of kilos: "))
pound = kilo * 2.204
print("That is", pound, "pounds.")

# How many times a small number goes into a bigger one, and what is the remainder
larger = int(input("Enter a number over 100: "))
smaller = int(input("Enter a number under 10: "))
calc3 = larger // smaller
calc4 = larger % smaller
print(smaller, "goes into", larger, calc3, "times, and the remainder is", calc4)
