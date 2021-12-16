"""Write a Python program to construct the following pattern, using a nested for
loop.
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""

a=5;
for i in range(a):
    for j in range(i):
        print ('*', end="")
    print('')

for i in range(a,0,-1):
    for j in range(i):
        print('*', end="")
    print('')