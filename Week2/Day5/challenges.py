# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

list1 = [1,23,4,55,6,64,123,4664]
list1.insert(0,-1)
print(list1)


# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

string1 = "Hello world, I love python."
count = 0
     
for i in range(0, len(string1)):
    if string1[i] == " ":
        count += 1
print(count)


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

string1 = "HeLlO wOrlD, I loVe pYthON."
countUpper = 0
countLower = 0
for i in range(0, len(string1.replace(" ",""))):
    if string1[i] ==string1[i].upper():
        countUpper+= 1
    else:
        countLower+=1

print(f"Upper case: {countUpper}")
print(f"Lower case: {countLower}")

# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

#     >>>my_sum([1,5,4,2])
#     >>>12

list1 = [1,5,4,2]

def my_sum(list1):
    sum = 0
    for i in list1:
        sum+=i
    return sum

my_sum(list1)




# Exercise 5
# Instructions
# Write a function to find the max number in a list

#     >>>find_max([0,1,3,50])
#     >>>50

list1= [0,1,3,50]

def find_max(list1):
    max = 0
    for i in list1:
        if i>max:
            max = i
    return max

find_max(list1)


# Exercise 6
# Instructions
# Write a function that returns factorial of a number

#     >>>factorial(4)
#     >>>24

def factorial(num):
    fact = 1
    for num in range(2, num + 1):
        fact *= num
    return fact

factorial(4)


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

#     >>>list_count(['a','a','t','o'],'a')
#     >>>2

def list_count(list,character):
    count = 0
    for i in list:
        if i == character:
            count+=1
    return count

list_count(['a','a','t','o'],'a')

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

#     >>>norm([1,2,2])
#     >>>3
import numpy as np

def norm(list):
    sum=0
    for i in list:
        sum+= (i**2)
    return(int(np.sqrt(sum)))

norm([1,2,2])


# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

#     >>>is_mono([7,6,5,5,2,0])
#     >>>True

#     >>>is_mono([2,3,3,3])
#     >>>True

#     >>>is_mono([1,2,0,4])
#     >>>False


def is_mono(list):
    return (all(list[i] <= list[i + 1] for i in range(len(list) - 1)) or
            all(list[i] >= list[i + 1] for i in range(len(list) - 1)))

is_mono([7,6,5,5,2,0])
is_mono([2,3,3,3])
is_mono([1,2,0,4])


# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

list = ["Hello","world","I","love","python"]

def longest_word(list):
    wordLength = 0
    longestWord = []
    for i in list:
        if len(i) >= wordLength:
            wordLength = len(i)
            longestWord.append(i)
    return longestWord.pop()
        
     
longest_word(list)






# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.


list = ["123",12,"wasd",123.1435,5342,"you"]

def separateIntStr(list):
    intList=[]
    strList=[]
    for i in list:
        if type(i) == int:
            intList.append(i)
        elif type(i) == str:
            strList.append(i)

    return print(f"str: {strList}, int: {intList}")


separateIntStr(["123",12,"wasd",123.1435,5342,"you"])


# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

#     >>>is_palindrome('radar')
#     >>>True

#     >>>is_palindrome('John)
#     >>>False


def is_palindrome(string):
    palindrome = False
    if(string == string[::-1]):
        palindrome =True
    return palindrome

is_palindrome('radar')
is_palindrome('John')
        

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

#     >>>sentence = 'Do or do not there is no try'
#     >>>k=2
#     >>>sum_over_k(sentence,k)
#     >>>3

sentence = 'Do or do not there is no try'
k=2

def sum_over_k(sentence,k):
    list = sentence.split(" ")
    count= 0
    for i in list:
        if len(i) > k:
            count+=1
    return count

sum_over_k(sentence,k)

# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

#     >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
#     >>>3
dict()

my_dict = {'a': 1,'b':2,'c':8,'d': 1}


def dict_avg(my_dict):
    totalSum = sum(my_dict.values())
    num = len(my_dict)
    avg = totalSum/num

    return avg

dict_avg(my_dict)


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

#     >>>common_div(10,20)
#     >>>[2,5,10]

def common_div(num1,num2):
    div = []
    for i in range (1,num1+1):
        if num1%i == num2%i:
            div.append(i)
    return div

common_div(10,20)







# Exercise 16
# Instructions
# Write a function that test if a number is prime:

#     >>>is_prime(11)
#     >>>True


def is_prime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(False)
                break
        else:
            print(True)
    else:
        print(False)

is_prime(11)


# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

#     >>>weird_print([1,2,2,3,4,5])
#     >>>[2,4]

list = [1,2,2,3,4,5]
weird = []
def weird_print(list):
    for index, value in enumerate(list):
        if value % 2== 0 and index%2==0:
            weird.append(value)
    return weird

weird_print([1,2,2,3,4,5])

# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

#     >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
#     >>>int: 1, str:1 , float:1, bool:2


def type_count(**kwargs):
    intCount=0
    strCount=0
    floatCount=0
    boolCount=0
    for key,value in kwargs.items():
        print(type(value))
        print(value)
        if str(type(value)) == "<class 'int'>":
            intCount +=1
        elif str(type(value)) == "<class 'str'>":
            strCount+=1
        elif str(type(value)) == "<class 'float'>":
            floatCount+=1
        elif str(type(value)) == "<class 'bool'>":
            boolCount+=1

    return print(f"int: {intCount}, str: {strCount}, float: {floatCount}, bool: {boolCount} ")


type_count(a=1,b='string',c=1.0,d=True,e=False)


# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.
# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

string = "Hello world, I love python"
sep = " "


def my_split(string,sep):
    wordList = []
    word = ''
    for i in string:
        if i not in sep:
            word += i
        elif word:
            wordList.append(word)
            word = ''

    if word:
        wordList.append(word)

    return wordList
    
my_split(string,sep)





# Exercise 20
# Instructions
# Convert a string into password format.
# Example:
# input : "mypassword"
# output: "***********"


string = "mypassword"
password = "*" * len(string)
print(password)



# Create a file called operators.py

# Create 2 functions : addOperator(x,y) that returns the addition of 2 numbers, and divideOperator(x,y) that returns the division of 2 numbers

# Create another file called calculator.py, and import the operators module. Call the 2 functions and display the results

# Do this process 3 times :

# once by importing the whole module
# the second time by importing specific functions
# the third time by using alias

operators.py
def addOperator(x,y):
    return x+y

def divideOperator(x,y):
    return x/y


  
  
  
calculator.py
from operators.py import addOperators as ad,DivideOperators as dv


