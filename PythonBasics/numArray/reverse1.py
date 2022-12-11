# Import the 'array' module
from array import array

# Create an empty array of integers
nums = array('i')

# Ask the user to enter 5 numbers
for i in range(5):
    num = int(input("Enter a number: "))
    nums.append(num)

# Sort the numbers in descending order
nums = sorted(nums, reverse=True)

# Print the sorted numbers
print(nums)
