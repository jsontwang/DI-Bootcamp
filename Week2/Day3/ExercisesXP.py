# 🌟 Exercise 1 : Convert Lists Into Dictionaries
# Instructions
# Convert the two following lists, into dictionaries.
# Hint: Use the zip method
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}


keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]


exerciseDict = dict(zip(keys,values))

# 🌟 Exercise 2 : Cinemax
# Instructions
# A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# Given the following object:

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}


# How much does each family member have to pay ?

# Print out the family’s total cost for the movies.
# Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).


family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total = 0
for key, values in family.copy().items():
    
    ticket =0
    if values <3:
        ticket = 0
    elif values > 12:
        ticket = 15
    else:
        ticket = 10
    
    total = total + ticket

    print(f"{key} pays {ticket}")
print(f"total:{total}")   



familyInput = input("Input name seperated by space:")
familyAge = input("Input age seperated by space:")

familyNameList = familyInput.split()
familyAgeList = familyAge.split()


familyDict = dict(zip(familyNameList,familyAgeList))








# 🌟 Exercise 3: Zara
# Instructions
# Here is some information about a brand.
# name: Zara 
# creation_date: 1975 
# creator_name: Amancio Ortega Gaona 
# type_of_clothes: men, women, children, home 
# international_competitors: Gap, H&M, Benetton 
# number_stores: 7000 
# major_color: 
#     France: blue, 
#     Spain: red, 
#     US: pink, green





# 2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).

zaraDict = {
    "name": "Zara" ,
    "creation_date": 1975 ,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": {"men", "women", "children", "home"} ,
    "international_competitors": {"Gap", "H&M", "Benetton"} ,
    "number_stores": 7000 ,
    "major_color": {"France": "blue", "Spain": "red", "US": {"pink", "green"}}
}
# 3. Change the number of stores to 2.
zaraDict["number_stores"] = 2

# 4. Print a sentence that explains who Zaras clients are.

client = zaraDict["type_of_clothes"]

print(f"Zara primary clients are yound to middle aged adults interested in  {client[0]}, {client[1]}, {client[2]} and {client[3]} clothing.")


# 5. Add a key called country_creation with a value of Spain.

key = {"country_creation":"Spain"}

zaraDict.update(key)

# 6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.

zaraDict["international_competitors"].append("Desigual")


# 7. Delete the information about the date of creation.
zaraDict.pop("creation_date")

# 8. Print the last international competitor.
zaraDict["international_competitors"][-1]

# 9. Print the major clothes colors in the US.
zaraDict["major_color"]["US"]


# 10. Print the amount of key value pairs (ie. length of the dictionary).
len(zaraDict)


# 11. Print the keys of the dictionary.
for key in enumerate(zaraDict):
    print(key)



# 12. Create another dictionary called more_on_zara with the following details:

more_on_zara = {"creation_date": 1975 ,"number_stores": 10000 }

# creation_date: 1975 
# number_stores: 10 000


# 13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
zaraDict.update(more_on_zara)

# 14. Print the value of the key number_stores. What just happened ?
zaraDict["number_stores"]
#The value 2 has been overwritten by the second value 10000 when using update function


# Exercise 4 : Disney Characters
# Instructions
# Use this list :

users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
# Analyse these results :

# #1/

# >>> print(disney_users_A)
# {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}
disney_users_A = list({})
for key, values in enumerate(users):
    disney_users_A.append(f"{values}: {key}")


# #2/

# >>> print(disney_users_B)
# {0: "Mickey",1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}



disney_users_B = list({})
for key, values in enumerate(users):
    disney_users_B.append(f"{key}: {values}")


# #3/ 

# >>> print(disney_users_C)
# {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}

disney_users_C = list({})

userList = sorted(users)

for key, values in enumerate(userList):
    disney_users_C.append(f"{values}: {key}")


# Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
# Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.
# Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
# Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.

print({key: value for value, key in enumerate(users) if "i" in key })

print({key: value for value, key in enumerate(users) if key[0].lower() in ["m","p"] })
