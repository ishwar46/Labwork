#Write a program that asks the user for a number in the range 1 through 12. The program should display the corresponding month of the year, where 1 = January, 2 = February, 3 = March, 4 = April, 5 = May, 6 = June, 7 = July, 8 = August, 9 = September, 10 = October, 11 = November, and 12 = December. The program should display an error message if the user enters a number that is outside the range of 1 through 12

month = {
	1:"January",
	2:"February",
	3:"March",
	4:"April",
	5:"May",
	6:"June",
	7:"July",
	8:"August",
	9:"September",
	10:"October",
	11:"November",
	12:"December"}

try:
	n = int(input('Enter the month number: '))
	print(month[n])
except (ValueError, KeyError):
	print('Please enter number from 1 to 12 only.')