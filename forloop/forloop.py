# Print numbers 1-10
for i in range(1, 11):
    print(i)

# Print numbers 1-10, with 3 as increasement
for i in range(1, 11, 3):
    print(i)

# Print numbers between 1-10, with 2 as decreasement (descending order)
for i in range(10, 1, -2):
    print(i)

# Print a word's letters, each in a new row
word = "kismiska"
for i in word:
    print(i)

name = input("Type in your name: ")
for i in range(0, 3):
    print(name)

num = int(input("Enter a number: "))
for i in range (0, num):
    print(name)

for i in name:
    print(i)

for x in range(0, num):
    for i in name:
        print(i)

num1 = int(input("Enter a number between 1 and 12: "))
for i in range(1, 13):
    answer = i * num1
    print(i, "x", num1, "=", answer)

num2 = int(input("Enter a number below 50: "))
for i in range(50, num2 - 1,  -1):
    print(i)

num3 = int(input("Enter a number: "))
if num3 < 10:
    for i in range(0, num3):
        print(name)
else:
    for i in range(0, 3):
        print("Too high.")

total = 0
for i in range(0, 5):
    num4 = int(input("Enter a number: "))
    ans = input("Do you want this number included? (y/n) ")
    if ans == "y":
        total = total + num4
print(total)

direction = input("Do you want to count up or down? (u/d) ")
if direction == "u":
    num5 = int(input("What is the top number? "))
    for i in range(1, num5 + 1):
        print(i)
elif direction == "d":
    num5 = int(input("Enter a number below 20: "))
    for i in range(20, num5 - 1, -1):
        print(i)
else:
    print("I don't understand.")

num6 = int(input("How many friends do you want to invite to the party? "))
if num6 <10:
    for i in range(0, num6):
        name = input("Enter a name: ")
        print(name, "has been invited.")
else:
    print("Too many people.")