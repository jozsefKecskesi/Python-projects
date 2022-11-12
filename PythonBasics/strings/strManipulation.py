msg = input("Please enter an UPPERCASE message: ")

if msg.isupper():
    print("Well done! Your message is:", msg)
elif msg.islower():
    print("Your message", "-", msg, "-", "is in lowercase.")
else:
    print("This is not in uppercase or lowercase only.")