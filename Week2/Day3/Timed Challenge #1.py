# Perfect Number
# A perfect number is a positive integer that is equal to the sum of its divisors.
# However, the number itself is not included in the sum.

# Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
# Hint: Google perfect numbers
# Example

# Input -- Enter the number:6
# Output -- True

# Input -- Enter the number:10
# Output --  False


number = int(input("Enter the number: "))
sum= 0

for i in range(1,number):
    print(i)
    if(number%i==0):
      sum += i
      print(sum)

print(sum)

if (sum == number):
  print(f"{number} is a perfect number")
else:
  print(f"{number} not a perfect number")
