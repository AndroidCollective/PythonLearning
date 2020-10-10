import random

for i in range(10):
    print("i is now {}".format(i))

i = 0
while i < 10:
    print("i is now {}".format(i))
    i += 1

# available_exits = ["north", "south", "east", "west"]
#
# chosen_exit = ""
# while chosen_exit not in available_exits:
#     chosen_exit = input("Please choose a direction: ")
#     if chosen_exit.casefold() == "quit":
#         print("Game over")
#         break
#
# print("aren't you glad you got out of there")
highest = 1000
answer = random.randint(1,highest)
print(answer) #TODO: Remove after testing

print("Please pick a number between 1 and {}: or 0 to quit".format(highest))
# guess = int(input())
#
# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have guessed incorrectly")
# else:
#     print("You got it first time")
print(9//4)
guess = 99999
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Program terminated")
        break
    if guess == answer:
        print("Well done, you guessed it")
        break
    if guess < answer:
        print("Please guess higher")
    else:
        print("Please guess lower")