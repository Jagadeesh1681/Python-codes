#greatest of 2 numbers.
a=int(input("Enter first number :"))
b=int(input("Enter second number :"))
if (a>b):
	print("{} is the greatest of ({},{})".format(a,a,b))
else:
	print("{} is the greatest of ({},{})".format(b,a,b))
