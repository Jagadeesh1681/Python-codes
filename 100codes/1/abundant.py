#abundant number.py
n=int(input("Enter a number :"))
num=0
for i in range(1,n):
	if ( n%i == 0):
		num=num+i
if (num > n):
	print("{} is a abundant number".format(n))
else:
	print("{} is not a abundant number".format(n))
