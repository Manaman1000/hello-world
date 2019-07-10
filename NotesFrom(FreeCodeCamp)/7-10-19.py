## Basic Calculator
## Purpose: implementation of if/elif/else, checking valid operators statements 

num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter a second number: "))
if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invlaid operator")
    
####################################################################################################################################
    
    
## DICTIONARIES
## Purpose: Introduce DICTIONARIES
## Goal: take 3-letter representations of months and spit out the full name of the month by retrieving this info from a dictionary

## Each Item in a dictionary takes two values, and the first must be unique. You can have multiple items refer to the same thing
## (as shown below)
###Q: Can you have multiple things reference one item on one line?

monthConversions = {
    "JAN":"January",
    "FEB":"February",
    "MAR":"March",
    "APR":"April",
    "MAY":"May",
    "JUN":"June",
    "JUL":"July",
    "AUG":"August",
    "SEP":"September",
    "OCT":"October",
    "NOV":"November",
    "DEC":"December",
    
    0:"January",
    1:"February",
    2:"March",
    3:"April",
    4:"May",
    5:"June",
    6:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"
}

print(monthConversions.get(12,"Not a Valid Key"))
print(monthConversions.get("DEC","Not a Valid Key"))
print(monthConversions.get(14,"Not a Valid Key"))

# the condition after the comma is a 'default' statement that only is shown if the 
# prior item is not found in the dictionary being referenced


####################################################################################################################################


##WHILE LOOPS
i=1
while i<=10:
  print(i)
   i+=1

print("Done with Loop")
# it's a while loop, what else is there to say?


####################################################################################################################################

## FOR LOOPS

friends = ["George", "Pankaj", "Sarah", "Gabby", "Jesse"]

for index in friends:
    print(index)
    
for index in range(len(friends)):
    print(friends[index])
    
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not First")
    
for index in range(7,12):
    print(index)
    
for letter in "Giraffe Academy":
    print(letter)

####################################################################################################################################
# Exponents Function
# GOAL: Create a function that will take a base number and raise it to a power numer

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result
    
print(raise_to_power(2,3))




####################################################################################################################################
## 2-D lists and Nested Loops

#Each item in this list, is going to be another array/list
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(number_grid[0][0])

for row in number_grid:
    for column in row:
        print(column)



####################################################################################################################################
## Translators
## GOAL: Create a program that changes any vowel in any string into a "g"
## deals with nested if statements, and some char/string operations

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation
    
print(translate(input("Enter a phrase: ")))



####################################################################################################################################
## Try-Except catches (Catching Errors)

## Always (when catching expcept )


try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("invalid input")



####################################################################################################################################
