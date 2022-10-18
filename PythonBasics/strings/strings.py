multiline = """This is a multi line
string, added new rows
to it.
Like an address."""
print(multiline)

sentence = "this is a capitalized sentence."
print(sentence.capitalize())

remove = "This text has no beginning."
print(remove.strip("T"))
print(sentence.capitalize().strip("T"))

number = 20
numberAsString = str(number)
print(type(number))
print(type(numberAsString))

firstname = input("Enter your first name: ")
surname = input("Enter your surname: ")
name = firstname + " " + surname
lenght = len(name)
print(lenght)

firstname = firstname.title()
surname = surname.title()
name = firstname + " " + surname
print(name)

phrase = input("Enter the first line of a nursery rhyme: ")
lenght = len(phrase)
print("This has", lenght, "letters in it")
start = int(input("Enter a starting number: "))
end = int(input("Enter an end number: "))
part = (phrase[start + 1:end + 1])
print(part)

word = input("Enter a word: ")
word = word.upper()
print(word)

name1 = input("Enter your first name: ")
if len(name1) < 5:
    surname1 = input("Enter your surname: ")
    name1 = name1 + surname1
    print(name1.upper())
else:
    print(name1.lower())

word1 = input("Please enter a word: ")
first = word1[0]
lenght = len(word1)
rest = word1[1:lenght]
if first != "a" and first != "e" and first != "i" and first != "o" and first != "u":
    newword = rest + first + "ay"
else:
    newword = word + "way"
print(newword.lower())