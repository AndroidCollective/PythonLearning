parrot = "Norwegian Blue"

for character in parrot:
    print(character)

number = "9,223;372:036 854,775;807"

separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

#number = input("Please enter a series of numbers, using any separaters you like: ")
number = "2 3 4 5"
separators = ""

for char in number:
    if not char.isnumeric():
        separators += char

print(separators)

values = "".join(char if char not in separators else " " for char in number).split()
print([int(val) for val in values])

print(sum([int(val) for val in values]))

for i in range(1,21):
    print("i is now {}".format(i))

print()

for i in range(21): #default start at 0
    print("i is now {}".format(i))

print()

for i in range(0,10,2):
    print("i is now {}".format(i))

print()

for i in range(10,0,-2):
    print("i is now {}".format(i))

print()

age  = 25

if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time")