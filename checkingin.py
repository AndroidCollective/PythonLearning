parrot = "Norwegian Blue"

letter = input("Enter a character: ")

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
else:
    print("I don't need that letter")

print("-" * 80)

activity = input("What would you like to do today? ")

if "cinema" not in activity.casefold(): #test for caseless match
    print("But I want to go to the cinema")

print("-" * 80)
#challenge

name = input("What is your name? ")
age = int(input("What is your age?"))

if 18 < age < 30:
    print("Welcome to the holiday {}.".format(name))
else:
    print("Sorry {}, no holiday for you.")