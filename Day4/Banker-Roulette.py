import random
names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(", ")
names_length = len(names)
person = random.randint(0, names_length-1)
# person = random.choice(names)           this is another way to get a random item from a list. 
print(f"{names[person]} is paying the bills tonight!!")
