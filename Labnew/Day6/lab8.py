# 8. Write a Python function to sum all the numbers in a list.
# list = [8,2,3,0,7]
total = 0
num = [8, 2, 3, 0, 7]

for a in range(0, len(num)):
	total = total + num[a]

print("Sum of all number in list: ", total)
