# Here is a Python script that could be used to split semicolon
# separated text from a database text values into a list and count
# how many times the same text is repeated:

# Split semicolon separated text into a list
def split_text(text):
    text_list = text.split(";")
    return text_list

# Count the number of times each item in the list occurs
def count_repeats(text_list):
    # Create a dictionary to store the counts
    count_dict = {}
    
    # Loop through the list and count the number of times each item occurs
    for item in text_list:
        if item in count_dict:
            count_dict[item] += 1
        else:
            count_dict[item] = 1
    
    # Return the dictionary of counts
    return count_dict

# Read in the database text
database_text = input("Enter the database text: ")

# Split the text into a list
text_list = split_text(database_text)

# Count the number of times each item in the list occurs
count_dict = count_repeats(text_list)

# Print the results
print("Item counts:")
for key, value in count_dict.items():
    print(key + ": " + str(value))

"""
To use this script, you would need to replace the database_text variable 
with the actual text from your database. You could then run the script 
to split the text into a list and count the number of times each item 
occurs. The script would then print out the results, showing the counts 
for each item in the list.
"""