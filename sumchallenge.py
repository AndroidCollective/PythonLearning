# print("Please choose your option from the list bellow:")
# print("1:\tLearn Python")
# print("2:\tLearn Java")
# print("3:\tGo Swimming")
# print("4:\tHave Dinner")
# print("5:\tGo to bed")
# print("0:\tExit")
choice = "-"
while choice != 0:

    if choice in "12345":
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list bellow:")
    print("1:\tLearn Python")
    print("2:\tLearn Java")
    print("3:\tGo Swimming")
    print("4:\tHave Dinner")
    print("5:\tGo to bed")
    print("0:\tExit")

    choice = input()