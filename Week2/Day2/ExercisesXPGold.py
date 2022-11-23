# Exercise 1: Concatenate Lists
# Instructions
# Write code that concatenates two lists together without using the + sign.

list1 = ["Hello","world"]
list2 = ["dlrow olleH"]

list1.extend(list2)
print(list1)





# Exercise 2: Range Of Numbers
# Instructions
# Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.

for i in range(1500,2501):
    if(i%5 ==0 and i%7==0):
        print(i) 



# Exercise 3: Check The Index
# Instructions
# Using this variable

# names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

# Ask a user for their name, if their name is in the names list print out the index of the first occurence of the name.
# Example: if input is 'Cortana' we should be printing the index 1

names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

userName = input("Input a name:")

if userName in names:
    print(names.index(userName))
else:
    print("not in list")







# Exercise 4: Greatest Number
# Instructions
# Ask the user for 3 numbers and print the greatest number.
#     Test Data
#     Input the 1st number: 25
#     Input the 2nd number: 78
#     Input the 3rd number: 87

#     The greatest number is: 87

number = []
suffix = ["st","nd","rd"]

for loop in range(0,3):
    inputNumber = input("input a number:")
    print(f"Input the {loop+1}{suffix[loop]} number: {inputNumber}")
    number.append(inputNumber)
print(f"The gratest number is {max(number)}")




# Exercise 5: The Alphabet
# Instructions
# Create a string of all the letters in the alphabet
# Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.

vowel = ["a","e","u","i","o"]

string = "qwertyuiopasdfghjklzxcvbnm"


for element in string:
    if element in vowel:
        print(f"{element} is a vowel")
    else:
        print(f"{element} is a consonant")





# Exercise 6: Words And Letters
# Instructions
# Ask a user for 7 words, store them in a list named words.
# Ask the user for a single character, store it in a variable called letter.
# Loop through the words list and print the index of the first appearence of the letter variable in each word of the list.
# If the letter doesn’t exist in one of the words, print a friendly message with the word and the letter.

wordList = []

for i in range(0,7):
    userInput = input("Input a word: ")
    wordList.append(userInput)

letter = input("Input a letter:")
# letter ="o"

for char in wordList:
    # print(char)
    if(letter in char):
        print(f"{letter} is in index {char.index(letter)} of {char}")
    else:
        print(f"{letter} not in {char}")



# Exercise 7:
# Instructions
# Create a list of numbers from one to one million and then use min() and max() to make sure your list actually starts at one and ends at one million. Use the sum() function to see how quickly Python can add a million numbers.


def sumNumber():

    numberList = []
    for i in range(1,1000001):
        numberList.append(i)

    # min(numberList)
    # max(numberList)
    sum(numberList)


import timeit
timeit.timeit(sumNumber,number=1)

    





# Exercise 8 : List And Tuple
# Instructions
# Write a program which accepts a sequence of comma-separated numbers. Generate a list and a tuple which contain every number.
# Suppose the following input is supplied to the program: 34,67,55,33,12,98

# Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')



numberList = input("Input sequence of comma-sepearated number: ")

numberList.split(",")

eval(numberList)







# Exercise 9 : Random Number
# Instructions
# Ask the user to input a number from 1 to 9 (including).
# Get a random number between 1 and 9. Hint: random module.
# If the user guesses the correct number print a message that says Winner.
# If the user guesses the wrong number print a message that says better luck next time.
# Bonus: use a loop that allows the user to keep guessing until they want to quit.
# Bonus 2: on exiting the loop tally up and display total games won and lost.




import random

randomNumber = random.randint(0,9)
winner = 0
lose = 0


while(True):
    inputNumber = input()
    if(inputNumber != "quit"):
        if (inputNumber != randomNumber):
            lose+= 1
            print("Better luck next time")
        else:
            winner+= 1
            print("winner")
    else:
         break

print(f"Total win:{winner}")







