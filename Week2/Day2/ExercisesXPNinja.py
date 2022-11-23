

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


