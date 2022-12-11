from array import *

nums = array('i',[45,324,654,45,264])

for x in nums:
    print(x)

# Asking user a new value and adding to the end of the existing array
newValue = int(input("Enter a number: "))
nums.append(newValue)
for x in nums:
    print(x)

# Rverses the order of the array
nums.reverse()
for x in nums:
    print(x)

# Sorts the array into ascending order
nums = sorted(nums)
for x in nums:
    print(x)

# Removing the last item from the array
nums.pop()
for x in nums:
    print(x)

newArray = array('i', [])
more = int(input("How many items: "))
for y in range(0, more):
    newValue = int(input("Enter a number: "))
    newArray.append(newValue)
nums.extend(newArray)

for x in nums:
    print(x)

getRid = int(input("Enter item to remove: "))
nums.remove(getRid)

for x in nums:
    print(x)

# Print how many times a value appears in an array
print(nums.count(45))