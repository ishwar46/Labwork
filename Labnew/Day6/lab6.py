math = int(input("Enter obtained marks: "))
programming = int(input("Enter obtained marks: "))
android = int(input("Enter obtained marks: "))
database = int(input("Enter obtained marks: "))

total = (math+programming+android+database)
avg = (math+programming+android+database)/4

print(f"Total Obtained Marks is: {total}")
print(f"Obtained Percentage is: {avg}")

if(avg>90):
    print("Congratulations! Your Grade is A+")
elif(avg>=80 and avg<90):
    print("Congratulations! Your Grade is A")
elif(avg>=70 and avg<80):
    print("Congratulations! Your Grade is B")
elif(avg>60 and avg<70):
    print("Congratulations! Your Grade is C")
elif(avg>50 and avg<60):
    print("Congratulations! Your Grade is D")
else:
    print("Sorry you have failed!")