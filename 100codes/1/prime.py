#Prime number.py
n=int(input("Enter a number :"))
factors=0
for i in range(2,n):
	if (n%i == 0):
		factors=factors+1
if (factors == 0):
	print("{} is a Prime number".format(n))
else:
	print("{} is a Composite number".format(n))
		
