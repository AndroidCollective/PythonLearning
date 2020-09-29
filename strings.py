import math
print('Today is a good day to learn Python')
print('Python is fun')
print("Python's strings are easy to use")
print('We can even include "quotes" in strings')
print("hello" + " World")
greeting = "Hello"
name = "Bruce"
#name = input("Please enter your name ")
print(greeting + ' ' + name)

age = 24


print(age)

print(type(greeting))
print(type(age))

age_in_words = "2 years"
print(name + f" is {age} years old")

print(age)
print(type(age))

cn = complex(6,6)

print(cn)
print(math.pi)

print(f"Pi is approximately {22 / 7:12.50f}")

#interpolation
age = 24
print("My age is %d years" % age)

major = "years"
minor = "months"
print("My age is %d %s, %d %s" %(age, major, 6, minor))
print("PI is approximately %f" %(22/7))
print("PI is approximately % 60.50f" %(22/7))

