ExercisesXP

# 🌟 Exercise 1 : Set
# Instructions
# Create a set called my_fav_numbers with all your favorites numbers.
# Add two new numbers to the set.
# Remove the last number.
# Create a set called friend_fav_numbers with your friend’s favorites numbers.
# Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {-1,0,1}
my_fav_numbers.update([10,100])
my_fav_numbers.remove(100)

friend_fav_numbers = {1,2,3,4,5}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)





# 🌟 Exercise 2: Tuple
# Instructions
# Given a tuple which value is integers, is it possible to add more integers to the tuple?

myTuple = (1,2,3)
"no, tuple is not mutable"



# 🌟 Exercise 3: List
# Instructions
# Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

# Remove “Banana” from the list.
# Remove “Blueberries” from the list.
# Add “Kiwi” to the end of the list.
# Add “Apples” to the beginning of the list.
# Count how many apples are in the basket.
# Empty the basket.
# Print(basket)


basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")

basket.append("Kiwi")
basket.insert(0,"Apples")

basket.count("Apples")

basket.clear()

print(basket)


# 🌟 Exercise 4: Floats
# Instructions
# Recap – What is a float? What is the difference between an integer and a float?
# Can you think of another way to generate a sequence of floats?
# Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).

#float number with decimal integer whole number without decimal 
#numpy
from numpy import arange
myList = []
for i in arange(1.5, 5.5, 0.5):
    myList.append(i)

print(myList)


# for i in range(0,myList.__len__()):
#     if (i%2!=0):
#         myList[i] = int(i)


# print(myList)




# 🌟 Exercise 5: For Loop
# Instructions
# Use a for loop to print all numbers from 1 to 20, inclusive.
# Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.

for i in range(1,21):
    print(i)

# myList = []
# for i in range(1,21):
#     myList.append(i)

for i in range(1,21):
    if(i%2!=0):
        print(i)



# 🌟 Exercise 6 : While Loop
# Instructions
# Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.


name = "Jason"


while(True):
    userInput = input("Enter your name")

    if(userInput == name):
        break

# 🌟 Exercise 7: Favorite Fruits
# Instructions
# Ask the user to input their favorite fruit(s) (one or several fruits).
# Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
# Store the favorite fruit(s) in a list (convert the string of words into a list of words).
# Now that we have a list of fruits, ask the user to input a name of any fruit.
# If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
# If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”.


userInput = input("Input favourite fruit(s) seperated by space: ")


fruitList = userInput.split(" ")


userInputFruit = input("Input any fruit")

if(fruitList.count(userInput)>0):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy")








# Exercise 8: Who Ordered A Pizza ?
# Instructions
# Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.
# Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


toppingList = []

while(True):
    pizzaTopping = input("Input a topping(s):")
    if(pizzaTopping == "quit"):
        break
    else:
        print(f"{pizzaTopping} added to pizza")
        toppingList.append(pizzaTopping)
        

print(f"total price of pizza = {10 + (toppingList.__len__() * 2.5)}")


# Exercise 9: Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.
# Ask a family the age of each person who wants a ticket.
# Store the total cost of all the family’s tickets and print it out.

# A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
# Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
# At the end, print the final list.

priceFamily =[]

familyNumber = int(input("Input number of person"))

for i in range(0,familyNumber):
    userInput = int(input("input age"))
    if(userInput <3):
        priceFamily.append(0)
    elif(12<userInput>3):
        priceFamily.append(10)
    else:
        priceFamily.append(12)

print(f"Total cost: {sum(priceFamily)}")




nameList = ["a","b","c","d"]
print(nameList)

for i in range(0,nameList.__len__()):
    userName = input("Enter your name")
    userAge = int(input("Enter your age"))

    if(16<userAge>21):
        nameList.remove(userName)

print(nameList)


# Exercise 10 : Sandwich Orders
# Instructions
# sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]
# Use the above list called sandwich_orders.
# Make an empty list called finished_sandwiches.
# As each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each sandwich that was made , such as I made your tuna sandwich.



sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

finished_sandwiches = []

for i in sandwich_orders:
    finished = input(f"is {i} finished")
    if(finished == "yes"):
        finished_sandwiches.append(i)


for i in finished_sandwiches:
    print(f"I have made your {i}")
    






# Exercise 11 : Sandwich Orders#2
# Instructions
# Using the list sandwich_orders from the previous exercise, make sure the sandwich ‘pastrami’ appears in the list at least three times.
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of ‘pastrami’ from sandwich_orders.
# Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders = ["Tuna sandwich", "Avocado sandwich", "Egg sandwich", "Sabih sandwich", "Pastrami sandwich"]

add = ("Pastrami sandwich","Pastrami sandwich","Pastrami sandwich")
sandwich_orders.extend(add)

print("Deli runs out of pastrami")
finished_sandwiches = []


for i in sandwich_orders:
        if(i == "Pastrami sandwich"):
            sandwich_orders

            finished = input(f"is {i} finished")
            if(finished == "yes"):
                finished_sandwiches.append(i)
            
for i in finished_sandwiches:
        print(f"I have made your {i}")


#DailyChallenges

# Instructions
# Challenge 1
# Ask the user for a number and a length.
# Create a program that prints a list of multiples of the number until the list length reaches length.
# Examples

# number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

# number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

# number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

userNumber = input()
userLength = input()

    # userNumber = 7
    # userLength = 5
numberList = []

for i in range(1,userLength+1):
    numberList.append(userNumber*i)

    print(numberList)






# Challenge 2
# Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
# Examples

# user's word : "ppoeemm" ➞ "poem"

# user's word : "wiiiinnnnd" ➞ "wind"

# user's word : "ttiiitllleeee" ➞ "title"

# user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
# Notes
# Final strings won’t include words with double letters (e.g. “passing”, “lottery”).
    


userInput = input()
userInput = "ppoeemm"
final = []

for i in userInput:
    print(i)
    if i not in final:
        final.append(i)

    print(final)




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









#ExercisesNinja


# Exercise 1: Formula
# Instructions
# Write a program that calculates and prints a value according to this given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50.
# H is 30.
# Ask the user for a comma-separated string of numbers, use each number from the user as D in the formula and return all the results
# For example, if the user inputs: 100,150,180
# The output should be:

# 18,22,24
import numpy as np
import math

userNumber = input("Input 3 numbers seperated by comma:")
numberList = userNumber.split(",")
numberList

for i in numberList:
    C =50
    H=30
    D = int(i)
    Q =np.sqrt([(2 * C * D)/H])

    print(math.floor(Q))





# Exercise 2 : List Of Integers
# Instructions
# Given a list of 10 integers to analyze. For example:

#     [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
#     [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
#     [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
#     [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]

numberList = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
numberList = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
numberList = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
numberList = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
numberList = [1,1,1,1,1,1,1,1,1,1]


# Store the list of numbers in a variable.
# Print the following information:
# a. The list of numbers – printed in a single line
for i in numberList:
    print(i)

# b. The list of numbers – sorted in descending order (largest to smallest)
numberList.sort(reverse=True)

# c. The sum of all the numbers

sum(numberList)

# A list containing the first and the last numbers.
[numberList[0],numberList[-1]]

# A list of all the numbers greater than 50.
greater50 =[]
for i in numberList:
    if(i>50):
        greater50.append(i)

 
print(greater50)
# A list of all the numbers smaller than 10.
less10 =[]
for i in numberList:
    if(i<10):
        less10.append(i)

 
print(less10)


# A list of all the numbers squared – eg. for [1, 2, 3] you would print “1 4 9”.

squareNumber =[]
for i in numberList:
    squareNumber.append(i**2)

print(squareNumber)
# The numbers without any duplicates – also print how many numbers are in the new list.
notDuplicateNumber =[]

for i in numberList:
    if(i not in notDuplicateNumber):
        notDuplicateNumber.append(i)

notDuplicateNumber
print(f"number in list: {len(notDuplicateNumber)}")

    

# The average of all the numbers.
print(f"average: {sum(numberList)/len(numberList)}")

# The largest number.
max(numberList)
# 10.The smallest number.
min(numberList)
# 11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
sum = 0
for i in numberList:
    sum+= i
print(sum)
# 12.Bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100. Ask the user for an integer between -100 and 100 – repeat this question 10 times. Each number should be added into a variable that you created earlier.
newNumberList = []

for i in range(0,10):
    number = int(input())
    if(number>-100 and number<100):
        newNumberList.append(number)

newNumberList
        
        


# 13.Bonus: Instead of asking the user for 10 integers, generate 10 random integers yourself. Make sure that these random integers are between -100 and 100.
import random
newNumberList = []

for i in range(0,10):
    num = random.randint(-100,100)
    newNumberList.append(num)

    

# 14.Bonus: Instead of always generating 10 integers, let the amount of integers also be random! Generate a random positive integer no smaller than 50.

import random
newNumberList = []

for i in range(0,random.randint(1,50)):
    num = random.randint(-100,100)
    newNumberList.append(num)

    
# 15.Bonus: Will the code work when the number of random numbers is not equal to 10? yes, but has to be greater than 0


# Exercise 3: Working On A Paragraph
# Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
# Paste it to your code, and store it in a variable.

text = """Biomolecular computers have great potential for use in intelligent nanomedicine. They allow computation to be performed at the molecular scale, while also interfacing directly with the molecular components of living systems. Nucleic acids are particularly suited for implementing biomolecular computers. They form stable structures that can be inserted into cells, and interactions between species can be precisely controlled in vitro by modifying their nucleotide sequences. The feasibility of using nucleic acids to solve computational problems was demonstrated by Adleman [1], who used DNA to solve an instance of the directed Hamiltonian path problem. Recent work has also highlighted novel therapeutic applications for nucleic acid computers, such as selectively triggering cell death in cancer cells [2].\
As the cost of DNA synthesis continues to decrease [3], significantly more complex DNA computing devices are being constructed [4,5]. As a result, such devices are also becoming increasingly difficult to design by hand, to the point where design automation tools will soon be indispensable. Such tools should allow for modular designs that encapsulate particular motifs, which can be parametrized and easily replicated [6,7]. They should also allow some of the underlying complexity of the molecular interactions to be abstracted away when focusing on high-level design questions, since complex models are more difficult to work with and more computationally expensive to analyse. Once a high-level design has been completed, such tools should allow further complexity to be subsequently reintroduced, in order to obtain a more realistic model of the system's behaviour prior to its physical construction. In this paper, we present a programming language for designing DNA circuits, which meets these criteria. """


# Let’s analyze the paragraph. Print out a nicely formatted message saying:
# How many characters it contains (this one is easy…).

len(text)
# How many sentences it contains.

len(text.split("."))


# How many words it contains.

len(text.split(" "))


# How many unique words it contains.

len(set(text.split(" ")))
# Bonus: How many non-whitespace characters it contains.

text.count(" ")
# Bonus: The average amount of words per sentence in the paragraph.
newText = text.split(". ")
characterList=[]
count = 0

from statistics import mean

for i in newText:
    count +=1
    sum = len(i)
    characterList.append(sum/count)

        
print(f"Average sentence in a paragraph: {math.floor(mean(characterList))}")


# Bonus: the amount of non-unique words in the paragraph.

len(text.split(" ")) - len(set(text.split(" ")))






# Exercise 4
# Instructions
# Write a program that prints the frequency of the words from the input.

# Suppose the following input is supplied to the program:
text = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

# Then, the output should be:

#     2:2
#     3.:1
#     3?:1
#     New:1
#     Python:5
#     Read:1
#     and:1
#     between:1
#     choosing:1
#     or:2
#     to:1


newText =text.split(" ")

for i in newText:
    print(f"{i}: {newText.count(i)}")



    








# Instructions
# Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
# Display a little cake as seen below:
#        ___iiiii___
#       |:H:a:p:p:y:|
#     __|___________|__
#    |^^^^^^^^^^^^^^^^^|
#    |:B:i:r:t:h:d:a:y:|
#    |                 |
#    ~~~~~~~~~~~~~~~~~~~

# The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

# Bonus : If they were born on a leap year, display two cakes !


number = int(input("Input a number"))


cake ={"|:H:a:p:p:y:|","__|___________|__" , "|^^^^^^^^^^^^^^^^^|","|:B:i:r:t:h:d:a:y:|","|                 |","~~~~~~~~~~~~~~~~~~~"}




number = 10


cake = '''      ___iiiii___
               |:H:a:p:p:y:|
             __|___________|__
            |^^^^^^^^^^^^^^^^^|
            |:B:i:r:t:h:d:a:y:|
            |                 |
            ~~~~~~~~~~~~~~~~~~~
'''
















