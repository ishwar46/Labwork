#4. Given three integers, print the smallest one. (Three integers should be user input)

a = int(input('Enter first number  : '))
b = int(input('Enter second number : '))
c = int(input('Enter third number  : '))

smallest = 0

if a < b and a < c :
    smallest = a
if b < a and b < c :
    smallest = b
if c < a and c < b :
    smallest = c

print(smallest, "is the smallest of three numbers.")