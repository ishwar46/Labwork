#Write a Python program to multiply all the numbers in a list. Sample list = [8,2,3,-1,7]

def multi (a) :
    multiply = 1
    for i in a :
        multiply *= i
    print ("Answer after multiply: ", multiply)
list = eval(input("Enter a List : "))
multi(list)