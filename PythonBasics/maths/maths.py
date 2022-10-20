import math

num = float(input("Enter a number with lots of decimal places: "))
print(num * 2)
answer = num * 2
print(answer)
print(round(answer, 2))

num1 = int(input("Enter a number over 500: "))
answer1 = math.sqrt(num1)
print(round(answer1, 2))

print(round(math.pi, 5))

radius = int(input("Enter the radius of the circle: "))
depth = int(input("Enter depth: "))
area = round((math.pi * (radius ** 2)), 3)
volume = round((area * depth), 3)
print(area, volume)

num3 = int(input("Enter a number: "))
num4 = int(input("Enter another number: "))
ans3 = num3 // num4
ans4 = num3 % num4
print(num3, "divided by", num4, "is", ans3, "with", ans4, "remaining.")

print("1, Square")
print("2, Triangle\n")

menuselection = int(input("Enter a number: "))
if menuselection == 1:
    side = int(input("Enter the lenght of one side: "))
    area = side * side
    print("The area of your Square is", area)
elif menuselection ==2:
    base = int(input("Enter the lenght of the base: "))
    height = int(input("Enter the height of the triangle: "))
    area = (base * height) / 2
    print("The area of your Triangele is", area)
else:
    print("Incorrect option selected.")