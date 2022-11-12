sports_list = ["tennis", "football"]
sports_list.append(input("What is your favourite sport? "))
sports_list.sort()
print(sports_list)

subject_list = ["maths", "english", "computing", "history", "science", "spanish"]
print(subject_list)
dislike = input("Which of these subjects do you dislike? ")
getrid = subject_list.index(dislike)
del subject_list[getrid]
print(subject_list)

colours = ["red", "blue", "black", "green", "white", "pink", "grey", "purple", "yellow", "brown"]
start = int(input("Enter a starting number (0-4):" ))
end = int(input("Enter an end number (5-9): "))
print(colours[start:end])

nums = [123, 345, 234, 765]
for i in nums:
    print(i)
selection = int(input("Enter a number from the list: "))
if selection in nums:
    print(selection, "is in position",nums.index(selection))
else:
    print("That is not in the list.")

name1 = input("Enter a name of somebody you want to invite to your party: ")
name2 = input("Enter another name: ")
name3 = input("Enter a third name: ")
party = [name1, name2, name3]
another = input("Do you want to invite another person (y/n)? ")
while another == "y":
    newname = party.append(input("Enter another name: "))
    another = input("Do you want to invite another person (y/n)? ")
print("You have", len(party), "people coming to your party.")
print(party)
selection = input("Enter one of the names: ")
print(selection,"is in position", party.index(selection),"on the list")
stillcome = input("Do you still want them to come(y/n): ")
if stillcome == "n":
    party.remove(selection)
print(party)

tv = ["Task Master", "Top Gear", "The Big Bang Theory", "How I met Your Mother"]
for i in tv:
    print(i)
newtv = input("Enter another tv show: ")
position = int(input("Enter a number between 0 and 3: "))
tv.insert(position, newtv)
for i in tv:
    print(i)

nums1 = []
count = 0
while count < 3:
    num1 = int(input("Enter a number: "))
    nums1.append(num1)
    print(nums1)
    count = count + 1
lastnum = input("Do you want the last number saved (y/n): ")
if lastnum == "n":
    nums1.remove(num1)
print(nums1)