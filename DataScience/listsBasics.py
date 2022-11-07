# Create an empty list
emptylist = []

# Creating a list with values in it
regions = ["Asia", "America", "Europe"]

# Adding values to the list
my_list = []
my_list.append('Pay bills')
my_list.append('Tidy up')
my_list.append('Walk the dog')
my_list.append('Cook dinner')
my_list.append('Empty the bins')

print(my_list)

print(my_list[0])

# Set an index point before insert a new list value
i = my_list.index('Cook dinner')
my_list.insert(i, 'Go to the pharmacy')
print(my_list)


# How many times a same element appears in a list?
print(my_list.count('Tidy up'))

