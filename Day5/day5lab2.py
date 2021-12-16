"""Write a Python program to convert temperatures to and from celsius,
fahrenheit"""

f = float(input("Enter temperature in Fahrenheit: "))

c = 5 * (f-32)/9

print("The tempeature in Celsius:",round(c,2))