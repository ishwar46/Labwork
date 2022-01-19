# 2.Write a Python program to sum three given integers. However, if two or more values are equal sum will be zero.

a = 1
b = 3
c = 4
sum = a+b+c
if a == b or b == c or a == c:
    print("Sum is zero")
else:
    print(sum)
