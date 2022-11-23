# Exercise 1 : Cars
# Instructions
# Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
# Convert it into a list using Python (don’t do it by hand!).
# Print out a message saying how many manufacturers/companies are in the list.
# Print the list of manufacturers in reverse/descending order (Z-A).
# Using loops or list comprehension:
# Find out how many manufacturers’ names have the letter ‘o’ in them.
# Find out how many manufacturers’ names do not have the letter ‘i’ in them.



carManufacturer = ("Volkswagen, Toyota, Ford Motor, Honda, Chevrolet").split(",")

print(f"There are {len(carManufacturer)} car manufacturers in the list.")

sorted(carManufacturer,reverse=True)

car_o = [car for car in carManufacturer if "o" in car.lower()]
print(f"There are {len(car_o)} car manufacturers' names with letter 'o' in them")

car_not_i = [car for car in carManufacturer if not "i" in car.lower()]
print(f"There are {len(car_not_i)} car manufacturers's names without letter 'i' in them ")


# Bonus: There are a few duplicates in this list:["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
# Remove these programmatically. (Hint: you can use set to help you).
# Print out the companies without duplicates, in a comma-separated string with no line-breaks (eg. “Acura, Alfa Romeo, Aston Martin, …”), also print out a message saying how many companies are now in the list.

# Bonus: Print out the list of manufacturers in ascending order (A-Z), but reverse the letters of each manufacturer’s name.

duplicate_car = ["Honda","Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
set(duplicate_car)

newCarManufacturer = ', '.join([str(car) for car in set(duplicate_car)])
newCarManufacturer = newCarManufacturer.split(", ")
print(f"There are {len(list(newCarManufacturer))} car manufacturers.")

sorted(carManufacturer)

[car[::-1] for car in sorted(newCarManufacturer)]-



