#sum of numbers in given range.
a=int(input("Enter first num :"))
b=int(input("Enter second num :"))
sum=0
if (b>a):
	for i in range(a,b+1):
		sum=sum+i
	print("The sum of numbers in b/n {} and {} = {}".format(a,b,sum))
else:
	for i in range(b,a+1):
		sum=sum+i
	print("The sum of numbers in b/n {} and {} = {}".format(b,a,sum))
		
