# Instructions
# Challenge 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.
# Examples


userInput = input()
# myList = []
# myList = [char for char in userInput]

# print(myList)

# for i in myList:
#     print(i)
# [j for j in range(len(userInput)) if string.startswith(i, j)]

# wordDict =dict.fromkeys(userInput," ")
# userInput = "froggy"
#myList = [char for char in userInput]
#[j for j in range(len(userInput)) if userInput.startswith(i, j)]
#for i in enumerate(userInput):
#    wordDict = {i : ""}

for i in enumerate(userInput):
    wordDict = {i : [j for j in range(len(userInput)) if userInput.startswith(i, j)]  for i in [char for char in userInput]}

# wordDict






keyList=[]
valueList = []


{key: value for value, key in enumerate(userInput)}

string = "froggy"

dictOfWords = dict.fromkeys(string , 2)

for i in range(0,len(string)):
    print(i)




# "dodo" ➞ { "d": [0, 2], "o": [1, 3] }
# "froggy" ➞ { "f":  [0], "r": [1], "o": [2], "g": [3, 4], "y": [5] }
# "grapes" ➞ { "g": [0], "r": [1], "a": [2], "p": [3]}


# Challenge 2
# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Examples

# The key is the product, the value is the price

# items_purchase = {
#   "Water": "$1",
#   "Bread": "$3",
#   "TV": "$1,000",
#   "Fertilizer": "$20"
# }

wallet = "$300"
afford= []

purchase = list(items_purchase.keys())
purchase.sort()

total = int(wallet.replace("$","").replace(",",""))

for item in purchase:
  price = int(items_purchase[item].replace("$","").replace(",",""))
  print(price)
  if (price <= total):
    afford.append(item)

if len(afford) ==0 :
  print("# ➞ Nothing")
else:
  print(afford)

  

# ➞ ["Bread", "Fertilizer", "Water"]

# items_purchase = {
#   "Apple": "$4",
#   "Honey": "$3",
#   "Fan": "$14",
#   "Bananas": "$4",
#   "Pan": "$100",
#   "Spoon": "$2"
# }

# wallet = "$100" 

# ➞ ["Apple", "Bananas", "Fan", "Honey", "Pan", "Spoon"]

items_purchase = {
  "Phone": "$999",
  "Speakers": "$300",
  "Laptop": "$5,000",
  "PC": "$1200"
}

wallet = "$1" 

# ➞ "Nothing"
