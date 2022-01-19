#Write a Python program that accepts a string and calculate the number of digits and letters

str = input("Input a string: ")
d=l=0
for c in str:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
print("The number pf Letters", l)
print("The number of Digits", d)