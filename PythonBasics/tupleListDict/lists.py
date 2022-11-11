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