#perfect number.py
n=int(input("Enter a number :"))
sum=0
for i in range(1,n//2+1):
	if (n % i == 0):
		sum=sum+i
if (sum == n):
	print("{} is a perfect number".format(n))
else:
	print("{} is not a perfect number".format(n))
	
	
