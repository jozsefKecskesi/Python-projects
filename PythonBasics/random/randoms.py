import random

num = random.randint(1, 100)
print(num)

fruit = random.choice(["apple", "orange", "grape", "banana", "strawberry"])
print(fruit)

coin = random.choice(["h", "t"])
guess = input("Enter heads or tails (h/t): ")
if guess == coin:
    print("you won!")
else:
    print("Bad luck.")
if coin == "h":
    print("It was heads.")
else:
    print("It was tails.")

num = random.randint(1, 5)
guess = int(input("Enter a number: "))
if guess == num:
    print("Well done!")
elif guess > num:
    print(("Too high."))
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You loose")
elif guess < num:
    print(("Too low."))
    guess = int(input("Guess again: "))
    if guess == num:
        print("Correct")
    else:
        print("You loose")

num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True

num = random.randint(1, 10)
correct = False
while correct == False:
    guess = int(input("Enter a number: "))
    if guess == num:
        correct = True
    elif guess > num:
        print("Too high")
    else:
        print("Too low")

score = 0
for i in range(1, 6):
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    correct = num1 + num2
    print(num1, "+", num2, "= ")
    answer = int(input("Your answer: "))
    print()
    if answer == correct:
        score = score + 1
print("You scored", score, "out of 5")

color = random.choice(["red", "blue","green","white","pink"])
print("Select from red, blue, green, white or pink")
tryagain = True
while tryagain == True:
    theirchoice = input("Enter a color: ").lower()
    if color == theirchoice:
        tryagain = False
    else:
        if color == "red":
            print("I bet you seeing RED right now!")
        elif color == "blue":
            print("Dont feel BLUE.")
        elif color == "green":
            print("I bet you are GREEN with envy right now!")
        elif color == "white":
            print("Are you WHITE as a sheet, as you didn't guess correctly?")
        elif color == "pink":
            print("Shame you are not feeling in the pink, as you got it wrong!")