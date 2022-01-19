#Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
a=[0,1,2,3,4,4,5,6]
for i in range (a):
    if i==3 and i==6:
        continue
        print("the numbers are",a)
