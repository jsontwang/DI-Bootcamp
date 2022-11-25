# Count Occurence
# Write a program which takes a string and a character as an input, and finds out the number of occurrences the character has in the string.

# String: Programming is cool!
# Character: o
# 3

string = input("Input a string:")
character = input("Input the character to search:")

# string ="This is a great example"
# character ="e"

count =0
for i in string.lower():
    if character.lower() == i:
        count += 1

print(F"String: {string}")
print(F"Character: {character}")
print(count)


# String: This is a great example
# Character: y
# 0


