n=int(input("Enter a number :"))
a=(2*n)
for i in range(1,a+1):
	if (i <= n):
		print(" "*(n-i) + "*"*(2*i-1))
	else:
		print(" "*(i-n) + "*"*(2*a-2*i-1))
	
