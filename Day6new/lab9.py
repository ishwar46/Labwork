#Write a program function to find min of three numbers.(no parameter and no return type)

a = int(input("Enter any number: "))
b = int(input("Enter any number: "))
c = int(input("Enter any number: "))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "is the smallest of three numbers.")