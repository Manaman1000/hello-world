# Working with FILES
# PULLS FROM A .TXT FILE CALLED 'employees.txt' WITH THE FOLLOWING CONTENTS
# Jim - Salesman
# Dwight - Salesman
# Pam - Receptionist
# Michael - Manager
# Oscar - Accountant

#Reading Files in Python

employee_file = open("employees.txt", "r")
#"r" stands for read
#"w" stands for write (as in you can change existing and add in new info)
#"a" means append (can add new info to the end of the file)
#"r+" read and write

print(employee_file.readable())


#print(employee_file.readline())
# If you create anohter one of these, it will read the NEXT line in the file
#print(employee_file.readline())
#print(employee_file.readline())
#print(employee_file.readline())


print(employee_file.readlines()[1])
#to read all lines 


for employee in employee_file.readlines():
    print(employee)
# to print out every line in the file

employee_file.close()



##########################################################################################################################
# WRITING NEW FILES/ APPENDING TO THEM



employee_file = open("employees.txt", "a")

employee_file.write("\nToby - Human Resources")
#Be careful with this since once you do append to the file, it is 'permanent'
#the \n makes sure it is on a new line



employee_file = open("employees1.txt", "w")
#w overwrites your existing file or can create a new one
employee_file.write("\nKelly - Customer Service")
#This creates a new file and puts the above line as the only content ( or overwrites it if it already exists.)


employee_file = open("index.html", "w")
employee_file.write("<p> This is HTML </p>")



employee_file.close()

##########################################################################################################################
##########################################################################################################################
