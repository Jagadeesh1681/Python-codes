#greatest of 3 numbers.
a=int(input("Enter first num :"))
b=int(input("Enter second num :"))
c=int(input("Enter third num :"))
if (a>b) and (a>c):
	print("{} is the greatest of ({} , {} , {})".format(a,a,b,c))
elif (b>c):
	print("{} is the greatest of ({} , {} , {})".format(b,a,b,c))
else:
	print("{} is the greatest of ({} , {} , {})".format(c,a,b,c))
