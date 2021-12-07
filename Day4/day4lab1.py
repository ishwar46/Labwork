""" #1 Check whether the given year is leap year or not. If year is leap print ‘LEAP YEAR’ else print ‘COMMON YEAR’."""

year = int(input("Enter year: "))

if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is a COMMON YEAR")