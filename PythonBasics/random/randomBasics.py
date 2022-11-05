import random

num = random.random()
num = num * 100
print(num)

num = random.randint(0, 9)
print(num)

num1 = random.randint(0, 1000)
num2 = random.randint(0, 1000)
newnum = num1 / num2
print(newnum)

num = random.randrange(0, 100, 5)
print(num)

color = random.choice(["red", "black", "white", "green"])
print(color)