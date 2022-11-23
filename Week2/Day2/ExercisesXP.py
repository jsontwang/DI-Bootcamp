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
