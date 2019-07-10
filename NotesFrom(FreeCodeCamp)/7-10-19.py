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








