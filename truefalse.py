day = "Friday"
#day = "Saturday"
temperature = 30
#raining = True
raining = False

if (day == "Saturday" and temperature > 27) or not raining:
    print("Go Swimming")
else:
    print("Learn Python")

print("-" * 80)

if 0:
    print("True") #unreachable
else:
    print("False")

print("-" * 80)

name = input("Please enter your name: ")
#if name:
if name != "":
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")