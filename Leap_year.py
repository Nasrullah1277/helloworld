year=int(input("Enter a year: "))
remainder= year % 4

if (remainder == 0):
	print(year,"is a leap year")
else:
	print(year," is not a leap year")