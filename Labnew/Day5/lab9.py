#Write a program to find the factorial of a number.

n = int(input("Enter a number: "))
for i in range(1,n+1):
	if not n%i:
		print(i,end=" ")