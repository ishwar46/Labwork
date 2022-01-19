#Write a program function to find max of three numbers.(no parameter and no return type)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the Third number: "))

def max():

    if (num1 > num2):
        if (num1 > num3):
            largest = num1
        else:
            largest = num3
    else:
        if num2 > num3:
            largest = num2

        else:
            largest = num3
        print("Maximum number of all three is: ", largest)
max()