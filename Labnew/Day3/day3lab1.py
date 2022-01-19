math = int(input("Enter obtaibed makrs: "))
programming = int(input("Enter obtained marks: "))
android = int(input("Enter obtained marks: "))
sdesign = int(input("Enter obtained marks: "))
database= int(input("Enter obtained marks: "))

total = (math+programming+android+sdesign+database)
avg = (math+programming+android+sdesign+database)/5

print(f"Obained Marks is: {total}")
print(f"Obainted Percentage is: {avg}")

if(avg>90):
    print("Congratulations! Your Grade is A")
elif(avg>=80 and avg<90):
    print("Congratulations! Your Grade is B")
elif(avg>=70 and avg<80):
    print("Congratulations! Your Grade is C")
elif(avg>60 and avg<70):
    print("Congratulations! Your Grade is D")
else:
    print("Sorry you have failed!")

"""a=[1,2,3,4,5]
if a:=5:
    print("5 is in the list")
else:
    print("5 is not in the list")"""

