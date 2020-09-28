letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25:0:-1]
print(backwards) #missing a

backwards = letters[25::-1]
print(backwards) #includes a

backwards = letters[::-1] #reversing the sequence
print(backwards) #includes a

print(letters[16:13:-1]) #qpo
print(letters[4::-1]) #edcba
print(letters[25:17:-1]) #zyxwvuts or letters[:-9:-1]

print()

print(letters[-4:]) #wxyz
print(letters[-1:]) #z
print(letters[1:]) #bcdefghijklmnopqrstuvwxyz
print(letters[:1]) #a
print(letters[0]) #a

letters1 = ""
#print(letters1[0]) # crashes because of empty string