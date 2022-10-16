rain = str.lower(input("Is it raining? "))
if rain == "yes":
    windy = str.lower(input("Is it windy? "))
    if windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an umbrella.")
else:
    print("Enjoy tour day!")