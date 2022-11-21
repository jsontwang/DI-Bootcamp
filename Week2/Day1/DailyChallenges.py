# Instructions
# Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.


string = str(input("Input a string:"))

if (string.__len__() < 10):
    print("string not long enough")
elif (string.__len__() > 10):
    print("string too long")

# Then, print the first and last characters of the given text.
print(f"{string[0]} is the first character and second character is {string[string.__len__() -1]}")







# Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:
# The user enters "Hello World"
# Then, you have to construct the string character by character
# H
# He
# Hel
# ... etc
# Hello World
msg = ""
for character in string:
    msg += character
    print(msg)




# 4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

# Hlrolelwod
import string_utils

print(string_utils.shuffle(string))
